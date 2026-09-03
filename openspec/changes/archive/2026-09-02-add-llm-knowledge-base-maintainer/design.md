## Context

Skill Kit distributes recurring agent methods as independently installable plugins. Existing instruction-led plugins package a focused `SKILL.md`, optional progressively disclosed references, Codex interface metadata, host manifests, and marketplace entries. See `proposal.md` and `specs/llm-knowledge-base-maintenance/spec.md` for the approved behavior.

## Goals / Non-Goals

**Goals:**

- Package one portable, model-invoked workflow for reference creation and ongoing maintenance.
- Keep canonical Markdown and both static indexes synchronized without requiring external infrastructure.
- Preserve existing collection conventions while providing a small default for new collections.
- Make integrity and evidence gaps visible before completion.

**Non-Goals:**

- Define or operate a retrieval runtime, vector store, crawler, documentation website, or hosted service.
- Introduce a universal documentation schema when a target collection already has equivalent conventions.
- Add a hook, custom agent, MCP server, or dependency for behavior that instructions and available project tools can provide.

## Decisions

### Package one instruction-led skill

The plugin will contain one `llm-knowledge-base-maintainer` skill and Codex interface metadata. Its entrypoint will classify create, maintain, and audit requests, run one shared inspection-to-validation workflow, and state its completion gate.

Detailed default page and index shapes will live in one disclosed reference loaded only when the target has no equivalent convention. This keeps common maintenance instructions visible without spending context on a default schema that many existing collections will not use.

Alternative: split creation, maintenance, and auditing into separate skills. Rejected because the modes share the same source, identity, synchronization, and validation invariants and would duplicate instructions and discovery surface.

### Start without bundled runtime automation

The skill will prefer existing repository generators, linters, and link checkers. When none exist, it will use the host's available deterministic file and shell capabilities for the current collection. The initial plugin will not ship a parser or index generator because portable Markdown metadata varies and no repository evidence establishes one universal input schema.

Alternative: bundle a configurable index generator and validator. Deferred until forward tests or real usage show repeated failures that a stable format-neutral script can prevent without imposing a second schema.

### Treat references as canonical and indexes as derived views

Canonical Markdown pages own the facts and stable document identity. `llms.txt` is a concise curated navigation view; `manifest.jsonl` is an exhaustive machine-readable inventory. After any authorized mutation, the skill will compare both views with the entire current collection so additions, metadata changes, renames, and removals cannot leave stale entries.

Alternative: make an index the source of truth. Rejected because it would either duplicate reference content or force human-readable authoring through an implementation-specific registry.

### Preserve logical identity across physical changes

Document identity will remain independent of filenames and headings. Renames and reorganizations preserve the stable ID while paths and index entries change. Provenance, applicable version, and update metadata remain close to the referenced facts so later maintenance can distinguish a content change from a relocation.

Alternative: derive identity only from the path. Rejected because path-based identities turn harmless reorganization into deletion and recreation and make stale-entry detection less reliable.

### Use automatic but narrow invocation

The skill description will name create and maintenance branches for LLM-ready reference collections and explicitly exclude general prose work, unrelated research, website work, and retrieval infrastructure. The user can still invoke the skill explicitly.

Alternative: explicit-only invocation. Rejected because natural-language requests to update or expand a knowledge base should discover the workflow without requiring the user to remember its name.

### Follow repository-native distribution

Implementation will mirror the existing plugin layout, append consistent entries to both marketplace manifests, and update README and host-count statements. Validation will use the repository's marketplace integrity test plus the skill and plugin validators; host installation remains unverified until separately exercised and recorded.

## Risks / Trade-offs

- [Different projects encode metadata differently] → Reuse equivalent local conventions and load the default-layout reference only when no usable convention exists.
- [Instruction-led index updates can miss stale entries] → Require a whole-collection comparison and deterministic checks before completion; add a script only if observed failures justify it.
- [Concise prose can omit necessary constraints] → Define concision as removal of duplication and narrative, while preserving defaults, limits, errors, versions, and provenance.
- [Source conflicts can produce false certainty] → Keep conflicts explicit and stop short of unsupported resolution.
- [Large collections make whole-corpus checks slower] → Accept the simple scan initially; introduce incremental machinery only after measured scale makes it necessary.
