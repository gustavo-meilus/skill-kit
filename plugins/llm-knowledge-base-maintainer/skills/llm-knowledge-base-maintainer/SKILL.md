---
name: llm-knowledge-base-maintainer
description: Create or maintain LLM-ready Markdown reference collections with stable identities, grounded claims, and synchronized llms.txt and manifest.jsonl indexes. Use for knowledge-base creation, revision, expansion, reorganization, auditing, or authorized removal. Do not use for ordinary prose, standalone research, websites, embeddings, vector databases, or hosted retrieval infrastructure.
---

# LLM Knowledge Base Maintainer

Maintain canonical Markdown references and their two derived indexes. Inspect an existing target before changing it. Ask only when the target or authoritative source material cannot be established safely.

## Work

1. Determine the requested operation and its authorized scope. Use supplied or authorized sources; leave unsupported claims unresolved and surface material source conflicts.
2. Inspect all in-scope references, `llms.txt`, and `manifest.jsonl`. Reuse an equivalent existing layout, metadata, naming, and index convention. If none exists, read [DEFAULT_LAYOUT.md](references/DEFAULT_LAYOUT.md).
3. Change only the requested canonical references. Keep each logical topic's stable ID across wording, filename, heading, and organization changes. Record title, summary, applicable version, update information, and provenance with the facts they support. Add resolvable relative links when they materially help navigation.
4. Regenerate or revise `llms.txt` as a concise navigation map and `manifest.jsonl` as one exhaustive current entry per canonical reference. Reconcile both against the entire collection after every authorized mutation; remove stale entries only with authorized reference removal.
5. Before completion, validate required metadata, duplicate IDs, internal links, referenced files, manifest completeness and duplicates, and agreement of both indexes with canonical references. Repair authorized in-scope defects; otherwise report them and do not claim synchronization.

Use existing project generators, linters, and link checkers when available. Do not add retrieval infrastructure or automation unless a repeated, demonstrated failure requires it.

## Completion

Report the changed scope, source or evidence gaps, and checks run. A conflict, unsupported claim, or unrepaired integrity defect is a visible incomplete result, not a fact to invent or a clean completion.
