## 1. Skill Package

- [x] 1.1 Create the repository-native `relentless-web-researcher` plugin manifest, focused `SKILL.md`, and Codex `agents/openai.yaml`; verify the manifest parses and `skill-creator`'s `quick_validate.py` passes.
- [x] 1.2 Review the skill against `skill-creator`, `writing-for-agents`, `plugin-creator`, More With Less, and the approved research specification; verify every requirement is represented once without adding hooks, scripts, agents, dependencies, or unsupported persistence claims.

## 2. Distribution

- [x] 2.1 Append consistent `relentless-web-researcher` entries to the Claude and Codex marketplace manifests; verify both JSON files parse and resolve to the new plugin path.
- [x] 2.2 Add the skill to README discovery/install guidance and update host-support package counts where applicable; verify names, descriptions, and supported-host claims agree with the manifests.

## 3. Verification

- [x] 3.1 Run the smallest repository-native structural checks, including skill validation and parsing all changed JSON/YAML metadata; verify every command exits successfully.
- [x] 3.2 Use a fresh independent Verifier to forward-test realistic full, topic-only, conflicting-evidence, comparison, and quick-lookup boundary prompts; verify it returns PASS for invocation, research rigor, citations, uncertainty, bounded completion, and packaging, or complete one bounded rework cycle.
