# Skill Kit

> Small, useful skills for Claude Code, Codex, and Copilot CLI.

Skills live in installable plugins. The first is **More With Less Engineering**: a minimum-sufficient engineering playbook with a shared skill and an optional Codex-only completion hook.

## Install

| CLI | Add marketplace | Install the skill |
| --- | --- | --- |
| Claude Code | `claude plugin marketplace add gustavo-meilus/skill-kit` | `claude plugin install s-kit@skill-kit` |
| Codex | `codex plugin marketplace add gustavo-meilus/skill-kit` | `codex plugin add s-kit@skill-kit` |
| Copilot CLI | `copilot plugin marketplace add gustavo-meilus/skill-kit` | `copilot plugin install s-kit@skill-kit` |

For local development, clone the repo and use `.` in place of `gustavo-meilus/skill-kit`. To refresh a Git marketplace, use `claude plugin marketplace update skill-kit`, `codex plugin marketplace upgrade skill-kit`, or `copilot plugin marketplace update skill-kit`, then update the plugin if prompted.

## Included

| Skill | What it does |
| --- | --- |
| `more-with-less-engineering` | Helps project work stay minimal without weakening correctness, security, or verification. |
| `cutting-a-release` | Guides evidence-based Git releases from preparation through verification. |
| `openspec-brainstorming` | Converts a rough idea into an approved, validated OpenSpec proposal. |
| `engineering-harness-adaptive` | Full adaptive workflow: a shared skill, deterministic completion gate, and read-only roles. |

The skill is available as `$more-with-less` in Codex and `/s-kit:more-with-less` in Claude Code. Copilot discovers it from the installed plugin.

`engineering-harness-adaptive` is available as `$engineering-discipline` in Codex and `/engineering-harness-adaptive:engineering-discipline` in Claude Code. Claude Code and Copilot CLI load its roles and completion gate directly. Codex loads its skill and trusted hook; the equivalent Codex role profiles are bundled under `profiles/codex` for manual opt-in because plugins do not load custom agent profiles. The hook requires Python 3 and uses the project's normal verification command; copy its template only to override detection.

## Add a skill

Add each reusable capability as `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`, then list its plugin in both marketplace manifests. Keep skills focused and add supporting files only when they are actually used.
