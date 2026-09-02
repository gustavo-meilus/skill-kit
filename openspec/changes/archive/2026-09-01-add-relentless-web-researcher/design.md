## Context

Skill Kit packages recurring agent methods as independently installable plugins for Claude Code, Codex, and Copilot CLI. Existing instruction-only plugins use `plugins/<name>/plugin.json`, a skill directory with `SKILL.md` and optional Codex metadata, and entries in both marketplace manifests. See `proposal.md` and `specs/relentless-web-research/spec.md` for intent and behavior.

## Goals / Non-Goals

**Goals:**

- Make deep web research discoverable from the user's recurring “research and learn all about” language.
- Preserve a rigorous research loop, source hierarchy, evidence discipline, comparisons, and a checkable stopping condition in compact agent instructions.
- Fit existing Skill Kit packaging and host documentation without adding runtime machinery.

**Non-Goals:**

- Guarantee exhaustive knowledge, permanent training, or persistence across sessions.
- Introduce a crawler, source database, citation manager, hook, custom agent, or required external service.
- Force every result into one report template or impose arbitrary source counts.

## Decisions

### Use one instruction-only skill

The plugin will contain a focused `SKILL.md` plus `agents/openai.yaml`; no scripts or references are needed unless implementation shows the entrypoint cannot remain readable. The workflow is judgment-led and uses browsing and document capabilities already available in the host.

Alternative: add scripts, hooks, or specialist agents. Rejected because none provides a deterministic guarantee required by this behavior, and each would add packaging and host-parity costs.

### Make invocation automatic but discriminating

The skill description will trigger on explicit deep-research, expertise-building, literature/document review, and comparative technology research requests. It will exclude quick factual lookups and ordinary recommendations so its permanent context pointer does not capture routine browsing.

Alternative: explicit-only invocation. Rejected because the reusable natural-language prompt is intended to activate the method without requiring the user to remember a skill name.

### Encode a bounded relentless loop

The instructions will normalize the topic, map material questions, search through the source hierarchy, inspect the strongest sources, chase consequential gaps or conflicts, compare adjacent approaches, and synthesize. Completion requires material coverage plus diminishing decision value, with unresolved gaps disclosed.

Alternative: prescribe a fixed source count or search depth. Rejected because topic breadth, evidence density, and risk vary; fixed counts can stop too early or reward low-value collection.

### Prefer primary sources without treating them as infallible

Official documentation, standards, original research, and source documents lead factual claims. Independent reputable sources supply critique, operational experience, and competing interpretations. The synthesis distinguishes facts, source claims, and inference and cites them near the relevant statements.

Alternative: use only primary sources. Rejected because vendor or author sources may omit limitations and cannot independently validate disputed claims.

### Keep output adaptive

The skill will answer the user's practical goal directly and remain concise by default while allowing depth demanded by the subject or requested artifact. It will not mandate a fixed dossier whose empty sections add noise.

Alternative: always emit a comprehensive research report. Rejected because it conflicts with concise goal-directed use and makes simple topics unnecessarily expensive.

### Follow repository-native plugin packaging

Implementation will mirror existing Skill Kit plugins, append entries to `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`, and update README and host-count statements. Repository-native manifests take precedence over personal-plugin scaffold paths where the generic `plugin-creator` skill differs.

## Risks / Trade-offs

- [“Relentless” encourages endless browsing] → Use material-question coverage and diminishing decision value as explicit completion gates.
- [Primary sources can be self-serving or incomplete] → Require independent context and surface conflicts rather than treating authority as truth.
- [A broad trigger captures ordinary web lookups] → Name deep-research branches explicitly and include a quick-lookup exclusion.
- [Current findings become stale] → Require browsing and date or version context for time-sensitive claims.
- [Source access or evidence remains incomplete] → Exhaust reasonable alternatives, disclose the gap, and bound conclusions.
- [Dense instructions consume attention] → Keep one linear workflow and remove generic browsing advice already enforced by the host.
