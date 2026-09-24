# More With Less Completion Gate Specification

## Purpose

Select and run an explicitly recognized project check and report dirty-tree and verification outcomes through More With Less's Codex Stop hook.

## Requirements

### Requirement: Detect a dirty working tree from Git status
The Stop hook SHALL treat a working tree as dirty only when a successful Git status command reports tracked or untracked changes. Git diagnostics SHALL NOT count as file changes. The hook SHALL NOT claim that a dirty tree was changed by the current turn without evidence of that timing.

#### Scenario: Clean tree with a Git diagnostic
- **WHEN** Git status succeeds with no changed paths and emits a diagnostic
- **THEN** the hook emits no dirty-tree or missing-check warning

#### Scenario: Pre-existing untracked file
- **WHEN** Git status reports an untracked file that predates the current turn
- **THEN** the hook treats the tree as dirty without attributing the file to the turn

### Requirement: Select an authoritative project check
For a dirty Git working tree, the Stop hook SHALL select the first available check in this order: a non-empty `MORE_WITH_LESS_CHECK`, executable `<git-root>/scripts/check`, then `<git-root>/scripts/check.py`. The Python check SHALL run with the interpreter running the hook. Check discovery and execution SHALL use the Git root even when the session starts in a subdirectory.

#### Scenario: Explicit override takes precedence
- **WHEN** the override and both project scripts are available
- **THEN** the hook runs only the override

#### Scenario: Python project check is available
- **WHEN** no higher-priority check exists and `scripts/check.py` exists
- **THEN** the hook runs that file with its Python interpreter

#### Scenario: Session starts in a subdirectory
- **WHEN** the session `cwd` is below the Git root and a check is selected
- **THEN** the hook finds and runs the root-level check from the Git root

### Requirement: Report check outcomes honestly and without an unbounded loop
If no check is available for a dirty tree, the Stop hook SHALL issue an advisory warning and SHALL NOT claim verification ran. A passing check SHALL allow completion. A failing or timed-out check SHALL report its failure and request at most one automatic continuation for the turn.

#### Scenario: No check is available
- **WHEN** the tree is dirty and none of the recognized checks exists
- **THEN** the hook warns without blocking or claiming a completed check

#### Scenario: Check succeeds
- **WHEN** the selected check exits successfully
- **THEN** the hook permits completion without a verification warning

#### Scenario: Check fails twice
- **WHEN** the selected check fails on the initial Stop and again after the hook-triggered continuation
- **THEN** the hook requests no further continuation and reports the failure

#### Scenario: Check times out
- **WHEN** the selected check exceeds its configured execution timeout
- **THEN** the hook reports the timeout as a verification failure
