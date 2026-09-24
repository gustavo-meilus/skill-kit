# Fix More With Less Completion Check

## Why

The More With Less Stop hook warns that no completion check is configured in
this repository even though `scripts/check.py` is its documented project
check. Its dirty-tree probe can also mistake Git diagnostics for file changes.
The plugin ID `s-kit` obscures the purpose expressed by the other descriptive
plugin names.

## What Changes

- Recognize `scripts/check.py` after `MORE_WITH_LESS_CHECK` and executable
  `scripts/check`, and run it with the current Python interpreter.
- Base dirty-tree detection on Git status output, excluding Git diagnostics.
  Describe a dirty tree without attributing changes to the current turn. Keep
  the missing-check result advisory and the failed-check continuation bounded.
- **BREAKING:** Rename the plugin ID and directory from `s-kit` to
  `more-with-less` across package manifests, marketplaces, install guidance,
  and branding references. Existing `s-kit` installations are not migrated.
- Add regression coverage for check selection, Windows paths and launch
  behavior, hook output, and marketplace-to-manifest name consistency.

## Capabilities

### New Capabilities

- `more-with-less-completion-gate`: Select and run a recognized project check,
  and report dirty-tree and verification outcomes through the Codex Stop hook.

### Modified Capabilities

- `plugin-marketplace-integrity`: Require each checked-in marketplace entry
  to match its package identity as well as resolve its package structure.

## Impact

- More With Less hook, tests, plugin directory, and host manifests.
- Codex and Claude marketplaces, install instructions, and branding.
- No new runtime dependency, user-level setting, trust change, or automatic
  plugin installation or removal.
