---
name: cutting-a-release
description: Release work for any Git repository. Use to prepare or publish a release, create a release tag, verify an existing release, or recover a partial or failed release; read RUNBOOK.md before acting.
---

# Release a Git Project

Read [RUNBOOK.md](RUNBOOK.md) before changing files, creating tags, or publishing. It contains the common release sequence.

Load [RELEASE-ADAPTERS.md](RELEASE-ADAPTERS.md) only for branches detected during discovery, such as tag-only or generated versioning, monorepos, hosted forges, registries, binary assets, signing, or a plain Git remote.

Repository-local instructions and automation are authoritative unless they conflict with safety or the user's explicit request.

## Release contract

- **Evidence over convention.** Discover the repository's branch, remote, version, tag, validation, integration, and publication policy from repository evidence.
- **Preserve work.** Use a clean worktree or an understood working tree; keep unrelated local changes recoverable and outside the release diff.
- **Native path first.** Prefer committed release scripts, CI, generators, and package tooling over hand-edited substitutes.
- **Pin the release.** Record one exact release identifier, tag, and target commit; re-pin after integration and publish that commit explicitly.
- **Gate irreversible actions.** Required checks must pass, and any protection bypass, force operation, public tag repair, or skipped required control needs explicit approval immediately before it occurs.
- **Treat publication as public.** Once a tag or package is public, fix forward by default rather than rewriting it.
- **Report evidence.** Distinguish passed, failed, skipped, pending, and not-applicable checks; never describe an unobserved result as successful.

## Common sequence

1. **Profile** — discover the release policy and fill every consequential field in the release ledger.
   - Done when the repository, release branch, target, identifier, version sources, checks, integration path, publication path, and required approvals are known.
2. **Pin** — resolve the exact target commit and prove the intended version/tag is unused.
   - Done when the identifier, tag, previous release boundary, and commit are unambiguous and recorded.
3. **Prepare** — apply the smallest project-native version and release-note changes.
   - Done when the diff contains only intended release changes and every generated change has a known source.
4. **Prove** — run the repository-required validation and classify every required check.
   - Done when all publication gates are passed or an allowed exception has explicit approval and is recorded.
5. **Integrate** — land release changes through the repository's actual branch and review policy.
   - Done when the release commit is on the integration branch and the target commit has been re-pinned.
6. **Publish** — create the conventional tag on the pinned commit and let the native release mechanism publish.
   - Done when the intended public tag exists and each synchronous publication target reports success; asynchronous targets are identified as pending.
7. **Verify** — compare remote evidence with the release ledger and report the result.
   - Done when the remote tag resolves to the pinned commit and every applicable release, package, asset, signature, or CI result is verified or explicitly pending.

## Stop gates

Stop before publication when any of these remains unresolved:

- the intended public tag/version already exists or points elsewhere
- authoritative version sources disagree unexpectedly
- the target branch or commit changed without a release-scope decision
- a required validation, review, signature, permission, or credential is unavailable
- the release diff contains unrelated or unexplained changes
- repository policy is consequentially ambiguous
- a privileged or destructive action lacks immediate explicit approval

## Completion record

Finish with the release ledger plus:

- exact tag and target commit
- release commit and PR/MR or direct-integration evidence
- commands/checks and their classified outcomes
- publication targets and verification evidence
- skipped or pending work with reasons
- approvals used and recovery actions taken

## OpenSpec release gate

When the repository contains `openspec/`, inspect active changes before release.
A release may proceed when relevant behavior changes are verified and archived,
or when the release ledger records an explicit reason the active change is not
part of this release. Do not publish code whose claimed behavior exists only in
an unverified or unsynchronized change.

Read-only subagents may gather release evidence or run isolated validation.
The main agent owns the release ledger, target commit, integration, tag, public
publication, and recovery decisions. Never delegate irreversible publication or
run several writers against the release branch.
