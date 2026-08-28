---
name: more-with-less
description: Apply minimum-sufficient engineering to project development, design, debugging, refactoring, specification, architecture, dependencies, tooling, agents, hooks, MCP, automation, and verification. Use for non-trivial project work where unnecessary complexity should be minimized without weakening correctness, security, data integrity, accessibility, operability, observability, or acceptance criteria. Do not use for pure prose or unrelated non-project tasks.
---

# More With Less Engineering

Use this Skill as the default design and implementation lens for non-trivial project work.

The objective is not minimum code, files, tokens, tools, agents, or tests independently. The objective is the **minimum sufficient system** that reliably satisfies the real requirements and preserves required guarantees.

## Core doctrine

> Do the least that fully solves the real problem. Use the least powerful sufficient mechanism. Keep active context, authority, tools, state, agents, handoffs, and orchestration as small as practical. Preserve the guarantees that matter. Hide unavoidable complexity behind stable interfaces. Add complexity only when evidence shows the simpler system is insufficient, and remove it when that evidence no longer holds.

## Mandatory operating rules

1. **Understand before simplifying.** Inspect the relevant code, docs, behavior, callers, constraints, and existing guarantees before choosing the smaller solution.
2. **Solve the real requirement.** Prefer outcome and acceptance criteria over user-prescribed implementation choreography unless the implementation method is itself a requirement.
3. **Delete or reuse before adding.** Prefer existing project capability, language/runtime facilities, native platform behavior, installed dependencies, and deterministic scripts before new machinery.
4. **Use the least powerful sufficient mechanism.** Prefer deterministic code, schemas, tests, linters, type systems, DB constraints, and scripts before model judgment or orchestration when they can decide the property reliably.
5. **Keep context progressive.** Load only the information required for the current decision. Do not dump the whole repository, spec corpus, or this full playbook into context without need.
6. **One agent by default.** Add a reviewer/specialist only for independent judgment, context isolation, different authority, specialized expertise, or useful parallelism.
7. **Minimize the tool and permission surface.** Give the current task only the capabilities needed to understand, act, observe, and verify.
8. **Make specification proportional.** Spec depth grows with uncertainty, consequence, and coordination. Do not force proposal/design/task ceremony onto trivial work.
9. **Make verification proportional.** Use the minimum evidence sufficiently strong for the consequence of failure. Keep the oracle stronger than the generator.
10. **Never simplify away critical guarantees.** Preserve trust-boundary validation, security, authorization, data integrity, accessibility, irreversible-operation safeguards, required architecture invariants, acceptance criteria, rollback/recovery, necessary observability, and explicit requirements.
11. **Prefer root-cause fixes.** For bugs, reproduce when feasible, trace the real path, and fix the shared cause rather than patching symptoms repeatedly.
12. **Design for deletion.** For non-trivial new harness or architecture mechanisms, know why they exist, what would prove them insufficient, and what would allow them to be removed.

## Decision ladder

Before adding custom code or harness machinery, stop at the first sufficient rung:

```text
1. Does this need to exist?
2. Is it already handled correctly in the project?
3. Can an existing deterministic project mechanism solve it?
4. Can the language/runtime/stdlib/native platform solve it?
5. Can an installed dependency or existing tool solve it?
6. Can one small direct script/check/implementation solve it?
7. Can one agent with the current feedback loop solve it?
8. Does one specialist context materially improve reliability?
9. Does a bounded loop materially improve convergence?
10. Only then build custom orchestration or infrastructure.
```

When comparing two solutions, optimize **total** complexity, not local line count. A slightly larger boundary can be simpler if it hides volatility or removes coupling.

## Workflow

### 1. Establish the completion contract

For non-trivial work identify:

- required observable outcome;
- constraints and non-goals;
- invariants that must survive;
- what evidence counts as complete.

If the task is trivial and obvious, keep this implicit and move on. Do not manufacture planning artifacts.

### 2. Inspect before editing

Read the smallest useful set of:

- relevant implementation;
- callers/consumers;
- local project instructions;
- active spec/change artifact;
- architecture constraints;
- existing tests/checks.

For bugs, reproduce the failure first when feasible.

### 3. Choose specification depth

Use this scale:

```text
trivial change
  -> direct task

obvious bug
  -> expected behavior + regression check

small feature
  -> behavior + acceptance criteria

complex feature
  -> proposal + spec + design + tasks when each removes distinct uncertainty

high-risk migration/security/protocol change
  -> explicit behavior + design + rollback/compatibility + verification
```

Each artifact must eliminate a different uncertainty. If it does not affect a later decision, remove it, make it conditional, or replace it with a reference.

### 4. Implement the smallest coherent solution

Prefer, in order:

```text
remove / reuse
existing project mechanism
standard/native capability
existing dependency
small deterministic mechanism
minimum custom implementation
new dependency or subsystem only when justified
```

Do not create abstractions just to avoid short-term duplication. Introduce an abstraction when it demonstrably compresses knowledge, hides volatility, removes real coupling, or already has multiple concrete uses.

### 5. Verify at the required tier

```text
Tier 0 - trivial
  build / format / type validity as applicable

Tier 1 - ordinary change
  + affected tests

Tier 2 - behavioral feature
  + integration / executable acceptance

Tier 3 - invariant-sensitive
  + architecture / security / property checks where relevant

Tier 4 - high consequence or high autonomy
  + independent semantic review where mechanical evidence is insufficient
  + mutation where test sensitivity matters
  + E2E/UI evidence where users are affected
  + external evidence provenance for high-value measurements
```

Do not run an expensive gauntlet merely because it exists. Do not omit a required check merely because it is expensive.

### 6. Review for deletion and unnecessary complexity

Before completion ask:

- What did this change add: concept, dependency, state, interface, artifact, tool, agent, hook, or handoff?
- Which addition is essential?
- Can anything now be deleted or collapsed?
- Did complexity move elsewhere instead of disappearing?
- Did any simplification weaken a guarantee?

### 7. Report evidence honestly

State what was actually verified. Never imply that a test, benchmark, UI path, security check, or external measurement passed if it was not run or independently observed.

## Harness-specific rules

When changing AI/harness infrastructure:

- Prefer a small `AGENTS.md`/project contract over a giant always-loaded manual.
- Prefer Skills for specialized reusable procedures and scripts for deterministic mechanics.
- Use hooks only for lifecycle persistence, permissions, completion gates, or other invariants that should not depend on model memory.
- Minimize MCP/tool exposure; defer discovery where possible.
- Do not add a second agent unless it has a concrete reason to exist.
- Do not add an outer loop until an objective failure signal, retry budget, progress detection, strategy change, and escalation condition exist.
- Keep high-value evidence collection outside the implementation agent's sole control.

## When to load the full playbook

Do **not** read `references/playbook.md` by default.

Read the relevant sections only when the task involves one or more of:

- designing or changing a harness;
- choosing between Skills, hooks, agents, MCP, worktrees, or loops;
- designing a Spec-Driven Development workflow;
- deciding verification/evidence architecture;
- high-risk architecture or migration work;
- diagnosing recurring agent failures;
- benchmarking or simplifying an existing harness;
- explaining the principles or their research basis.

For Codex-specific implementation details and source links, read `references/codex-implementation-notes.md`.

## Completion standard

Do not claim completion unless the requested behavior is satisfied and the verification evidence you actually have is stated accurately.

For ordinary work, keep the final report concise:

```text
Changed: <what materially changed>
Verified: <checks/evidence actually run>
Complexity: <only mention if a meaningful dependency, abstraction, tool, agent, hook, or limitation was added/removed>
```
