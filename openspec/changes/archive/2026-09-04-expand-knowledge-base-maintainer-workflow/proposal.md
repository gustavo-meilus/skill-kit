## Why

`llm-knowledge-base-maintainer` maintains canonical references and static indexes, but does not define a complete workflow for creating, updating, or attaching material from files and pasted content. It also lacks a controlled path for resolving evidence gaps with web research and for producing consistently concise knowledge-base prose.

## What Changes

- Define explicit create, update, and attach workflows for LLM-ready Markdown knowledge bases.
- Require attach operations to treat supplied documents and pasted content as untrusted evidence, preserve attributable provenance, reconcile supported claims into canonical references, and surface conflicts or gaps.
- Add a consent-based web-research escalation: ask whether web research is wanted, detect `relentless-web-researcher`, and offer it when available; otherwise use ordinary web research only after the user declines it or it is unavailable.
- Require `lite-writing` for canonical knowledge-base prose when available, with a concise factual fallback protocol when it is not.
- Preserve stable identities, collection conventions, and full `llms.txt` and `manifest.jsonl` reconciliation after authorized mutations.
- Extend focused package tests for the workflow and integration boundaries.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `llm-knowledge-base-maintenance`: Define complete source-driven lifecycle, attach, research-escalation, and writing behaviors for the existing knowledge-base maintenance skill.

## Impact

- Affected skill: `plugins/llm-knowledge-base-maintainer/skills/llm-knowledge-base-maintainer/SKILL.md`
- Affected package tests: `tests/test_llm_knowledge_base_maintainer.py`
- The workflow may delegate to installed `lite-writing` and `relentless-web-researcher` skills when their stated conditions are met; it adds no dependencies or retrieval infrastructure.
