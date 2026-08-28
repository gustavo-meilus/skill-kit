from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from typing import Any

DEFAULT_CONFIG: dict[str, Any] = {
    "verify_command": None,
    "require_verifier_for_code_changes": True,
    "allow_test_only_fallback": False,
    "verification_timeout_seconds": 600,
    "max_output_chars": 12000,
}

DOC_EXTENSIONS = {".md", ".mdx", ".rst", ".adoc", ".txt"}
DOC_BASENAMES = {
    "README",
    "LICENSE",
    "LICENCE",
    "CHANGELOG",
    "CONTRIBUTING",
    "CODE_OF_CONDUCT",
    "SECURITY",
    "NOTICE",
}


def run_git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(root), *args],
        stderr=subprocess.DEVNULL,
    )


def find_repo_root(cwd: str | Path) -> Path:
    cwd = Path(cwd).resolve()
    try:
        out = subprocess.check_output(
            ["git", "-C", str(cwd), "rev-parse", "--show-toplevel"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        return Path(out).resolve()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return cwd


def load_config(root: Path) -> dict[str, Any]:
    config = dict(DEFAULT_CONFIG)
    path = root / ".engineering-harness.json"
    legacy = root / ".codex" / "harness.json"
    if not path.exists() and legacy.exists():
        path = legacy
    if not path.exists():
        return config
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Invalid {path}: {exc}") from exc
    if not isinstance(loaded, dict):
        raise RuntimeError(f"Invalid {path}: expected a JSON object")
    config.update(loaded)
    return config


def _split_nul(data: bytes) -> list[str]:
    return [p.decode("utf-8", errors="surrogateescape") for p in data.split(b"\0") if p]


def dirty_paths(root: Path) -> set[str]:
    """Return tracked paths differing from HEAD plus untracked non-ignored files."""
    try:
        changed = _split_nul(run_git(root, "diff", "--name-only", "-z", "HEAD", "--"))
        untracked = _split_nul(
            run_git(root, "ls-files", "--others", "--exclude-standard", "-z", "--")
        )
        return set(changed) | set(untracked)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return set()


def file_state(root: Path, relative: str) -> str:
    path = root / relative
    try:
        if path.is_symlink():
            payload = ("symlink:" + os.readlink(path)).encode("utf-8", errors="surrogateescape")
        elif path.is_file():
            h = hashlib.sha256()
            h.update(f"mode:{path.stat().st_mode}:".encode())
            with path.open("rb") as f:
                for chunk in iter(lambda: f.read(1024 * 1024), b""):
                    h.update(chunk)
            return "file:" + h.hexdigest()
        elif path.exists():
            payload = ("other:" + str(path.stat().st_mode)).encode()
        else:
            return "missing"
        return "sha256:" + hashlib.sha256(payload).hexdigest()
    except OSError as exc:
        return f"error:{type(exc).__name__}:{exc}"


def workspace_snapshot(root: Path) -> dict[str, str]:
    return {path: file_state(root, path) for path in sorted(dirty_paths(root))}


def changed_since(baseline: dict[str, str], current: dict[str, str]) -> list[str]:
    paths = set(baseline) | set(current)
    return sorted(path for path in paths if baseline.get(path, "clean") != current.get(path, "clean"))


def state_path(root: Path, session_id: str) -> Path:
    root_key = hashlib.sha256(str(root).encode("utf-8")).hexdigest()[:16]
    safe_session = re.sub(r"[^A-Za-z0-9_.-]", "_", session_id or "unknown")[:160]
    base = Path(tempfile.gettempdir()) / "adaptive-engineering-harness" / root_key
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{safe_session}.json"


def load_baseline(root: Path, session_id: str) -> dict[str, str] | None:
    path = state_path(root, session_id)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        snapshot = data.get("snapshot") if isinstance(data, dict) else None
        if isinstance(snapshot, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in snapshot.items()):
            return snapshot
    except (OSError, json.JSONDecodeError):
        return None
    return None


def save_baseline(root: Path, session_id: str, snapshot: dict[str, str]) -> None:
    path = state_path(root, session_id)
    payload = {"root": str(root), "session_id": session_id, "snapshot": snapshot}
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def is_documentation_path(path_text: str) -> bool:
    path = Path(path_text)
    suffix = path.suffix.lower()
    if suffix in DOC_EXTENSIONS:
        return True
    stem_upper = path.name.split(".", 1)[0].upper()
    if stem_upper in DOC_BASENAMES:
        return True
    return False


def only_documentation_changes(paths: list[str]) -> bool:
    return bool(paths) and all(is_documentation_path(p) for p in paths)


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    head = max(0, limit // 2)
    tail = max(0, limit - head)
    return text[:head] + "\n... output truncated ...\n" + text[-tail:]

def retry_path(root: Path, session_id: str) -> Path:
    return state_path(root, session_id).with_suffix(".retry")


def load_retry_count(root: Path, session_id: str) -> int:
    path = retry_path(root, session_id)
    try:
        value = int(path.read_text(encoding="utf-8").strip())
        return max(0, min(value, 2))
    except (OSError, ValueError):
        return 0


def save_retry_count(root: Path, session_id: str, value: int) -> None:
    path = retry_path(root, session_id)
    path.write_text(str(max(0, min(int(value), 2))), encoding="utf-8")

