# Improve AI fingerprint audit

## Why

The AI Fingerprint Mitigator already gives Codex a careful,
provenance-preserving editing workflow and a dependency-free style audit.
The audit mostly reports aggregate signals without pointing to their
locations, and its ASCII-only word counter miscounts accented text.
Improve those gaps while keeping the tool fast, local, and focused on
writing quality.

## What Changes

- Add a line number and short excerpt to existing stock-phrase hits while
  retaining current JSON fields and aggregate signals.
- Count Unicode text correctly without adding dependencies; keep existing
  phrase rules scoped to English.
- Clarify revision checks for omitted or unsupported claims and changes to
  negation, certainty, numbers, citations, and other protected content.
- Add focused regression coverage for located phrase hits and Unicode
  handling.
- Keep auditing separate from editing. Do not add automatic rewrites,
  detector scoring, external services, model downloads, or dependencies.

## Capabilities

### New Capabilities

- `ai-fingerprint-mitigation`: Lightweight, location-aware style
  auditing and meaning-preserving prose revision within Codex.

### Modified Capabilities

## Impact

- `plugins/ai-fingerprint-mitigator/skills/ai-fingerprint-mitigator/scripts/prose_audit.py`
- `plugins/ai-fingerprint-mitigator/skills/ai-fingerprint-mitigator/SKILL.md`
  and its revision protocol reference
- Focused tests for the audit script
- No external APIs, services, runtime dependencies, or detector integrations
