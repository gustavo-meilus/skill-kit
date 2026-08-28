# Codex implementation notes

These notes record why this kit uses an AGENTS fragment + Skill + narrow hooks, with an optional reviewer agent rather than mandatory multi-agent orchestration.

## Current Codex primitives used

### AGENTS.md

Codex reads `AGENTS.md` before work and builds a project instruction chain from the Git root to the current working directory. Use it for the smallest always-on operating contract and router, not for the full playbook.

Official documentation:
https://developers.openai.com/codex/guides/agents-md

### Skills

Codex Skills use progressive disclosure: name and description are initially available; the full `SKILL.md` is loaded when the Skill is selected. Repository Skills can live under `$REPO_ROOT/.agents/skills`; installable plugins can bundle Skills under their plugin `skills/` directory.

Official documentation:
https://developers.openai.com/codex/skills

### Hooks

Codex hooks can run scripts or MCP tools at lifecycle events including `SessionStart`, `SubagentStart`, `PreToolUse`, `PostToolUse`, and `Stop`. Project and plugin hooks require trust review. This kit uses hooks only for policy persistence and a bounded completion check.

Official documentation:
https://developers.openai.com/codex/hooks

### Subagents

Codex supports built-in and custom subagents. Current docs recommend narrow, opinionated custom agents with tool surfaces matching their jobs. This kit therefore does not require a subagent. A read-only reviewer template is included only for cases where independent semantic judgment is materially useful.

Official documentation:
https://developers.openai.com/codex/subagents

### Plugins

OpenAI documentation recommends starting with a Skill while iterating and packaging a stable reusable capability as a plugin for team distribution. Codex can load plugin-bundled hooks in addition to Skills.

Official documentation:
https://developers.openai.com/codex/build-plugins

## Why the Stop hook is deliberately narrow

There is no project-agnostic deterministic test command. The hook therefore does not guess package-manager commands.

It runs an authoritative completion command only when:

1. the working tree has changes, and
2. one of these is available:
   - environment variable `MORE_WITH_LESS_CHECK`, or
   - executable `<repo>/scripts/check`.

If neither exists, the hook does not invent a verification command. It only warns Codex to report evidence honestly.

If the configured check fails, the hook forces at most one continuation. On a second failed Stop in the same turn, it allows the turn to end but warns that verification is still failing. This preserves bounded autonomy rather than creating an infinite self-correction loop.

## Why there is no default PreToolUse dependency blocker

The playbook says dependencies, agents, hooks, and tools must be justified, but justification is semantic. A generic shell parser cannot reliably determine whether `npm install`, `uv add`, `cargo add`, or another command is appropriate. Blocking them mechanically would turn a design principle into a brittle policy.

The Skill handles the semantic decision. The hook handles only deterministic lifecycle and completion behavior.

## Supporting engineering sources

OpenAI, Harness engineering:
https://openai.com/index/harness-engineering/

Martin Fowler / Thoughtworks, Harness engineering for coding agent users:
https://martinfowler.com/articles/harness-engineering.html

Martin Fowler / Thoughtworks, Maintainability sensors for coding agents:
https://martinfowler.com/articles/sensors-for-coding-agents.html

Anthropic, Building effective agents:
https://www.anthropic.com/engineering/building-effective-agents

Anthropic, Agent Skills and progressive disclosure:
https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
