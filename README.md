# Skill Kit

> Small, useful skills for Claude Code, Codex, and Copilot CLI.

Skills live in installable plugins. The first is **More With Less Engineering**: a minimum-sufficient engineering playbook with a shared skill and an optional Codex-only completion hook.

## Install

| CLI | Add marketplace | Install the skill |
| --- | --- | --- |
| Claude Code | `claude plugin marketplace add gustavo-meilus/skill-kit` | `claude plugin install more-with-less-engineering@skill-kit` |
| Codex | `codex plugin marketplace add gustavo-meilus/skill-kit` | `codex plugin add more-with-less-engineering@skill-kit` |
| Copilot CLI | `copilot plugin marketplace add gustavo-meilus/skill-kit` | `copilot plugin install more-with-less-engineering@skill-kit` |

For local development, clone the repo and use `.` in place of `gustavo-meilus/skill-kit`. To refresh a Git marketplace, use `claude plugin marketplace update skill-kit`, `codex plugin marketplace upgrade skill-kit`, or `copilot plugin marketplace update skill-kit`, then update the plugin if prompted.

## Included

| Plugin | What it does |
| --- | --- |
| `more-with-less-engineering` | Helps project work stay minimal without weakening correctness, security, or verification. |
| `cutting-a-release` | Guides evidence-based Git releases from preparation through verification. |
| `openspec-brainstorming` | Converts a rough idea into an approved, validated OpenSpec proposal. |

The skill is available as `$more-with-less` in Codex and `/more-with-less-engineering:more-with-less` in Claude Code. Copilot discovers it from the installed plugin.

## Add a skill

Add each reusable capability as `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`, then list its plugin in both marketplace manifests. Keep skills focused and add supporting files only when they are actually used.
