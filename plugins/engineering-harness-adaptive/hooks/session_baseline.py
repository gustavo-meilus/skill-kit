#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from harness_common import find_repo_root, load_baseline, save_baseline, workspace_snapshot


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    cwd = event.get("cwd") or "."
    session_id = str(event.get("session_id") or event.get("sessionId") or "unknown")
    root = find_repo_root(cwd)

    # SessionStart also runs after compaction/resume. Never overwrite a baseline
    # that already represents the last verified state for this session.
    if load_baseline(root, session_id) is None:
        save_baseline(root, session_id, workspace_snapshot(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
