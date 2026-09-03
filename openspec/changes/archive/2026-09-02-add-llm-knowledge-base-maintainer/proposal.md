## Why

Creating and maintaining an LLM-readable reference collection currently requires repeated decisions about document structure, provenance, stable identity, and index synchronization. Skill Kit should package that recurring workflow so reference content and its portable indexes remain concise, consistent, and reviewable as the collection changes.

## What Changes

- Add an `llm-knowledge-base-maintainer` plugin whose skill creates, revises, expands, reorganizes, and audits Markdown reference collections.
- Require each managed collection to preserve canonical reference content, stable document identity, relevant provenance and version information, and useful cross-links.
- Maintain a curated `llms.txt` and an exhaustive `manifest.jsonl` in agreement with the reference collection.
- Detect duplicate identities, broken links, stale index entries, conflicting source claims, and insufficient evidence instead of silently publishing inconsistent or invented content.
- Reuse an existing collection's equivalent conventions and otherwise establish a minimal documented layout.
- Package the skill for the supported marketplaces and document its user-facing entry point.

## Capabilities

### New Capabilities

- `llm-knowledge-base-maintenance`: Create and maintain concise Markdown reference collections with synchronized portable LLM indexes and evidence-preserving validation.

### Modified Capabilities

None.

## Impact

- Adds an independently installable plugin under `plugins/llm-knowledge-base-maintainer/` with skill and Codex interface metadata.
- Updates both marketplace manifests plus README and host-support documentation.
- Adds focused structural and behavioral verification for creation, revision, expansion, authorized removal, conflict handling, and invocation boundaries.
- Adds no vector database, embeddings, hosted retrieval service, crawler, website generator, MCP server, hook, custom agent, runtime dependency, or default `llms-full.txt` output.
