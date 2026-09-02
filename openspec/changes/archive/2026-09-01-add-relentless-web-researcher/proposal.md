## Why

Users repeatedly restate the same deep-research prompt to make a session build current, evidence-backed expertise on a topic and selected subtopics. Skill Kit should package that recurring method with explicit source quality, comparison, citation, uncertainty, and completion rules.

## What Changes

- Add a `relentless-web-researcher` plugin whose skill accepts a main topic, optional subtopics, and an optional practical goal.
- Require iterative web and document research led by current primary sources, with reputable secondary sources used for context and competing interpretations.
- Require cited synthesis that separates sourced facts from inference, reconciles conflicts, exposes material gaps, and compares adjacent tools or technologies.
- Bound "relentless" research by material coverage and diminishing returns rather than unlimited browsing.
- Package the plugin for supported marketplaces and document its user-facing entry point.

## Capabilities

### New Capabilities

- `relentless-web-research`: Deep, current, goal-directed topic research and comparative specialist synthesis with evidence provenance and bounded completion.

### Modified Capabilities

None.

## Impact

- Adds a plugin under `plugins/relentless-web-researcher/` with skill and Codex interface metadata.
- Updates both marketplace manifests plus the README and host-support documentation.
- Adds no hooks, scripts, specialist agents, persistent knowledge store, runtime dependencies, or claims of permanent model training.
