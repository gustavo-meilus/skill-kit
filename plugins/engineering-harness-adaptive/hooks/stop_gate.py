#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

from harness_common import (
    changed_since,
    find_repo_root,
    load_baseline,
    load_config,
    only_documentation_changes,
    save_baseline,
    load_retry_count,
    save_retry_count,
    truncate,
    workspace_snapshot,
)


def emit(payload: dict) -> int:
    print(json.dumps(payload, ensure_ascii=False))
    return 0


def failure_decision(reason: str, root: Path, session_id: str) -> int:
    count = load_retry_count(root, session_id)
    if count == 0:
        save_retry_count(root, session_id, 1)
        return emit(
            {
                "decision": "block",
                "reason": (
                    "The engineering harness blocked completion. Resolve the verification issue, rerun the relevant checks, "
                    "then attempt completion again. Do not weaken the oracle merely to obtain green output. "
                    "If the issue cannot be resolved within the requested scope, preserve the failure evidence and say so.\n\n"
                    + reason
                ),
            }
        )
    if count == 1:
        save_retry_count(root, session_id, 2)
        return emit(
            {
                "decision": "block",
                "reason": (
                    "Verification is still failing after the automatic correction attempt. Do not start another speculative repair loop. "
                    "Either make one clearly justified final correction if the cause is now deterministic, or report the failing evidence, "
                    "residual risk, and concrete next action. Then stop.\n\n"
                    + reason
                ),
            }
        )
    # A third failing stop is allowed so the agent can report failure instead of looping forever.
    save_retry_count(root, session_id, 0)
    return emit({})


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return emit({})

    cwd = event.get("cwd") or "."
    session_id = str(event.get("session_id") or event.get("sessionId") or "unknown")
    root = find_repo_root(cwd)

    baseline = load_baseline(root, session_id)
    current = workspace_snapshot(root)

    # If the hook was enabled mid-session and no baseline exists, establish one
    # instead of guessing which pre-existing workspace changes belong to the agent.
    if baseline is None:
        save_baseline(root, session_id, current)
        save_retry_count(root, session_id, 0)
        return emit({})

    changed_paths = changed_since(baseline, current)
    if not changed_paths:
        save_retry_count(root, session_id, 0)
        return emit({})

    # Editorial documentation changes should not force a project build/test gate.
    if only_documentation_changes(changed_paths):
        save_baseline(root, session_id, current)
        save_retry_count(root, session_id, 0)
        return emit({})

    try:
        config = load_config(root)
    except RuntimeError as exc:
        return failure_decision(str(exc), root, session_id)

    verifier = Path(__file__).resolve().parents[1] / "scripts" / "engineering_verify.py"
    if not verifier.exists():
        return failure_decision(
            f"Missing harness verifier script: {verifier}. Restore the harness or configure an equivalent deterministic gate.",
            root,
            session_id,
        )

    timeout = int(config.get("verification_timeout_seconds", 600)) + 5
    max_output = int(config.get("max_output_chars", 12000))

    try:
        completed = subprocess.run(
            [sys.executable, str(verifier)],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        captured = (exc.stdout or "") if isinstance(exc.stdout, str) else ""
        return failure_decision(
            f"Canonical verification timed out after {timeout - 5}s.\n{truncate(captured, max_output)}",
            root,
            session_id,
        )

    output = truncate(completed.stdout or "", max_output).strip()

    if completed.returncode == 0:
        # The current workspace state is now verified. Future turns only gate new changes.
        save_baseline(root, session_id, current)
        save_retry_count(root, session_id, 0)
        return emit({})

    if completed.returncode == 3 and not bool(config.get("require_verifier_for_code_changes", True)):
        save_baseline(root, session_id, current)
        save_retry_count(root, session_id, 0)
        return emit({})

    if completed.returncode == 3:
        reason = (
            "This turn changed code/configuration, but the repository has no canonical verifier. "
            "Prefer adding a stable scripts/check (or project check/verify target), or set "
            ".engineering-harness.json -> verify_command to the repository's authoritative verification command.\n\n"
            + output
        )
    else:
        reason = f"Canonical verification failed with exit code {completed.returncode}.\n\n{output}"

    return failure_decision(reason, root, session_id)


if __name__ == "__main__":
    raise SystemExit(main())
