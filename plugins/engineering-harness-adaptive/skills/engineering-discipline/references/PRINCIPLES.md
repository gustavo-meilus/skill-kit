# Engineering principles reference

Use principles as decision aids, not independent objectives. Correctness and the explicit requirement outrank stylistic purity.

## KISS

Choose the least complex design that fully meets current requirements. Complexity includes code, abstractions, dependencies, configuration, agents, hooks, handoffs, and operational states.

## YAGNI

Do not build for hypothetical future requirements. Add extension points when a real second use or known requirement justifies them.

## DRY

Centralize duplicated knowledge, business rules, schemas, invariants, and policies. Do not force superficially similar code behind an abstraction when the concepts can evolve independently.

## Separation of Concerns / SRP

Separate responsibilities when they change for different reasons, require different privileges, or benefit from independent verification. Avoid needless fragmentation.

## SOLID

Use SOLID to control coupling and substitutability where it materially improves the design. Do not introduce interfaces, factories, layers, or dependency injection without a concrete seam or variation that needs them.

## Gall's Law

Build a simple working system and evolve it. Large orchestration and framework designs should emerge from demonstrated needs, not precede them.

## Chesterton's Fence

Do not remove an existing rule, check, validation, compatibility behavior, or unusual constraint until its purpose and consequences are understood.

## Poka-yoke / Make invalid states unrepresentable

Prefer designs that prevent mistakes: types, schemas, constraints, constructors, generated artifacts, architecture rules, safe APIs, and canonical scripts.

## Fail Fast

Detect cheap failures early and close to the change. Prefer compiler, type, lint, focused tests, and structural checks before expensive E2E or semantic review.

## Defense in Depth

Use multiple independent sensors only when they cover materially different failure modes. More checks are not automatically safer if they are redundant, noisy, or unaffordable.

## Least Privilege

Give a task or agent only the capabilities it needs. Read-only investigation and review should remain read-only. Privilege boundaries also reduce the action space and accidental damage.

## Principle of Least Astonishment

Prefer predictable repository structure, naming, commands, APIs, and failure messages. Agent-legible is usually human-legible too.

## Information Hiding / Law of Demeter

Keep module contracts narrow so a change can be reasoned about locally. Avoid forcing callers or agents to understand distant implementation details.

## Reversible decisions

Use lightweight experimentation for cheap, reversible decisions. Increase specification, review, and approval for expensive or irreversible changes.

## Control-system view

Treat development as a feedback system:
- guides/feedforward: requirements, architecture, AGENTS, skills, schemas, safe APIs;
- sensors/feedback: compiler, tests, linters, logs, browser, metrics, reviewers;
- controller: Codex and the human steering it;
- plant: the repository and running system.

A good harness improves observability and correction without adding unnecessary control machinery.
