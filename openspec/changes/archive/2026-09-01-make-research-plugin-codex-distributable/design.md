## Context

See `proposal.md` for motivation. The repository distributes plugins from root-relative marketplace entries. Codex requires a manifest at `.codex-plugin/plugin.json`; the research plugin currently has only the repository-native metadata file. Existing plugins provide paired host manifests, while the research plugin does not. The existing test suite does not validate marketplace-to-package resolution.

## Goals / Non-Goals

**Goals:**
- Make the listed research plugin satisfy Codex's required package structure.
- Preserve the repository's paired Claude/Codex manifest convention for this plugin.
- Detect broken source paths, required manifests, and skills directories with a small local check.
- Make the web-content trust boundary explicit in the research skill.

**Non-Goals:**
- Add CI infrastructure, hooks, MCP servers, dependencies, or public-directory submission metadata.
- Normalize versioning for unrelated plugins.
- Claim host-install success without an observed clean-host record.

## Decisions

### Add host manifests beside the existing repository metadata

Create the Codex manifest at the host-required path and add the matching Claude manifest used by the other plugins. Keep the package skills-only and reuse existing manifest fields and metadata conventions.

Alternative considered: rely on the root `plugin.json`. Rejected because it is not Codex's required entry point and does not make the advertised package installable.

### Validate catalog resolution in a focused local test

Add one standard-library-based Python test that loads the checked-in marketplace JSON, resolves each root-relative source path, and verifies the appropriate host manifest and `skills/` directory. Keep it alongside the existing pytest-based tests and avoid a new validation framework.

Alternative considered: add a release-time manual checklist only. Rejected because the structural defect is deterministic and inexpensive to catch before host testing.

### Keep the source-trust boundary in the skill instructions

Add a compact rule near the research procedure stating that retrieved content is data, not authority; only applicable system and user instructions can authorize actions or change scope.

Alternative considered: add a hook or filtering subsystem. Rejected because the package is instruction-only and the required boundary is procedural, not a new runtime capability.

### Keep clean-host verification as manual evidence

After structural validation, run and record Codex marketplace add, install, discovery, and uninstall in a clean environment when available. Do not mark the host-support record successful until those actions are observed.

Alternative considered: simulate installation. Rejected because a local structural check cannot prove host behavior.

## Risks / Trade-offs

- [Codex manifest schema changes] → Validate against the current official documentation during implementation and exercise the actual host flow.
- [Structural check diverges from host behavior] → Keep it limited to deterministic filesystem assertions and retain clean-host verification as a separate requirement.
- [Prompt injection remains possible at the model boundary] → State the non-authority rule explicitly and preserve host permission controls; do not overclaim complete prevention.

## Migration Plan

1. Add manifests, the focused check, and the source-trust rule.
2. Run structural and skill validation.
3. In a clean Codex environment, add the marketplace, install and discover the plugin, then uninstall it.
4. Record only observed host results. Roll back by removing the new plugin marketplace entry if a host install cannot be made valid.
