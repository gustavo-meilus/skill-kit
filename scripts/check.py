#!/usr/bin/env python3
"""Run Skill Kit's focused tests and strict OpenSpec validation."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    commands = [
        [sys.executable, str(path.relative_to(ROOT))]
        for path in sorted(ROOT.rglob("test_*.py"))
        if "__pycache__" not in path.parts
    ]

    openspec = shutil.which("openspec")
    if not openspec:
        print("check: openspec is required", file=sys.stderr)
        return 127
    commands.append([openspec, "validate", "--all", "--strict", "--no-interactive"])

    for command in commands:
        print("+", " ".join(command), flush=True)
        completed = subprocess.run(command, cwd=ROOT, check=False)
        if completed.returncode:
            return completed.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
