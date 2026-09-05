<p align="center">
  <img src="assets/skill-kit-mark.svg" width="96" alt="Skill Kit mark">
</p>

# Skill Kit

> **Better defaults for coding agents.**

Install reusable engineering, planning, release, and writing methods into Claude Code, Codex, and Copilot CLI. Use a lightweight skill when instructions are enough; use hooks, verification gates, or specialist roles when stronger controls are warranted.

**[Pick a skill](#pick-a-skill) · [Install](#install) · [How it works](#how-skill-kit-works) · [Host details](docs/HOSTS.md)**

## Stop re-teaching your agent how to work

Coding agents can edit files and run commands. The recurring problem is the working method around that work: how much architecture is enough, when planning is worth it, what evidence counts as done, and when a deterministic check should replace judgment.

Skill Kit packages those methods so they can be reused without replacing your agent host with another framework.

```text
Task: add the requested behavior

Generic path                 More With Less
new abstraction              inspect the requirement
new helper                   reuse the existing mechanism
speculative extension points smallest coherent change
broad cleanup                required verification
                             stop
```

## Pick a skill

### BUILD

| Skill | Use it for | Included controls |
| --- | --- | --- |
| [More With Less](plugins/s-kit/skills/more-with-less/SKILL.md) | Minimum-sufficient engineering without weakening correctness or verification. | Skill; optional Codex completion hook |
| [Adaptive Engineering Harness](plugins/engineering-harness-adaptive/skills/engineering-discipline/SKILL.md) | Risk-scaled engineering work that benefits from deterministic verification or isolated review. | Skill, hook, and host-specific roles |
| [Relentless Web Researcher](plugins/relentless-web-researcher/skills/relentless-web-researcher/SKILL.md) | Deep, current research on a topic or tool with evidence and practical comparisons. | Instruction-only skill |
| [LLM Knowledge Base Maintainer](plugins/llm-knowledge-base-maintainer/skills/llm-knowledge-base-maintainer/SKILL.md) | Grounded Markdown knowledge bases with safe source workflows and synchronized `llms.txt` and manifest indexes. | Instruction-only skill |

### SHIP

| Skill | Use it for | Included controls |
| --- | --- | --- |
| [OpenSpec Brainstorming](plugins/openspec-brainstorming/skills/openspec-brainstorming/SKILL.md) | Turning a rough idea into an approved, validated OpenSpec change. | Skill and workflow references |
| [Cutting a Release](plugins/cutting-a-release/skills/cutting-a-release/SKILL.md) | Preparing, publishing, verifying, or recovering a Git release. | Procedural skill and release adapters |

### WRITE

| Skill | Use it for | Included controls |
| --- | --- | --- |
| [Lite Writing](plugins/lite-writing/skills/lite-writing/SKILL.md) | Concise technical and professional prose without lost meaning. | Skill and editing references |
| [AI Fingerprint Mitigator](plugins/ai-fingerprint-mitigator/skills/ai-fingerprint-mitigator/SKILL.md) | Removing formulaic AI-style prose patterns while preserving facts, provenance, and voice. | Skill and prose audit script |

AI Fingerprint Mitigator is a style editor, not an AI-detector-evasion tool.

## Install

Add the marketplace once, then install the skill that matches the job.

| CLI | Add marketplace | Install a plugin |
| --- | --- | --- |
| Claude Code | `claude plugin marketplace add gustavo-meilus/skill-kit` | `claude plugin install s-kit@skill-kit` |
| Codex | `codex plugin marketplace add gustavo-meilus/skill-kit` | `codex plugin add s-kit@skill-kit` |
| Copilot CLI | `copilot plugin marketplace add gustavo-meilus/skill-kit` | `copilot plugin install s-kit@skill-kit` |

For local development, clone this repository and use `.` in place of `gustavo-meilus/skill-kit`. To refresh a Git marketplace, use `claude plugin marketplace update skill-kit`, `codex plugin marketplace upgrade skill-kit`, or `copilot plugin marketplace update skill-kit`, then update the plugin if prompted.

The installed entry points are host-specific. Codex uses `$more-with-less`, `$lite-writing`, `$ai-fingerprint-mitigator`, `$relentless-web-researcher`, `$llm-knowledge-base-maintainer`, and `$engineering-discipline`; Claude Code uses namespaced slash commands; Copilot discovers skills from the installed plugin. See [HOSTS.md](docs/HOSTS.md) for exact packaged behavior and current verification status.

## How Skill Kit works

```text
Skill   reusable operating method
Plugin  distributable package
Hook    deterministic lifecycle behavior when needed
Agent   isolated specialist context when needed
Script  deterministic mechanism where model judgment is unnecessary
```

The collection is deliberately mixed: some jobs only need a compact method; others benefit from stronger, host-native controls. Read the [philosophy](docs/PHILOSOPHY.md) and [verification policy](docs/VERIFICATION.md) for the boundaries.

## Proof, not promises

The repository currently ships eight separately installable plugins through its Claude Code and Codex marketplace manifests. The Adaptive Engineering Harness includes executable hook files and host-specific role definitions. These are structural facts, not claims that installation makes an agent universally faster or more correct.

Before a public launch, maintainers should record clean-install results for each host and version. The [host matrix](docs/HOSTS.md) distinguishes packaged support from that launch proof.

## Trust and boundaries

Skill Kit can provide reusable procedures, host-native plugin surfaces, and included hooks or scripts. It cannot guarantee model correctness, make every host enforce identical boundaries, replace repository-specific requirements, or make text undetectable as AI-generated.

Read [contributing](CONTRIBUTING.md), [security](SECURITY.md), [support](SUPPORT.md), [plugin authoring](docs/PLUGIN-AUTHORING.md), and [branding](docs/BRANDING.md). License and public-release gates remain maintainer decisions.
