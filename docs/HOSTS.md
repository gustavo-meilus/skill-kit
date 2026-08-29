# Host support

Skill Kit is packaged for Claude Code, Codex, and Copilot CLI. This table describes the checked-in package structure; a clean-install matrix is still required before making a launch claim for a specific host version.

| Capability | Claude Code | Codex | Copilot CLI |
| --- | --- | --- | --- |
| Marketplace manifest | `.claude-plugin/marketplace.json` | `.agents/plugins/marketplace.json` | Uses the plugin package layout |
| Skills | Bundled in every plugin | Bundled in every plugin | Bundled in every plugin |
| Adaptive Harness hook | `hooks/claude-hooks.json` | Bundled trusted hook | `hooks/copilot-hooks.json` |
| Adaptive Harness roles | Bundled Claude role files | Manual opt-in profiles in `profiles/codex` | Bundled Copilot agent files |
| More With Less hook | Not packaged as a Claude lifecycle hook | Optional Codex completion hook | No hook packaged |

## Important differences

- Claude Code and Copilot CLI package Adaptive Harness roles and lifecycle hooks directly.
- Codex packages its skill and hook. Its role profiles are deliberately manual opt-in because the plugin does not load custom agent profiles.
- Host behavior can change. Record the host version, exact commands, plugin discovery, relevant hook behavior, and uninstall result before marking a row launch-verified.

## Launch verification record

| Host | Version | Marketplace add | Install/discover | Hook behavior | Uninstall | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Code | — | Not yet recorded | Not yet recorded | Not yet recorded | Not yet recorded | Pending |
| Codex | — | Not yet recorded | Not yet recorded | Not yet recorded | Not yet recorded | Pending |
| Copilot CLI | — | Not yet recorded | Not yet recorded | Not yet recorded | Not yet recorded | Pending |
