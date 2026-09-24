from __future__ import annotations

import json
import importlib.util
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

HOOK = Path(__file__).resolve().parents[1] / "hooks" / "more_with_less_hook.py"
HOOK_MANIFEST = HOOK.parent / "hooks.json"
HOOK_SPEC = importlib.util.spec_from_file_location("more_with_less_hook", HOOK)
HOOK_MODULE = importlib.util.module_from_spec(HOOK_SPEC)
assert HOOK_SPEC and HOOK_SPEC.loader
HOOK_SPEC.loader.exec_module(HOOK_MODULE)


def call_hook(payload: dict, cwd: Path, env: dict[str, str] | None = None) -> dict:
    merged = os.environ.copy()
    merged.pop("MORE_WITH_LESS_CHECK", None)
    merged.pop("MORE_WITH_LESS_CHECK_TIMEOUT", None)
    if env:
        merged.update(env)
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        cwd=str(cwd),
        input=json.dumps(payload),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=merged,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return json.loads(result.stdout or "{}")


class HookTests(unittest.TestCase):
    def test_windows_command_uses_powershell_plugin_root(self) -> None:
        manifest = json.loads(HOOK_MANIFEST.read_text(encoding="utf-8"))
        for event in ("SessionStart", "SubagentStart", "Stop"):
            command = manifest["hooks"][event][0]["hooks"][0]["commandWindows"]
            self.assertTrue(command.startswith('python "$env:PLUGIN_ROOT'))
            self.assertIn("$env:PLUGIN_ROOT", command)
            self.assertNotIn("%PLUGIN_ROOT%", command)

    def make_repo(self) -> Path:
        td = tempfile.TemporaryDirectory(prefix="skill kit ")
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        return root

    def test_git_diagnostics_are_separate_from_status_output(self) -> None:
        root = self.make_repo()
        result = subprocess.CompletedProcess(
            ["git", "status"], 0, stdout="", stderr="Git diagnostic"
        )
        with patch.object(HOOK_MODULE.subprocess, "run", return_value=result) as run:
            self.assertFalse(HOOK_MODULE.working_tree_changed(root))
        self.assertEqual(run.call_args.kwargs["stderr"], subprocess.PIPE)

    def test_check_selection_precedence(self) -> None:
        root = self.make_repo()
        scripts = root / "scripts"
        scripts.mkdir()
        check = scripts / "check"
        check.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
        check.chmod(check.stat().st_mode | stat.S_IXUSR)
        python_check = scripts / "check.py"
        python_check.write_text("raise SystemExit(1)\n", encoding="utf-8")

        with patch.dict(os.environ, {"MORE_WITH_LESS_CHECK": "echo override"}):
            self.assertEqual(
                HOOK_MODULE.project_check(root), ("shell", "echo override")
            )

        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(HOOK_MODULE.project_check(root), ("argv", [str(check)]))
            check.unlink()
            self.assertEqual(
                HOOK_MODULE.project_check(root),
                ("argv", [sys.executable, str(python_check)]),
            )

    def test_session_start_injects_small_policy(self) -> None:
        root = self.make_repo()
        out = call_hook({"hook_event_name": "SessionStart", "cwd": str(root)}, root)
        spec = out["hookSpecificOutput"]
        self.assertEqual(spec["hookEventName"], "SessionStart")
        self.assertIn("minimum sufficient mechanism", spec["additionalContext"])
        self.assertIn("$more-with-less", spec["additionalContext"])

    def test_stop_without_changes_passes(self) -> None:
        root = self.make_repo()
        out = call_hook({"hook_event_name": "Stop", "cwd": str(root), "stop_hook_active": False}, root)
        self.assertEqual(out, {})

    def test_changed_tree_without_check_warns_but_does_not_block(self) -> None:
        root = self.make_repo()
        (root / "file.txt").write_text("changed", encoding="utf-8")
        out = call_hook({"hook_event_name": "Stop", "cwd": str(root), "stop_hook_active": False}, root)
        self.assertIn("systemMessage", out)
        self.assertIn("working tree has changes", out["systemMessage"])
        self.assertNotIn("decision", out)

    def test_python_check_runs_from_repo_root_when_cwd_is_nested(self) -> None:
        root = self.make_repo()
        (root / "changed.txt").write_text("changed", encoding="utf-8")
        scripts = root / "scripts"
        scripts.mkdir()
        check = scripts / "check.py"
        check.write_text("print('python-check-marker')\nraise SystemExit(9)\n", encoding="utf-8")
        nested = root / "subdirectory"
        nested.mkdir()

        out = call_hook(
            {"hook_event_name": "Stop", "cwd": str(nested), "stop_hook_active": False},
            nested,
        )
        self.assertEqual(out.get("decision"), "block")
        self.assertIn("python-check-marker", out.get("reason", ""))

    def test_timed_out_check_is_reported_as_failure(self) -> None:
        root = self.make_repo()
        (root / "changed.txt").write_text("changed", encoding="utf-8")
        scripts = root / "scripts"
        scripts.mkdir()
        (scripts / "check.py").write_text(
            "import time\nprint('timeout-check-marker', flush=True)\ntime.sleep(3)\n",
            encoding="utf-8",
        )

        out = call_hook(
            {"hook_event_name": "Stop", "cwd": str(root), "stop_hook_active": False},
            root,
            {"MORE_WITH_LESS_CHECK_TIMEOUT": "1"},
        )
        self.assertEqual(out.get("decision"), "block")
        self.assertIn("timed out after 1s", out.get("reason", ""))
        self.assertIn("timeout-check-marker", out.get("reason", ""))

    def test_failed_check_blocks_once(self) -> None:
        root = self.make_repo()
        (root / "file.txt").write_text("changed", encoding="utf-8")
        scripts = root / "scripts"
        scripts.mkdir()
        check = scripts / "check"
        check.write_text("#!/bin/sh\necho failing-check\nexit 7\n", encoding="utf-8")
        check.chmod(check.stat().st_mode | stat.S_IXUSR)
        out = call_hook({"hook_event_name": "Stop", "cwd": str(root), "stop_hook_active": False}, root)
        self.assertEqual(out.get("decision"), "block")
        self.assertIn("failing-check", out.get("reason", ""))

    def test_failed_check_second_stop_warns_without_second_block(self) -> None:
        root = self.make_repo()
        (root / "file.txt").write_text("changed", encoding="utf-8")
        scripts = root / "scripts"
        scripts.mkdir()
        check = scripts / "check"
        check.write_text("#!/bin/sh\necho still-failing\nexit 1\n", encoding="utf-8")
        check.chmod(check.stat().st_mode | stat.S_IXUSR)
        out = call_hook({"hook_event_name": "Stop", "cwd": str(root), "stop_hook_active": True}, root)
        self.assertTrue(out.get("continue"))
        self.assertIn("still fails", out.get("systemMessage", ""))
        self.assertNotIn("decision", out)

    def test_passing_check_passes(self) -> None:
        root = self.make_repo()
        (root / "file.txt").write_text("changed", encoding="utf-8")
        scripts = root / "scripts"
        scripts.mkdir()
        check = scripts / "check"
        check.write_text("#!/bin/sh\necho ok\nexit 0\n", encoding="utf-8")
        check.chmod(check.stat().st_mode | stat.S_IXUSR)
        out = call_hook({"hook_event_name": "Stop", "cwd": str(root), "stop_hook_active": False}, root)
        self.assertEqual(out, {})


if __name__ == "__main__":
    unittest.main()
