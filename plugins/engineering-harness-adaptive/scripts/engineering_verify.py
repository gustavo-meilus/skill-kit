#!/usr/bin/env python3
"""Run the repository's canonical verifier with conservative auto-discovery.

Exit codes:
  0  verifier found and passed
  3  no canonical verifier found
  other nonzero  verifier failed or could not run
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
from typing import Any


def repo_root() -> Path:
    try:
        value = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        return Path(value).resolve()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return Path.cwd().resolve()


def load_config(root: Path) -> dict[str, Any]:
    defaults = {
        "verify_command": None,
        "allow_test_only_fallback": False,
        "verification_timeout_seconds": 600,
    }
    path = root / ".engineering-harness.json"
    legacy = root / ".codex" / "harness.json"
    if not path.exists() and legacy.exists():
        path = legacy
    if not path.exists():
        return defaults
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Invalid {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)
    if not isinstance(data, dict):
        print(f"Invalid {path}: expected a JSON object", file=sys.stderr)
        raise SystemExit(2)
    defaults.update(data)
    return defaults


def package_manager(root: Path) -> str:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "bun.lock").exists() or (root / "bun.lockb").exists():
        return "bun"
    return "npm"


def package_script(root: Path, names: tuple[str, ...]) -> list[str] | None:
    package = root / "package.json"
    if not package.exists():
        return None
    try:
        data = json.loads(package.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    scripts = data.get("scripts", {}) if isinstance(data, dict) else {}
    if not isinstance(scripts, dict):
        return None
    for name in names:
        if name in scripts:
            pm = package_manager(root)
            return [pm, "run", name]
    return None


def make_target(root: Path, names: tuple[str, ...]) -> list[str] | None:
    makefile = next((p for p in (root / "Makefile", root / "makefile") if p.exists()), None)
    if not makefile:
        return None
    try:
        text = makefile.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    for name in names:
        if re.search(rf"(?m)^{re.escape(name)}\s*:(?:\s|$)", text):
            return ["make", name]
    return None


def just_target(root: Path, names: tuple[str, ...]) -> list[str] | None:
    path = next((p for p in (root / "justfile", root / "Justfile") if p.exists()), None)
    if not path or not shutil.which("just"):
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    for name in names:
        if re.search(rf"(?m)^{re.escape(name)}(?:\s[^:]*)?:\s*(?:#.*)?$", text):
            return ["just", name]
    return None


def script_candidate(root: Path) -> list[str] | None:
    candidates = [
        root / "scripts" / "check",
        root / "scripts" / "check.sh",
        root / "scripts" / "check.py",
        root / "scripts" / "check.cmd",
        root / "scripts" / "check.bat",
        root / "scripts" / "check.ps1",
        root / "scripts" / "verify",
        root / "scripts" / "verify.sh",
        root / "scripts" / "verify.py",
        root / "scripts" / "verify.cmd",
        root / "scripts" / "verify.bat",
        root / "scripts" / "verify.ps1",
    ]
    for path in candidates:
        if not path.is_file():
            continue
        rel = str(path.relative_to(root))
        suffix = path.suffix.lower()
        if suffix == ".py":
            return [sys.executable, rel]
        if suffix == ".sh":
            shell = shutil.which("bash") or shutil.which("sh")
            return [shell, rel] if shell else None
        if os.name == "nt" and suffix in {".cmd", ".bat"}:
            return [rel]
        if os.name == "nt" and suffix == ".ps1":
            shell = shutil.which("powershell") or shutil.which("pwsh")
            return [shell, "-NoProfile", "-File", rel] if shell else None
        if os.access(path, os.X_OK):
            return [str(path)]
        if os.name != "nt" and shutil.which("sh"):
            return ["sh", rel]
    return None


def test_only_fallback(root: Path) -> list[str] | None:
    cmd = package_script(root, ("test",))
    if cmd:
        return cmd
    if (root / "go.mod").exists() and shutil.which("go"):
        return ["go", "test", "./..."]
    if (root / "Cargo.toml").exists() and shutil.which("cargo"):
        return ["cargo", "test"]
    if (root / "gradlew").exists():
        return [str(root / "gradlew"), "test"]
    if (root / "mvnw").exists():
        return [str(root / "mvnw"), "test"]
    if any((root / name).exists() for name in ("pytest.ini", "tox.ini")):
        if (root / "uv.lock").exists() and shutil.which("uv"):
            return ["uv", "run", "pytest"]
        if shutil.which("pytest"):
            return ["pytest"]
    return None


def discover(root: Path, allow_test_only: bool) -> tuple[list[str] | str | None, bool]:
    # Return (command, use_shell). Prefer explicit canonical project surfaces.
    cmd = script_candidate(root)
    if cmd:
        return cmd, False
    cmd = make_target(root, ("check", "verify"))
    if cmd:
        return cmd, False
    cmd = just_target(root, ("check", "verify"))
    if cmd:
        return cmd, False
    cmd = package_script(root, ("check", "verify"))
    if cmd:
        return cmd, False
    if allow_test_only:
        cmd = test_only_fallback(root)
        if cmd:
            return cmd, False
    return None, False


def render(cmd: list[str] | str) -> str:
    if isinstance(cmd, str):
        return cmd
    return " ".join(shlex.quote(x) for x in cmd)


def main() -> int:
    root = repo_root()
    config = load_config(root)
    timeout = int(config.get("verification_timeout_seconds", 600))

    explicit = config.get("verify_command")
    if isinstance(explicit, str) and explicit.strip():
        cmd: list[str] | str = explicit.strip()
        use_shell = True
    else:
        cmd, use_shell = discover(root, bool(config.get("allow_test_only_fallback", False)))
        if cmd is None:
            print(
                "No canonical verifier found. Add scripts/check (preferred), a Make/just/package 'check' or 'verify' target, "
                "or set .engineering-harness.json -> verify_command. Test-only auto-detection is intentionally disabled by default.",
                file=sys.stderr,
            )
            return 3

    print(f"[engineering-harness] verifier: {render(cmd)}")
    try:
        completed = subprocess.run(
            cmd,
            cwd=root,
            shell=use_shell,
            timeout=timeout,
            check=False,
        )
        return int(completed.returncode)
    except subprocess.TimeoutExpired:
        print(f"[engineering-harness] verifier timed out after {timeout}s", file=sys.stderr)
        return 124
    except FileNotFoundError as exc:
        print(f"[engineering-harness] verifier could not start: {exc}", file=sys.stderr)
        return 127


if __name__ == "__main__":
    raise SystemExit(main())
