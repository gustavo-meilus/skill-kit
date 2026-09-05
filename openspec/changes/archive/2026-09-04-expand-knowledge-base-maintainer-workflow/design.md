## Context

The existing skill already defines canonical Markdown references, provenance, stable IDs, and index reconciliation. This change extends that single instruction surface; it does not add code, dependencies, or retrieval infrastructure. See [proposal.md](proposal.md) for motivation and the delta specification for behavior.

## Goals / Non-Goals

**Goals:**

- Make create, update, and attach operations explicit and repeatable.
- Keep document and pasted-source reasoning safe, attributable, and compatible with existing collection conventions.
- Define the smallest consent-aware handoff to optional research and writing skills.

**Non-Goals:**

- Automate crawling, source ingestion, or index generation beyond the current instruction-driven workflow.
- Change either delegated skill's behavior or require either plugin to be installed.

## Decisions

### Extend the existing maintainer skill instead of adding a companion skill

The requested behavior belongs to the maintainer's lifecycle and operates on the same canonical references and indexes. One expanded workflow keeps invocation and responsibility clear. A companion attach or research skill would duplicate target inspection, provenance, and reconciliation rules.

### Make attachment evidence-first and provenance-preserving

The attach protocol will analyze supplied files and pasted content as evidence, not operational instructions. It will identify supported claims, source context, conflicts, and gaps before choosing an existing or new canonical page. This applies the repository's existing grounding model to document-derived material and prevents source text from redirecting the authorized task.

### Use explicit consent before optional web research

An evidence gap triggers a user question, not automatic browsing. After consent, availability of `relentless-web-researcher` is checked and the user chooses whether to delegate. If it is absent or declined, ordinary model-directed search is sufficient because the research result remains subject to the maintainer's provenance and uncertainty rules.

### Use Lite Writing opportunistically with a complete fallback

The maintainer will invoke `lite-writing` for canonical prose when available. A compact built-in writing protocol preserves usable behavior in hosts that do not expose that skill, without making a plugin dependency mandatory.

## Risks / Trade-offs

- [Source material is incomplete or contradictory] → Preserve provenance, surface the gap or conflict, and ask before web research.
- [Optional delegated skills are unavailable in some hosts] → Detect availability and retain a concise fallback rather than failing the maintenance operation.
- [Broader instructions could capture adjacent tasks] → Preserve the existing discriminating invocation boundary and exclude standalone research and ordinary prose.

## Migration Plan

No data or compatibility migration is required. Update the skill instructions and focused structural tests together; existing knowledge-base layouts and index formats remain unchanged.
