# Brainstorm Into an OpenSpec Proposal

Convert exploration or a rough brief into a focused, verifiable OpenSpec change:

`recover -> ground -> normalize -> resolve -> contract -> approve -> propose -> validate -> review`

Use optional deeper analysis only when the change warrants it:

`compare approaches -> test assumptions -> refine contract`

## Hard gates

- Do not write application code, scaffold implementation, or modify product files.
- Do not create the OpenSpec change until the user explicitly approves the normalized change contract.
- Treat silence, earlier exploration agreement, or approval of an approach as insufficient approval of the final contract.
- End with a validated, user-reviewed OpenSpec change ready for apply, not implementation.

## Working principles

- **Reuse known context:** Recover facts, decisions, options, risks, and evidence already present in the conversation or supplied artifacts. Never make the user repeat known information.
- **Ground material claims:** Verify consequential claims against the repository, existing specs, tests, and OpenSpec configuration when those sources are available.
- **Separate certainty:** Distinguish observed facts, user decisions, assumptions, and open questions.
- **One clear intent:** Represent one outcome that can be reviewed, implemented, and validated as a unit.
- **Behavior before implementation:** State what users, consumers, APIs, or systems must observe. Do not prescribe classes, libraries, schemas, frameworks, or internal steps unless they are hard requirements.
- **Make important cases testable:** Capture primary behavior, meaningful alternate flows, failures, edge cases, recovery, compatibility, and persistence semantics when relevant.
- **Preserve what is not changing:** Make compatibility and non-goals explicit when accidental scope expansion would be costly.
- **Resolve material ambiguity:** Ask when an unresolved choice could materially change scope, observable behavior, compatibility, migration, security, or acceptance criteria. Treat minor details as explicit assumptions.
- **Progressive rigor:** Keep straightforward changes concise. Add deeper analysis for high-risk, cross-cutting, architectural, security, privacy, data, migration, or contract-sensitive work.
- **Let OpenSpec define artifacts:** The selected schema, `openspec/config.yaml`, and each artifact's `openspec instructions` output are authoritative. Do not hardcode a replacement artifact format.
- **Review before apply:** Strict validation checks structure; it does not replace behavioral and cross-artifact review.

## 1. Recover the handoff

Recover from the conversation and supplied artifacts:

- problem and affected users or systems
- current behavior, limitation, or regression
- desired outcome and motivation
- relevant files, modules, APIs, data models, tests, and existing capabilities
- constraints, compatibility requirements, and behavior that must be preserved
- options already considered and rejected
- explicit user decisions
- risks, unknowns, and prior evidence

Classify consequential information internally as:

- **Observed fact:** verified in code, specs, tests, configuration, or authoritative documentation
- **User decision:** explicitly chosen by the user
- **Assumption:** reasonable but not verified or explicitly decided
- **Open question:** unresolved and capable of changing the proposal

Do not turn implementation guesses into requirements.

## 2. Resolve the OpenSpec context

When the user names a registered store or the work belongs to one, run:

```bash
openspec store list --json
```

Resolve its store ID and preserve `--store <id>` on commands that accept it, including `new change`, `status`, `instructions`, `list`, `show`, `validate`, `archive`, `doctor`, `context`, `schemas`, and `view`.

Without a selected store, use the nearest initialized local OpenSpec root. Resolve it through the CLI rather than assuming `openspec/` paths. Use:

```bash
openspec context --json
```

and, when useful:

```bash
openspec list --json
```

Read `openspec/config.yaml` or `openspec/config.yml` at the resolved root when present:

- Treat project `context` as facts and constraints.
- Treat artifact `rules` as generation instructions.
- Apply them as instructions; do not copy them mechanically into artifacts.

If a relevant active change already exists, run:

```bash
openspec status --change "<name>" --json
```

Read existing artifacts from CLI-resolved paths. Do not silently overwrite or duplicate a change. Determine whether the same intent should be refined in place or whether the new request is materially different enough to require a distinct change.

Inspect repository files only as needed to close material factual gaps. Do not restart broad exploration by default. If no initialized project or resolvable store exists, stop and state the missing prerequisite.

## 3. Normalize the brief

Internally normalize the request into the smallest sufficient change brief. Use these fields as a reasoning model, not a mandatory output template:

- **Change intent:** one sentence describing the single outcome the change should achieve
- **Problem / current behavior:** what exists today, what is wrong, missing, or limiting, and why the change is needed
- **Desired behavior:** what should be true afterward from an externally observable perspective
- **In scope:** exact behaviors, flows, surfaces, integrations, or capabilities included
- **Out of scope:** adjacent work that must not be introduced
- **Required behaviors and acceptance cases:** primary behavior plus meaningful alternate, edge, failure, recovery, persistence, retry, or idempotency cases when relevant
- **Constraints:** security, privacy, performance, reliability, compatibility, regulatory, platform, dependency, API, UX, or other hard constraints
- **Compatibility and preservation:** existing behavior, contracts, APIs, data, interfaces, or workflows that must remain unchanged
- **Migration / rollout:** existing data, backwards compatibility, deployment, rollback, feature flags, or migration needs when relevant
- **Validation expectations:** tests, observable results, commands, metrics, or other evidence that demonstrates success
- **Assumptions:** minor unresolved details safe to carry as assumptions
- **Material open questions:** only unresolved choices that could change the contract

Omit irrelevant fields rather than filling them with boilerplate.

### Adapt by change type

**Bug or regression**

State both the current broken behavior and intended behavior. Preserve the regression case as an explicit acceptance scenario. Do not reduce the brief to "fix X."

**New feature**

Emphasize the observable capability, happy path, meaningful alternate and error cases, explicit non-goals, and compatibility with nearby behavior.

**Behavior modification**

Distinguish exactly what changes from what must remain compatible. Let OpenSpec map the resulting delta to ADDED, MODIFIED, REMOVED, or RENAMED requirements according to the selected schema.

**Pure refactor, tooling, or docs change**

If externally observable behavior does not change, do not invent a behavioral requirement. Plan `skip_specs: true` when the selected schema and current OpenSpec instructions support it.

**Architecture-oriented change**

Separate mandatory technical constraints from implementation latitude. A technical choice belongs in the approved brief only when the user has decided it is required or repository evidence makes it non-negotiable. Otherwise leave architecture to the design artifact.

**Performance, security, privacy, reliability, or data change**

Turn vague qualities into observable constraints only when the user, existing contract, tests, SLOs, policy, or repository evidence supplies a defensible target. Do not invent thresholds, retention periods, threat models, or compatibility promises merely to make the brief look precise.

## 4. Check scope before details

Split the request when it contains independent outcomes that can be reviewed or shipped separately, such as:

- unrelated user outcomes
- independent services or products
- capabilities with separate rollout or acceptance criteria
- migrations that can stand alone
- behavioral work mixed with unrelated cleanup

For an oversized request:

1. Show the natural slices and dependencies.
2. Recommend the smallest valuable coherent slice.
3. Resolve which slice is being proposed.
4. Continue with that slice only.

Do not hide several projects inside one umbrella change.

## 5. Resolve proposal-critical ambiguity

Ask only when the answer could materially change:

1. intended outcome
2. scope boundary
3. externally observable behavior
4. authorization, privacy, safety, or compliance
5. failure and recovery behavior
6. compatibility or migration
7. measurable acceptance criteria

Prefer concise concrete options when the decision space is known. Use an open question when options would conceal meaningful possibilities.

Do not ask about details that can safely remain design decisions. When a minor detail follows an established repository convention, carry it as an explicit assumption instead of blocking progress.

Stop questioning when the remaining unknowns cannot change requirements, scope, compatibility, migration, or acceptance.

## 6. Apply deeper analysis only when warranted

Do not require approach comparison or falsification for every change. Use this section when a meaningful technical or product choice remains, or when the cost of a wrong assumption is high.

### Compare approaches

Present two or three genuinely different approaches only when choosing among them can change scope, behavior, compatibility, migration, risk, or implementation feasibility. For each, keep the comparison proportional and cover:

- fit with the current system
- externally observable differences, if any
- complexity and operational cost
- compatibility and migration impact
- security, reliability, or data implications when relevant
- reversibility
- testing implications
- intentionally omitted scope

Recommend one approach when the evidence supports it. Do not manufacture alternatives for a trivial change.

### Test assumptions

For consequential uncertainty, identify the assumption, what evidence could disprove it, and what would change in the proposal if disproved. Record a regression behavior when existing accepted behavior is at risk.

Do not force a formal falsification gate into ordinary low-risk work.

## 7. Present the normalized change contract

Before creating OpenSpec files, present a concise contract that reflects the normalized brief. Use only sections that add decision value. A typical contract is:

```markdown
## Proposed OpenSpec Change

**Name:** <kebab-case-name>

**Intent:** <single desired outcome>

**Current / Problem:** <current behavior and why it needs to change>

**Desired Behavior:** <externally observable future behavior>

**In Scope**
- ...

**Out of Scope**
- ...

**Acceptance Cases**
- <primary behavior and expected outcome>
- <important alternate, edge, failure, or regression case when relevant>

**Constraints / Preservation**
- ...

**Migration / Rollout**
- ...

**Validation**
- ...

**Assumptions**
- ...

**Material Decisions**
- <only explicit user decisions or non-negotiable technical constraints>

**Open Questions**
- None
```

For a small change, collapse or omit sections so the contract remains short. Do not duplicate the selected OpenSpec artifact templates. Do not pre-author design.md in the contract.

Inspect existing `openspec/specs/` capability paths before claiming that an existing capability will be modified. Capability mapping is an OpenSpec artifact concern; include it in the contract only when verified and useful for scope approval.

Resolve every question that could change the contract, then ask for explicit approval of the complete contract. Do not create the change before approval.

## 8. Run the proposal workflow

After approval, use the approved contract as the source intent for the installed OpenSpec propose workflow. Preserve:

- approved scope and exclusions
- observable behaviors and acceptance cases
- compatibility and preservation requirements
- hard constraints
- migration or rollout requirements
- validation expectations
- explicit user decisions
- disclosed assumptions

Do not turn unspecified implementation details into requirements. If new repository evidence reveals a conflict that materially changes scope, observable behavior, compatibility, migration, or acceptance criteria, surface it instead of silently redefining the approved change.

If direct `openspec-propose` skill or command invocation is unavailable, execute the equivalent CLI workflow.

### CLI fallback

1. Create the change using the configured default schema unless the user explicitly requested another schema:

   ```bash
   openspec new change "<name>"
   ```

2. For a behavior-free change, set `skip_specs: true` in `.openspec.yaml` only when supported by the selected workflow and consistent with the approved contract.

3. Read the artifact graph:

   ```bash
   openspec status --change "<name>" --json
   ```

4. Compute the required closure from `applyRequires` by recursively following each artifact's `requires` edges. Do not rely on output status alone.

5. For each missing artifact in dependency order, run:

   ```bash
   openspec instructions <artifact-id> --change "<name>" --json
   ```

6. Treat the response as authoritative:
   - apply `context` and `rules` without copying them into artifacts
   - re-read dependency files from disk
   - use `template` and `instruction`
   - honor `skipped`, `warning`, and conditional instructions
   - invoke delegated skills or commands when instructed
   - write to concrete resolved paths, never to a literal glob
   - verify output existence

7. Rerun status after every artifact.

8. Stop when every artifact in the required closure is done, skipped by OpenSpec, or omitted because its own instruction explicitly makes it conditional.

Do not hardcode `proposal.md -> specs -> design -> tasks` as the universal schema. That is the default spec-driven shape, not a guarantee for every configured workflow.

## 9. Validate and self-review

Run strict validation:

```bash
openspec validate "<name>" --strict
```

Then review the actual artifacts in dependency order. For the default spec-driven schema, review proposal, delta specs, design when present, then tasks.

### Intent and scope

- one coherent outcome
- approved problem and desired behavior preserved
- no scope expansion or unrelated cleanup
- explicit breaking or compatibility impact when relevant
- no implementation choice presented as a requirement unless it is mandatory

### Behavioral requirements

When the schema uses delta specs:

- requirements describe observable behavior
- normative language and scenario format follow the active OpenSpec instructions
- each requirement has meaningful scenarios
- primary, alternate, edge, failure, authorization, recovery, compatibility, and regression cases are covered when relevant
- new and modified capability paths match existing organization and approved intent
- no invented requirement exists solely to satisfy validation

### Design

When a design artifact exists:

- it satisfies the approved behavior and hard constraints
- implementation decisions are justified by repository evidence or explicit trade-offs
- it follows existing patterns or explains deviations
- relevant security, performance, migration, rollout, and rollback concerns are addressed
- no unresolved design decision changes the approved behavior contract

### Tasks

When a task artifact exists:

- tasks follow the active artifact instructions
- work is ordered and independently verifiable
- behavioral requirements have implementation and test coverage
- validation and migration work is represented where required
- no task adds out-of-scope work
- no task depends on an unresolved material decision

### Cross-artifact coherence

- proposal intent matches the approved contract
- specs match the approved desired behavior and acceptance cases
- design satisfies specs without redefining them
- tasks implement the design and specs
- constraints, names, APIs, compatibility, migration, and validation expectations agree
- no TBD, TODO, placeholder, contradiction, or material ambiguity remains

Fix issues in the OpenSpec artifacts and rerun:

```bash
openspec validate "<name>" --strict
openspec status --change "<name>"
```

Do not present the change as ready while strict validation fails.

## 10. Request user review and hand off

Summarize:

- change name and resolved location
- selected schema
- artifacts created
- any artifact skipped or omitted and the authoritative reason
- material assumptions retained
- strict-validation result

Ask the user to review the written artifacts. Right-size the review: a tiny low-risk change needs a quick pass; auth, payments, irreversible data changes, migrations, public contracts, security, or privacy work deserves deeper review.

When revisions are requested:

1. update the relevant artifact
2. propagate the decision through dependent artifacts
3. repeat the coherence review
4. rerun strict validation
5. present the revised change for review

Do not start implementation in the same response. After the user later requests implementation, hand off to the apply surface installed for the current tool. Use the invocation OpenSpec generated for that tool instead of assuming one universal command spelling.

## Guardrails

- Use after exploration or when the user explicitly wants structured convergence into an OpenSpec proposal.
- Do not make this workflow mandatory for ordinary brainstorming that is not intended to become an OpenSpec change.
- Do not implement application code.
- Do not ask the user to repeat known findings.
- Ask only material questions; minor implementation details belong in design.
- Decompose oversized work before proposing.
- Do not force alternatives, architecture, or falsification ceremony into trivial changes.
- Require deeper option and assumption analysis when risk or uncertainty makes it decision-relevant.
- Obtain explicit approval of the normalized behavior contract before creating artifacts.
- Keep the change focused and reject unrelated refactoring.
- Follow the selected schema and `openspec instructions` rather than embedded artifact templates.
- Re-read dependencies from disk before generating downstream artifacts.
- Use CLI-resolved roots, stores, paths, and action context.
- Never write to a glob as if it were a file.
- Use `skip_specs: true` only when externally observable behavior does not change and the active workflow supports it.
- Convert vague quality goals into measurable constraints only when the target is grounded; never invent arbitrary metrics.
- Strictly validate and repair inconsistencies before review.
- Do not commit, push, create branches, or open pull requests unless separately requested.
- Hand off only to the OpenSpec apply workflow after a separate user request.
