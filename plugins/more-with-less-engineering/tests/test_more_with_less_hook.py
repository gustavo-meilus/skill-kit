from __future__ import annotations

import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest

HOOK = Path(__file__).resolve().parents[1] / "hooks" / "more_with_less_hook.py"


def call_hook(payload: dict, cwd: Path, env: dict[str, str] | None = None) -> dict:
    merged = os.environ.copy()
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
    def make_repo(self) -> Path:
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        return root

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
        self.assertNotIn("decision", out)

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
