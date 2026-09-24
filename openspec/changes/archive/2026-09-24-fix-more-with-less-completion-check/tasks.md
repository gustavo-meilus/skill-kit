# Implementation Tasks

## 1. Completion check behavior

- [x] 1.1 Separate Git status stdout from diagnostics and correct the dirty-tree
  warning wording; verify focused tests cover clean status with stderr and a
  pre-existing untracked file.
- [x] 1.2 Add `scripts/check.py` after the existing override and executable
  check, launching it with the hook's Python interpreter from the Git root;
  verify tests cover precedence, subdirectory `cwd`, and paths with spaces.
- [x] 1.3 Preserve advisory missing-check output and bounded failure handling;
  verify focused tests cover no check, success, failure, repeat Stop, and timeout.

## 2. Plugin identity

- [x] 2.1 Rename the package directory and the root, Codex, and Claude
  manifest IDs to `more-with-less`; verify the skill and hook paths still
  resolve within the renamed package.
- [x] 2.2 Update both marketplace entries, install commands, and branding
  references, including manual transition guidance for existing `s-kit`
  installations; verify a repository search finds no stale current-ID usage.
- [x] 2.3 Extend the marketplace integrity test to compare entry IDs with
  host manifest names; verify a deliberate mismatch fails and the checked-in
  catalogs pass.

## 3. Integrated verification

- [x] 3.1 Run the focused hook and marketplace tests plus `scripts/check.py`;
  record the exact commands, results, and any environment-related failures.
- [x] 3.2 Inspect the active CLI hook source, version, and trust state without
  changing them; when a suitable Desktop session is available, check its
  Windows launcher and distinguish More With Less output from separate hook
  failures. `codex plugin list` does not show the old `s-kit` package, while
  user config retains its enabled flag and Stop trust hash; this is persisted
  state, not proof the package is currently loaded by CLI. CLI lists Decision
  Tracer 0.1.3 as enabled, and its cached 0.1.6 Stop handler only records
  lifecycle events. The Desktop cache contains `s-kit` 1.0.2 with the warning
  text. Its `py -3` launcher fails in this Windows environment (exit 101); the
  updated `python` launcher runs in PowerShell from a path with spaces. The
  Desktop hook browser is unavailable, so the installed cache's active trust
  and Codex-managed launch path remain unverified.
- [x] 3.3 Run strict OpenSpec validation for this change and review the final
  diff for only the intended hook, package, marketplace, documentation, test,
  and planning changes.
