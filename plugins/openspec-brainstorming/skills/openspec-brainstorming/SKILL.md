---
name: openspec-brainstorming
description: Refine an OpenSpec exploration or rough project brief into one focused, explicitly approved change, then generate, strictly validate, and review the planning artifacts required for implementation. Use after openspec-explore or when the user wants to turn an uncertain or incomplete idea into a high-quality OpenSpec proposal without starting implementation; requires the OpenSpec CLI and an initialized project or registered store.
---

# OpenSpec Brainstorming

Use [references/workflow.md](references/workflow.md) as the authoritative workflow.

Remain in planning throughout. Do not write application code, scaffold implementation, or modify product files. Do not create an OpenSpec change until the user explicitly approves the normalized change contract.

Optimize for decision clarity, not prompt length. Ground material claims in repository, specification, test, and configuration evidence. Separate observed facts, user decisions, assumptions, and open questions. Describe requirements as observable behavior; leave implementation latitude to OpenSpec unless a technical choice is itself a hard requirement.

Let the selected OpenSpec schema, project configuration, and `openspec instructions` define artifact structure and artifact-specific rules. Do not duplicate or substitute your own proposal, spec, design, or task templates.

Right-size the process. Small, low-risk changes should stay small. Use deeper option analysis only when alternatives, risk, migration, security, data integrity, compatibility, or architecture can materially change the proposal.

**Complete when:** one cohesive OpenSpec change has all artifacts transitively required for apply, passes strict validation and a cross-artifact coherence review, and has been presented for user review. The next action is a separate user request to start the installed OpenSpec apply workflow, not implementation in this skill.
