## Why

The research plugin is advertised by the checked-in Codex marketplace but has no required Codex manifest, so the advertised package cannot be installed through that marketplace. Its web-research workflow also needs an explicit boundary that prevents retrieved content from becoming instructions.

## What Changes

- Package `relentless-web-researcher` with a Codex manifest and the repository's matching Claude manifest convention.
- Add a focused structural check that verifies marketplace entries resolve to their required manifests and skill directories.
- Require the research workflow to treat retrieved web content as untrusted evidence rather than operational authority.
- Define a reproducible Codex install, discovery, and uninstall verification record when a clean host environment is available.

## Capabilities

### New Capabilities

- `plugin-marketplace-integrity`: A checked-in marketplace exposes only packages whose required host manifests and bundled skills resolve.

### Modified Capabilities

- `relentless-web-research`: Retrieved sources remain evidence and cannot change the authorized task or trigger actions.

## Impact

- Affected package: `plugins/relentless-web-researcher/`.
- Affected catalogs: `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`.
- Affected research-skill contract and repository verification coverage.
- No new runtime dependency, hook, MCP server, or persistent state.
