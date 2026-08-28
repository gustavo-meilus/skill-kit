#!/usr/bin/env python3
"""Select the GitHub Copilot CLI engineering agent model family.

Usage:
  python scripts/select_copilot_profile.py openai
  python scripts/select_copilot_profile.py anthropic
  python scripts/select_copilot_profile.py anthropic-fable

Only the four engineering agent profiles are replaced.
"""
from __future__ import annotations

from pathlib import Path
import shutil
import sys

VALID = {"openai", "anthropic", "anthropic-fable"}
FILES = (
    "engineering-scout.agent.md",
    "engineering-planner.agent.md",
    "engineering-reviewer.agent.md",
    "engineering-specialist.agent.md",
)


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in VALID:
        print("usage: select_copilot_profile.py openai|anthropic|anthropic-fable", file=sys.stderr)
        return 2

    profile = sys.argv[1]
    root = Path(__file__).resolve().parents[1]
    src = root / "profiles" / "copilot" / profile
    dst = root / "copilot-agents"
    if not src.is_dir():
        print(f"missing profile directory: {src}", file=sys.stderr)
        return 2

    dst.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        source = src / name
        if not source.is_file():
            print(f"missing profile file: {source}", file=sys.stderr)
            return 2
        shutil.copy2(source, dst / name)

    print(f"Installed Copilot engineering profile: {profile}")
    if profile == "openai":
        print("Suggested parent session: GPT-5.6 Sol Medium before calibration; Terra Medium for task classes proven by local evals.")
    elif profile == "anthropic":
        print("Suggested parent session: Claude Opus 5 High before calibration; Medium where local evals show quality holds.")
    else:
        print("WARNING: Claude Fable 5 has model-specific data-retention considerations in GitHub Copilot. Use only when organization policy permits it.")
        print("Suggested parent session: Claude Opus 5 High; Fable xHigh remains specialist-only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
