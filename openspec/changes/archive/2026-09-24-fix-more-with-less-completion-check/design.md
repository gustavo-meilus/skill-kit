# Completion Check and Plugin Identity Design

## Context

See [proposal.md](proposal.md). The Stop hook discovers a Git root from the
event `cwd`, checks porcelain status, then selects an environment override or
an extensionless `scripts/check`. This repository instead supplies
`scripts/check.py`. The hook currently combines Git stdout and stderr, and its
warning implies a change happened during the turn without tracking a baseline.
The plugin is listed as `s-kit` in two marketplaces and three manifests.

## Goals / Non-Goals

**Goals:** Keep check selection deterministic, preserve the advisory result
when no check exists, and make Git diagnostics unable to trigger the gate.
Keep the rename consistent across package identities and published guidance.

**Non-goals:** Infer package-manager commands, track per-turn file baselines,
alter hook trust, or migrate installed copies automatically.

## Decisions

### Recognize the existing Python check

Keep the override first and extensionless executable second. Add
`scripts/check.py` as a third recognized candidate, launched as an argument
list with `sys.executable`. This uses the repository's existing verifier and
avoids a platform-specific wrapper. The alternative is requiring each user
to set `MORE_WITH_LESS_CHECK`; that leaves this package's own documented
check undiscovered and adds external configuration.

Keep the override's existing shell behavior for compatibility. On Windows,
Python uses the system command shell for `shell=True`, so examples and tests
must use that shell's syntax. Preserve the current 280-second command timeout
within the 300-second Stop hook timeout.

### Distinguish Git status from diagnostics

Read porcelain stdout separately from stderr and base dirty-tree detection
only on successful status stdout. Continue to gate any dirty tree, including
pre-existing changes; change the advisory wording to say the tree *has*
changes. A session baseline would add state and a different scope of gating,
so it is excluded from this change.

### Rename the distributed package identity

Move `plugins/s-kit` to `plugins/more-with-less` and set `more-with-less` in
the root, Codex, and Claude manifests and both marketplace entries. Update
installation examples and branding references, including the statement that
`S-Kit` names the old plugin. Keep the skill ID `$more-with-less` and relative
hook paths. Extend the existing marketplace integrity check to compare each
entry ID with its host manifest name. Do not retain a second `s-kit` package:
that would create two install identities for one capability.

## Risks / Trade-offs

- A repository may contain `scripts/check.py` without intending it as a full
  completion check. Mitigation: document the recognized convention and retain
  explicit override precedence; test the checked-in script's actual behavior.
- Existing `s-kit` installations will not follow the new ID automatically.
  Mitigation: document the new install name and the manual transition; do not
  change installed or user-level files as part of this repository change.
- A Windows host may launch `commandWindows` differently than assumed.
  Mitigation: verify the manifest command in a fresh CLI and Desktop runtime;
  adjust the launcher only if that evidence shows a failure.

## Migration Plan

Publish the repository package and marketplace rename together, then update
install guidance. Existing users can install `more-with-less` and remove the
old `s-kit` installation when ready. A rollback restores the old directory,
IDs, and marketplace references as one change. No automatic uninstall or
trust update is part of deployment.
