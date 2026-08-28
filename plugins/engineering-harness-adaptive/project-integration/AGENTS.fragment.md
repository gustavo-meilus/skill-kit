# Engineering discipline contract

For implementation, debugging, refactoring, architecture, testing, dependency, build, CI, migration, or behavior-affecting configuration work, use the `engineering-discipline` skill.

## Operating rules

- Preserve the requested outcome and existing behavior except where the task explicitly requires change.
- Prefer the smallest coherent solution. Apply KISS first and YAGNI aggressively; do not add abstractions, dependencies, agents, indirection, or generalized infrastructure without a concrete need.
- Understand an existing rule, test, boundary, validation, or unusual design before weakening or removing it. Treat unexplained constraints as Chesterton's Fence.
- Prefer structural prevention over reminders: types, schemas, invariants, narrow interfaces, deterministic scripts, and executable checks when they can encode the rule reliably.
- Prefer deterministic evidence over model judgment: compiler/type checks, linters, tests, structural checks, contracts, and executable acceptance checks before semantic review.
- Never weaken, delete, skip, or rewrite tests merely to make an incorrect implementation pass. If expected behavior changes, explain why the oracle changes and preserve equivalent or stronger coverage of the new contract.
- Keep changes local. Do not mix unrelated cleanup with requested work or reopen accepted requirements/design decisions during implementation unless new evidence proves they are invalid or blocking.
- Respect existing architectural boundaries and repository conventions. Improve them only when the requested outcome or a demonstrated defect requires it.
- Use least privilege. Read-only exploration/review should stay read-only; broader capabilities require a concrete need.
- Before declaring completion, inspect the final diff and provide only verification evidence actually obtained.

## Model and effort allocation

Treat **reasoning difficulty** and **change risk** as separate axes. Importance alone is not a reason to maximize model capability or effort.

- Keep the main implementation path at a balanced effort. Medium is the target when the selected model/workload has been validated there; otherwise use the provider's safe default until local evals justify stepping down.
- Use higher effort for unresolved planning, root-cause diagnosis, difficult test/oracle design, and independent review. Return to bounded implementation once the decision is settled.
- Use xHigh/Max only for a bounded hard question with a strong stopping condition: subtle concurrency, security, migration invariants, distributed state, or a stubborn failure after a lower-effort attempt.
- Use efficient models/low effort for narrow read-only lookup, classification, file discovery, repetitive transformations, and other tasks with strong deterministic checks.
- Escalate after evidence of uncertainty or failure rather than prepaying frontier-model/highest-effort compute for every phase.
- Escalate one axis at a time when practical: effort first on the current capable model, then model tier if the task still needs more capability. Downgrade again after the hard question is resolved.
- Higher effort requires a narrower problem statement and stronger stop condition, not a longer generic process prompt.
- Do not spawn another agent when a compiler, deterministic script, test, or direct inspection answers the question more cheaply and reliably.

Use the provider-specific `engineering-scout`, `engineering-planner`, `engineering-reviewer`, and `engineering-specialist` roles only when their narrower task justifies separate context/model allocation. The implementation agent remains responsible for the requested change.

## Project knowledge

Treat repository-local code, tests, schemas, architecture documents, decision records, and executable scripts as the system of record. Keep this file short; place specialized procedures in skills or nearby scoped instructions.

## Verification

The provider hook adapters share one authoritative final verification gate. If verification fails, fix the cause rather than bypassing the gate. If no canonical verifier exists for a code-changing task, establish one or configure the harness before claiming completion.
