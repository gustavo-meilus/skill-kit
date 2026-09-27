# Tasks

## 1. Improve local audit findings

- [x] 1.1 Add one-based line locations and bounded excerpts to existing
  stock-phrase hit strings; verify a focused test preserves current JSON keys
  and leaves document-level patterns aggregate.
- [x] 1.2 Make word counting Unicode-aware and disclose that phrase checks are
  English-specific; verify a focused test with accented text and the scope
  note.

## 2. Preserve revision quality

- [x] 2.1 Clarify checks for omitted or unsupported claims, negation, and
  modality, and document the audit's located-hit behavior; verify alignment
  with the authorship and provenance boundaries.

## 3. Verify the change

- [x] 3.1 Run the focused audit tests, then `python scripts/check.py`; verify
  both commands exit successfully without new dependencies.
