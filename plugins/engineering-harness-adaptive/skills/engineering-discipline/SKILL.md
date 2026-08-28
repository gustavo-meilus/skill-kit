---
name: engineering-discipline
description: Apply disciplined software engineering to implementation, debugging, refactoring, architecture, tests, migrations, dependencies, build/CI, and behavior-affecting configuration. Use KISS/YAGNI, explicit acceptance criteria, adaptive model/effort allocation, deterministic verification, architecture boundaries, and independent review only when warranted. Do not use for simple read-only questions or purely editorial prose changes.
---

# Engineering Discipline

Use this workflow for software changes. Optimize for correctness and evidence with the least process, model capability, reasoning effort, and orchestration that adequately controls the task.

## 1. Orient before editing

1. Read applicable repository instructions and relevant local documentation.
2. Inspect the implementation, tests, and call paths that own the behavior. Do not design from filenames or assumptions alone.
3. Identify existing invariants, boundaries, conventions, generated files, and validation. Do not remove unusual constraints until their purpose is understood.
4. For version-sensitive external APIs or tools, verify current official documentation rather than guessing.

Use an `engineering-scout` only when a narrow read-only search can keep noise out of the main context. Use an `engineering-planner` only when the task has unresolved semantic, architectural, or causal complexity that materially benefits from a separate high-effort pass.

## 2. Define the scope contract

For non-trivial work, establish a compact contract:

```text
Goal:
  one observable outcome

In scope:
  specific behavior/surfaces

Out of scope:
  important exclusions

Done when:
  executable checks or other concrete evidence
```

Do not create a large specification for a small change. A spec, design, ADR, or task plan is useful only when it removes a future decision or preserves important reasoning across context boundaries.

Once requirements/design are accepted, implementation should execute them rather than reopening them because a different design seems more elegant. New evidence may reopen a decision only when the accepted decision is contradictory, unsafe, impossible, or blocks the requested outcome.

## 3. Classify risk and reasoning difficulty separately

### Change risk

- **Low:** local, reversible, well-tested, no public contract/data impact.
- **Medium:** multiple modules, public behavior/API change, dependency change, integration behavior, non-trivial refactor, or meaningful regression risk.
- **High:** auth/security, privacy, destructive/data migration, concurrency, financial logic, irreversible operation, production infrastructure, or broad public API change.

Risk determines the strength and independence of verification. It does **not** automatically determine the model tier.

### Reasoning difficulty

- **D0 mechanical:** explicit transformation, obvious location, deterministic oracle.
- **D1 routine:** known requirement, familiar/local architecture, ordinary implementation choices.
- **D2 complex:** root cause unknown, multi-module causality, meaningful design choice, difficult edge cases or oracle design.
- **D3 specialist:** subtle security/concurrency/distributed state/migration invariant, or repeated plausible hypotheses have failed.

Difficulty determines reasoning/model escalation. An important but straightforward change can be high-risk and still D1; compensate with stronger verification instead of automatically using maximum reasoning.

## 4. Allocate model and effort before spending it

Default shape:

```text
explore/locate        -> efficient model, low/medium
plan/diagnose         -> capable model, high
implement settled work-> balanced model, medium when validated
verify/review         -> capable model, high
bounded hard question -> frontier model, xHigh; Max only exceptionally
parallel orchestration-> only when workstreams are genuinely independent
```

Use these rules:

1. Start at the lowest configuration that has demonstrated adequate quality for this task class. When no local eval exists, use the provider's documented safe starting point and calibrate downward later.
2. Escalate because of uncertainty, long causal chains, failed hypotheses, difficult tradeoffs, or difficult verification - not merely because the task is important.
3. With a trustworthy verifier, prefer `attempt -> verify -> escalate the failed/uncertain step` over running the whole workflow at maximum effort.
4. Escalate one axis at a time when practical: increase effort on the current model, then move to a stronger model if capability remains the bottleneck.
5. After planning/diagnosis resolves the hard question, return implementation to a bounded balanced configuration. Do not let expensive reasoning continuously reopen settled decisions.
6. High/xHigh work must have explicit scope and stopping criteria. More effort plus vague autonomy increases scope-expansion risk.
7. Use Max only when a bounded quality-first problem remains unsolved and the marginal quality is worth the latency/cost. It is never the ambient project default.
8. Multi-agent/parallel modes are an orchestration choice, not a synonym for deeper reasoning. Use them only when tasks can proceed independently with clear synthesis boundaries.

Provider mappings, bootstrap-vs-calibrated policy, and the escalation state machine are in `references/EFFORT_ROUTING.md`.

## 5. Choose the simplest adequate design

Apply in this order:

1. **KISS:** simplest design that fully satisfies the requirement.
2. **YAGNI:** no anticipated extension points, frameworks, or generalized infrastructure without a present use.
3. **Existing design first:** prefer established project patterns while they remain adequate.
4. **Poka-yoke:** structurally prevent recurring mistakes before adding another instruction.
5. **Make invalid states unrepresentable:** use types, schemas, constraints, constructors, or boundary validation when appropriate.
6. **Separation of concerns:** separate responsibilities when it improves change isolation or independent verification, not for aesthetic purity.
7. **DRY with judgment:** centralize duplicated knowledge/invariants; tolerate small duplication when abstraction would obscure intent or couple unrelated concepts.
8. **SOLID as heuristics:** use them to reduce concrete coupling/substitution/testability problems, not as goals in themselves.
9. **Gall's Law:** evolve complexity from a simple working system.
10. **Least astonishment:** prefer discoverable names, commands, layouts, and conventions.

Before adding a dependency, abstraction, service, agent, hook, or framework, ask: "What concrete failure or requirement makes this necessary now?"

See `references/PRINCIPLES.md` when a tradeoff is material.

## 6. Establish an independent failure signal when feasible

For a bug or behavior change:

1. Reproduce current behavior when practical.
2. Add or identify a focused failing test/acceptance check when expected behavior can be established reliably.
3. Implement the smallest coherent change that makes the behavior correct.
4. Refactor only enough to leave the touched area understandable.

Do not mechanically recite TDD ceremony. Preserve its useful property: an external executable oracle constrains the implementation and supplies a stopping condition.

For difficult changes, scrutinize the **spec/test boundary**. If the same agent invents the requirement, expected result, test, implementation, and final judgment, a green test can become circular evidence. Prefer human-approved semantics, existing contracts, independent fixtures, property/invariant tests, or an independent reviewer where warranted.

## 7. Keep implementation narrow

During implementation:

- avoid unrelated cleanup and speculative generalization;
- avoid broad rewrites when a targeted change is adequate;
- preserve public contracts unless changing them is required;
- do not edit generated artifacts manually unless the project explicitly requires it;
- do not weaken the oracle to obtain green output;
- if implementation uncovers a separate improvement, record/report it rather than silently expanding scope.

Implementation is usually execution of a settled decision. If it becomes a discovery problem, stop and explicitly reclassify/escalate that subproblem rather than silently raising effort and scope for the whole task.

## 8. Verify from cheap/deterministic to expensive/inferential

Use only relevant levels:

1. syntax/format/static validity;
2. compiler/type checker/linter;
3. focused unit/property tests;
4. architecture/structural checks;
5. integration/contract tests;
6. executable acceptance/UI/E2E checks;
7. coverage/mutation/performance/security checks when risk warrants them;
8. independent semantic review;
9. human judgment for requirements, UX, irreversible actions, or unresolved ambiguity.

Run cheap high-signal checks early. Run the canonical final verifier before completion. Never substitute an LLM opinion for a deterministic check that exists.

See `references/VERIFICATION.md` for oracle guidance.

## 9. Use specialized agents only for isolated cognitive work

The prepared roles are intentionally read-only:

- **engineering-scout:** cheap targeted repository lookup/file discovery.
- **engineering-planner:** high-effort plan/root-cause analysis when D2 work benefits from separate context.
- **engineering-reviewer:** independent post-verification review for medium/high-risk work or residual semantic uncertainty.
- **engineering-specialist:** xHigh bounded analysis for D3 problems only.

The main agent owns implementation. This avoids write conflicts, duplicated investigation, and coordination overhead merely to change effort/model by phase.

For medium/high-risk work, run deterministic checks before `engineering-reviewer`. For D3 issues, give `engineering-specialist` one narrow question plus evidence and a stopping condition, then return the result to the main implementation path.

## 10. Completion

Before finishing:

1. inspect the final diff for accidental/unrelated changes;
2. verify acceptance criteria one by one;
3. run the canonical project verification command;
4. confirm no test/validation/security boundary was weakened without explicit justification;
5. resolve material independent-review findings when review was required;
6. report changes, evidence obtained, and any residual risk/unverified area.

A verification hook may continue the turn after failure. Fix the failure; do not bypass the gate.

## 11. Improve the harness from evidence, including effort data

When the same failure recurs, propose the smallest reusable control:

`design simplification -> invariant/type/schema -> deterministic script/lint/test -> documentation/context -> skill -> reviewer agent -> orchestration`

Prefer earlier options. Periodically remove stale or redundant controls.

Also measure your local model/effort curve. For representative tasks record at least: accepted-task rate, human-review defects, changed files/lines, failed attempts, latency, tool calls/tokens when available, and rework. Promote or downgrade a task class only when the evidence justifies it.
