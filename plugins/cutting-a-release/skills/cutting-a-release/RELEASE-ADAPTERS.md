# Git Release Adapters

This is conditional reference for [RUNBOOK.md](RUNBOOK.md). Load only the sections selected by the release profile. The common sequence remains Profile → Pin → Prepare → Prove → Integrate → Publish → Verify.

## 1. Version-model adapters

### 1.1 Tag-only

**Use when:** repository evidence derives the version from Git tags and no tracked version source must change.

**Actions:**

- verify the tag convention and target commit
- leave manifests or generated version output untouched unless policy requires them
- use the pinned change range for notes and validation

**Done when:** no tracked version edit is required and the planned tag uniquely represents the release.

### 1.2 Single authoritative source

**Use when:** one tracked manifest or version file controls the release.

**Actions:**

- use the project's version command when available
- edit the one authority only as a fallback
- regenerate mirrors, lockfiles, or artifacts through native tooling

**Done when:** the authority contains the release value and every derived output either matches or is intentionally generated later.

### 1.3 Synchronized sources

**Use when:** several files must carry the same repository-wide version.

**Actions:**

- find the committed synchronizer, generator, or check before editing
- identify one authority and classify the rest as mirrors when policy supports that distinction
- run the consistency check before and after integration

**Done when:** every required source reports the intended value and no unrelated version field was changed.

### 1.4 Generated version

**Use when:** build metadata, VCS state, or a generator produces the version.

**Actions:**

- locate the generator and its input
- modify the input or tag, not generated output
- prove the generated value in a dry run or build artifact

**Done when:** the generator produces the intended version from the pinned commit.

### 1.5 Fixed-version monorepo

**Use when:** all releasable components move together.

**Actions:**

- use workspace/release tooling to update the shared version and internal dependencies
- include all policy-required packages, even unchanged ones, only when the fixed-version model requires it
- validate the workspace-wide graph

**Done when:** all governed components agree and workspace validation passes.

### 1.6 Independent-version monorepo

**Use when:** components publish separately.

**Actions:**

- identify the changed component set from repository policy/tooling
- use component tag and changelog conventions
- restrict version edits, validation, notes, and publication to the release set plus required dependents
- keep unaffected packages out of the release diff

**Done when:** every releasing component has an exact identifier/target and every non-releasing component remains unchanged unless dependency policy requires an update.

## 2. Integration and host adapters

### 2.1 Hosted forge with PR/MR

**Use when:** the remote host exposes reviews, checks, releases, or protected branches.

**Actions:**

- use forge metadata to confirm the integration branch and required gates
- prefer the available connector/API or documented CLI for PR/MR and release objects
- inspect current command help before using flags
- capture PR/MR, check, merge, release, and workflow identifiers in the ledger

**Done when:** repository-required review/check policy is satisfied and the integrated commit is re-pinned.

### 2.2 Authorized direct integration

**Use when:** repository policy explicitly permits a direct commit or push.

**Actions:**

- confirm the branch and fast-forward relationship immediately before pushing
- push the exact intended ref without force
- fetch and verify the remote commit afterward

**Done when:** the remote integration ref equals the intended release commit and no protection was bypassed.

### 2.3 Plain Git remote or unknown forge

**Use when:** no supported release API/CLI is available.

**Actions:**

- use ordinary Git branches and tags as the portable baseline
- follow repository-defined review coordination outside the tooling when applicable
- treat any web release object as a manual or external step

**Done when:** the remote tag and integration ref are verified; unsupported host actions are explicitly reported rather than inferred.

### 2.4 CI-created release

**Use when:** merge or tag events drive publication.

**Actions:**

- identify the exact trigger and required inputs
- perform only the change or tag that the workflow expects
- capture the triggered run and verify jobs/artifacts
- avoid manually duplicating package or forge publication

**Done when:** the intended workflow run is associated with the pinned commit/tag and each required job reaches its expected state.

## 3. Publication adapters

### 3.1 Forge release object

Confirm the release object:

- references the intended tag
- has the intended draft, prerelease, or final state
- contains evidence-based notes
- includes every required asset

The Git tag is the commit anchor; the forge object is publication metadata.

### 3.2 Language/package registry

Use the repository's documented credentials and publish command or CI. Before publishing, query whether the version already exists. Afterward, query registry metadata directly and, when practical, install or inspect the published artifact.

**Done when:** the registry reports the intended package/version and its artifact metadata matches the plan.

### 3.3 Container registry

Publish immutable images from the pinned commit. Record digests, not only mutable tags. Verify every required architecture/platform manifest.

**Done when:** expected tags resolve to recorded digests and the manifest set is complete.

### 3.4 Binary assets

Build through reproducible project tooling where available. Verify filenames, embedded versions, checksums, signatures, target platforms, and downloadability.

**Done when:** every required asset is attached to the intended release and its integrity evidence verifies.

### 3.5 Documentation or deployment

Treat documentation publication or deployment as a separate target with its own gate and evidence. A package release does not prove docs or deployment completed.

**Done when:** the target environment exposes the intended release/version and its workflow reports success.

## 4. Signing and provenance adapter

**Use when:** repository policy or publication infrastructure requires signed tags, commits, packages, attestations, SBOMs, or provenance.

- establish the required identity and tool before publication
- keep private key material outside repository files and logs
- verify signatures/attestations using the public verification path
- record verification output or artifact identifiers

**Done when:** each required public object verifies against the expected identity and pinned commit/artifact.

## 5. Shell and platform adapter

Prefer commands already used by the repository. Keep Git operations shell-neutral where possible. For multiline bodies or generated notes, write a temporary UTF-8 file and pass it to the tool rather than embedding shell-specific quoting. Remove the temporary file and confirm it is absent from staged changes.

Use platform-native path handling and encoding rules. Preserve existing line endings and file encodings; for JSON, use UTF-8 without a BOM unless repository policy specifies another format.
