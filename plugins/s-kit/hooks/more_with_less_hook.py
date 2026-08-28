#!/usr/bin/env python3
"""Codex lifecycle hook for the More With Less engineering policy.

The hook is intentionally narrow:
- SessionStart/SubagentStart: inject a small policy reminder.
- Stop: if the git working tree changed, run the project's authoritative check
  when configured via MORE_WITH_LESS_CHECK or an executable scripts/check.
- A failing check forces at most one continuation per turn.

It does not try to infer whether a dependency, abstraction, agent, or tool is
semantically justified; that belongs in the Skill, not brittle shell parsing.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any

POLICY = (
    "More With Less is active for project-development work. Use the minimum "
    "sufficient mechanism; understand before simplifying; prefer existing, "
    "native, and deterministic solutions; minimize context, tools, authority, "
    "state, agents, and handoffs; make specification and verification "
    "proportional to risk; never simplify away required correctness, security, "
    "data-integrity, accessibility, operability, observability, or acceptance "
    "guarantees. For non-trivial work, load and follow $more-with-less."
)


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, separators=(",", ":")))


def run(argv: list[str], cwd: Path, timeout: int = 10) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        argv,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )


def git_root(cwd: Path) -> Path | None:
    try:
        result = run(["git", "rev-parse", "--show-toplevel"], cwd, timeout=5)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return Path(value) if value else None


def working_tree_changed(root: Path) -> bool:
    try:
        result = run(["git", "status", "--porcelain", "--untracked-files=normal"], root, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0 and bool(result.stdout.strip())


def project_check(root: Path) -> tuple[str, str | list[str]] | None:
    override = os.environ.get("MORE_WITH_LESS_CHECK", "").strip()
    if override:
        return ("shell", override)

    script = root / "scripts" / "check"
    if script.is_file() and os.access(script, os.X_OK):
        return ("argv", [str(script)])

    return None


def run_project_check(root: Path, command: tuple[str, str | list[str]]) -> tuple[int, str]:
    timeout = int(os.environ.get("MORE_WITH_LESS_CHECK_TIMEOUT", "280"))
    try:
        if command[0] == "shell":
            result = subprocess.run(
                str(command[1]),
                cwd=str(root),
                shell=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=timeout,
                check=False,
            )
        else:
            argv = list(command[1])  # type: ignore[arg-type]
            if os.name == "nt" and Path(argv[0]).suffix == "":
                shell = shutil.which("sh")
                git_shell = Path(os.environ.get("ProgramFiles", r"C:\\Program Files")) / "Git/bin/sh.exe"
                if shell or git_shell.is_file():
                    argv.insert(0, shell or str(git_shell))
            result = run(argv, root, timeout=timeout)
        return result.returncode, result.stdout or ""
    except subprocess.TimeoutExpired as exc:
        partial = exc.stdout or ""
        if isinstance(partial, bytes):
            partial = partial.decode(errors="replace")
        return 124, f"Verification timed out after {timeout}s.\n{partial}"
    except OSError as exc:
        return 126, f"Could not run verification command: {exc}"


def tail(text: str, limit: int = 2200) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return "...\n" + text[-limit:]


def start_context(event: str) -> None:
    emit(
        {
            "hookSpecificOutput": {
                "hookEventName": event,
                "additionalContext": POLICY,
            }
        }
    )


def stop_gate(data: dict[str, Any]) -> None:
    cwd = Path(data.get("cwd") or os.getcwd())
    root = git_root(cwd)
    if root is None or not working_tree_changed(root):
        emit({})
        return

    command = project_check(root)
    if command is None:
        emit(
            {
                "systemMessage": (
                    "More With Less: the working tree changed, but no authoritative "
                    "completion command is configured. Report only the checks and "
                    "evidence actually run; do not imply unperformed verification. "
                    "Set MORE_WITH_LESS_CHECK or provide executable ./scripts/check "
                    "to enable the mechanical Stop gate."
                )
            }
        )
        return

    code, output = run_project_check(root, command)
    if code == 0:
        emit({})
        return

    evidence = tail(output) or f"verification exited with status {code}"
    reason = (
        "More With Less completion gate: authoritative project verification failed. "
        "Fix the relevant failure and rerun verification. If the failure is unrelated "
        "or cannot be resolved within scope, report it explicitly and do not claim "
        f"successful verification.\n\nVerification output:\n{evidence}"
    )

    if not bool(data.get("stop_hook_active")):
        emit({"decision": "block", "reason": reason})
        return

    emit(
        {
            "continue": True,
            "systemMessage": (
                "More With Less: verification still fails after the one bounded Stop "
                "continuation. Do not claim completion or a passing check. Report the "
                f"failure and evidence accurately. Last output: {tail(evidence, 1000)}"
            ),
        }
    )


def main() -> int:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as exc:
        emit({"systemMessage": f"More With Less hook received invalid JSON: {exc}"})
        return 0

    event = str(data.get("hook_event_name") or "")
    if event == "SessionStart":
        start_context("SessionStart")
    elif event == "SubagentStart":
        start_context("SubagentStart")
    elif event == "Stop":
        stop_gate(data)
    else:
        emit({})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
