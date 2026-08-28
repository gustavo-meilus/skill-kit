# Portable Git Release Runbook

This file is the common process for releasing any Git repository. It contains only the sequence every release needs. After profiling the repository, load the matching branch from [RELEASE-ADAPTERS.md](RELEASE-ADAPTERS.md) rather than reading every possible ecosystem or host path.

Repository-local release instructions, committed automation, CI, and configuration are the source of truth. This runbook supplies discovery, safety gates, and verification where project guidance is incomplete.

## 0. Keep a release ledger

Create and maintain this record before acting. Evidence can be a command result, file path, CI check, forge response, or user decision.

| Field | Value | Evidence/status |
|---|---|---|
| Repository root | | |
| Repository instructions | | |
| Primary remote and host | | |
| Integration/default branch | | |
| Current worktree/branch state | | |
| Release identifier | | |
| Tag name and type | | |
| Previous release boundary | | |
| Target commit | | |
| Version model and sources | | |
| Generated files/tooling | | |
| Release-note source | | |
| Required local checks | | |
| Required remote checks/reviews | | |
| Integration path | | |
| Publication targets | | |
| Signing/provenance requirements | | |
| Credentials/approvals | | |
| Recovery path | | |

Use the statuses **passed**, **failed**, **skipped**, **pending**, and **not applicable** consistently. Publication starts only after every consequential field is known.

## 1. Profile the repository

### 1.1 Establish Git context

Run from the repository root and record the results:

```sh
git rev-parse --show-toplevel
git status --short --branch
git worktree list --porcelain
git remote -v
git branch --show-current
```

Inspect repository-local guidance before applying generic steps. Search for agent instructions, contributor/release documentation, CI definitions, task/build files, and committed release scripts. Follow pointers from those files when they describe the release branch you are taking.

### 1.2 Resolve the remote and integration branch

Choose the remote from upstream configuration, repository policy, or user intent; record the choice.

```sh
git remote
git remote show <remote>
git symbolic-ref --quiet --short refs/remotes/<remote>/HEAD
git remote get-url <remote>
```

When remote HEAD is absent, use upstream branch metadata, forge metadata, or repository instructions. A branch name is a decision backed by evidence, not a default guess.

### 1.3 Discover the release convention

Refresh references without modifying working files:

```sh
git fetch <remote> --tags --prune
git tag --list --sort=-version:refname
git for-each-ref --sort=-creatordate \
  --format='%(refname:short) %(objecttype) %(creatordate:iso8601) %(subject)' \
  refs/tags
```

Determine from history and policy:

- release identifier and tag pattern
- annotated, lightweight, or signed tag
- repository-wide or component-specific release
- prerelease/promotion rules
- version source: manifest, synchronized manifests, generated value, monorepo policy, or tag-only
- release-note source and publication trigger

Load only the relevant sections of [RELEASE-ADAPTERS.md](RELEASE-ADAPTERS.md).

### 1.4 Discover validation and publication gates

Use evidence in this order:

1. release documentation or committed release automation
2. required CI checks, reviews, and branch rules
3. contributor documentation
4. task/build/package configuration
5. ecosystem convention only when the repository supplies no stronger signal

Inspect commands and current `--help` output instead of caching CLI flags in the plan. Separate local validation from remote gates and publication from verification.

**Profile completion criterion:** every consequential ledger field is filled, or marked not applicable with evidence; each conditional adapter to load is named.

## 2. Pin the release

### 2.1 Preserve working state

Record all local state before edits:

```sh
git status --porcelain=v1
git diff
git diff --cached
```

A clean temporary worktree is usually the safest release workspace:

```sh
git worktree add <temporary-path> <integration-ref>
```

When using an existing dirty worktree, account for every local change and keep unrelated work outside the release commit. Use stashing, moving, or cleanup only with a clear recovery path and user approval where work may be affected.

### 2.2 Resolve target and previous boundary

After fetching, resolve immutable commit IDs:

```sh
git rev-parse <remote>/<integration-branch>
git log --oneline --decorate -5 <remote>/<integration-branch>
git rev-parse <previous-tag>^{commit}
```

Review the intended release range using the repository's history model:

```sh
git log --first-parent --oneline <previous-tag>..<target-commit>
git diff --stat <previous-tag>..<target-commit>
```

For component releases, apply repository-defined path or package filtering.

### 2.3 Prove uniqueness

Check the intended tag locally and remotely and check any target registry/forge using its documented lookup path.

```sh
git show-ref --verify --quiet refs/tags/<tag>
git ls-remote --tags <remote> refs/tags/<tag> refs/tags/<tag>^{}
```

An existing public identifier is a release conflict. Preserve it and stop for a recovery decision when it does not match the plan.

**Pin completion criterion:** one release identifier, one tag, one previous boundary, and one target commit are recorded; the intended public identifier is unused.

## 3. Prepare release changes

### 3.1 Use the native path

Run the repository's documented version/release tool, preferably in dry-run or preview mode. Inspect its output and diff before accepting changes.

When the project derives its version from tags or CI, leave tracked version files untouched unless policy says otherwise. When multiple files must agree, identify the authoritative source and generator before editing mirrors.

### 3.2 Apply a manual fallback only when needed

When no native path exists:

1. edit authoritative sources only
2. preserve syntax, ordering, encoding, and line endings
3. regenerate derived files through their generator when available
4. update dependency references only when release policy requires it
5. inspect the complete diff immediately

```sh
git diff --check
git diff --stat
git diff
```

### 3.3 Draft evidence-based release notes

Match the project's current format and vocabulary. Build notes from the pinned change range, merged work, issues, migrations, and supplied documentation. Include compatibility, security, breaking-change, and deprecation claims only when evidence supports them.

When the project does not maintain a changelog, follow its native release-note mechanism. Introducing a new changelog or convention is a product decision, not a release default.

**Prepare completion criterion:** the working diff contains only intended release changes; every version value agrees under the detected model; every generated change has a known generator; every release-note claim has evidence.

## 4. Prove readiness

Create a validation matrix before running checks:

| Gate | Command/source | Required? | Result | Evidence/reason |
|---|---|---:|---|---|
| Manifest/config parse | | | | |
| Version consistency | | | | |
| Format/static analysis | | | | |
| Unit/integration tests | | | | |
| Build/package/dry run | | | | |
| Signing/provenance | | | | |
| Remote CI/reviews | | | | |

Run only checks supported by repository evidence. A guessed ecosystem command is not a substitute for policy.

Always inspect the final intended diff and staging boundary:

```sh
git diff --check
git status --short
git diff --stat
git diff
```

Classify checks truthfully. A skipped required gate needs both repository permission and explicit user acceptance before publication.

**Prove completion criterion:** every required gate is passed, or an allowed exception has immediate explicit approval and a recorded reason; the release diff has no unexplained file.

## 5. Integrate release changes

Choose the first policy-compatible path:

1. repository automation that creates or lands release changes
2. release branch plus PR/MR and required checks/reviews
3. explicitly permitted direct integration
4. tag-only release when no tracked file changes are required

Stage explicit paths and inspect the staged result:

```sh
git add <intended-paths>
git diff --cached --check
git diff --cached
git commit -m '<project-conventional release message>'
```

For a PR/MR, use the detected forge mechanism and its current help/documentation. Keep multiline bodies in a temporary file when shell quoting is uncertain, then remove that file.

Apply privileged merges, review bypasses, direct protected-branch pushes, or force operations only after restating the exact action and obtaining immediate explicit approval.

After integration, fetch and re-pin:

```sh
git fetch <remote> --tags --prune
git rev-parse <remote>/<integration-branch>
git log --oneline --decorate -3 <remote>/<integration-branch>
```

If the branch advanced beyond the intended release scope, decide whether those commits belong in the release before tagging. Re-run post-merge checks required by policy.

**Integrate completion criterion:** the release changes are landed under repository policy, required remote gates are satisfied, and the ledger target commit equals the final release commit on the integration branch.

## 6. Publish

### 6.1 Create the conventional tag on the pinned commit

Use only the tag form established during profiling.

```sh
# Annotated
git tag -a <tag> <target-commit> -m '<release title>'

# Signed, when required and configured
git tag -s <tag> <target-commit> -m '<release title>'

# Lightweight, when it is the project convention
git tag <tag> <target-commit>
```

Verify the local tag before publishing:

```sh
git show --no-patch --decorate <tag>
git rev-parse <tag>^{commit}
```

Push the one intended tag:

```sh
git push <remote> refs/tags/<tag>
```

### 6.2 Trigger native publication

Use the project's configured CI, forge, registry, or release script. Load the matching publication adapter for host releases, packages, containers, binaries, documentation, signatures, checksums, SBOMs, or provenance.

For asynchronous publication, record the run/job identifier and its current state. Pending work stays pending until observed; tag success alone is not package or asset success.

**Publish completion criterion:** the intended public tag exists; each synchronous publication target reports success; every asynchronous target has a concrete run reference and is marked pending or completed.

## 7. Verify and report

### 7.1 Verify the remote tag

```sh
git fetch <remote> --tags --prune
git rev-parse <tag>^{commit}
git ls-remote --tags <remote> refs/tags/<tag> refs/tags/<tag>^{}
```

For annotated or signed tags, compare the peeled `^{}` commit with the ledger target.

### 7.2 Verify every applicable target

Collect direct evidence for the branches used:

- forge release points to the intended tag and has the intended draft/prerelease/final state
- registry reports the intended version
- assets are present, named correctly, and retrievable
- signatures, checksums, SBOMs, or provenance verify
- container digest/tag matches the intended build
- release-triggered CI completed successfully
- documentation/deployment reflects the intended release
- linked issues or milestones changed only as intended

### 7.3 Produce the completion record

Report the completed ledger and summarize:

- repository, remote, and integration branch
- release identifier, tag, and exact target commit
- release commit and PR/MR/direct-integration evidence
- changed files and generator/tool used
- local and remote gate outcomes
- publication targets and verification evidence
- skipped or pending work with reasons
- approvals, bypasses, and recovery actions

**Verify completion criterion:** the remote tag resolves to the ledger target commit and every applicable publication target is directly verified or explicitly pending with a concrete reference.

## 8. Recovery branches

### Before a public tag

Fix the release branch or PR/MR, rerun the required gates, and re-pin the target.

### Local tag only

Prove the tag is absent from every relevant remote, then recreate the local tag if needed:

```sh
git ls-remote --tags <remote> refs/tags/<tag> refs/tags/<tag>^{}
```

### Public tag without completed publication

Keep the public tag stable and repair publication against it when possible.

### Wrong public tag or bad package

Pause normal release work and follow the repository's incident, yank, deprecation, or corrective-release policy. Public tag replacement or history rewriting is exceptional and requires explicit approval plus stakeholder coordination.

### Failed validation or CI

Fix forward on a branch, rerun all required gates, and publish only after the gate is green or an explicitly permitted exception is recorded.

## 9. Final audit

- [ ] The release ledger is complete and evidence-backed.
- [ ] Repository-local policy and native automation were used.
- [ ] Unrelated working-tree state remains recoverable and outside the release.
- [ ] Identifier, tag, previous boundary, and target commit are exact.
- [ ] The detected version model is internally consistent.
- [ ] Release-note claims are supported by the pinned change range.
- [ ] Every required gate is classified and publication policy is satisfied.
- [ ] Integration followed actual branch/review rules.
- [ ] The one intended tag points to the pinned commit.
- [ ] Every applicable publication target is verified or concretely pending.
- [ ] No secret, temporary file, unrelated change, or unexplained generated output was committed.
