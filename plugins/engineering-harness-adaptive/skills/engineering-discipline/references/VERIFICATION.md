# Verification and evidence reference

## Prefer independent, executable evidence

A useful evidence hierarchy is:

1. compiler/type/system constraints;
2. deterministic validators and static analysis;
3. focused tests and property checks;
4. structural/architecture checks;
5. integration/contract tests;
6. executable acceptance/UI/E2E evidence;
7. mutation, coverage-quality, performance, or security analysis where relevant;
8. independent LLM review;
9. same-agent self-review.

This is not an absolute ordering: choose the cheapest reliable oracle for the behavior at risk.

## Test the contract, not the implementation

Tests should constrain externally meaningful behavior and important invariants. Avoid tests whose only purpose is preserving incidental implementation details.

When implementation and tests are both newly generated, strengthen the oracle with one or more independent sources where important:
- user-approved acceptance examples;
- existing behavior/fixtures;
- schemas/contracts;
- property-based invariants;
- mutation testing;
- real-system E2E evidence;
- independent reviewer or human validation.

## Coverage is not correctness

Coverage says code executed. It does not prove assertions are meaningful. Use mutation testing selectively when weak tests are a material risk.

## Separate producer and judge

The implementation agent should not be the only authority deciding whether its own work is correct. Prefer deterministic gates first; use a read-only independent reviewer for semantic risks.

## Preserve oracle integrity

A failing test is evidence, not an obstacle. Do not delete, skip, loosen, or rewrite checks merely to obtain green output. If the requirement intentionally changes, update the oracle with an explicit rationale and equivalent or stronger evidence for the new contract.

## Runtime evidence

For behavior that depends on a running system, source-level reasoning is insufficient. Use available logs, traces, browser automation, database state, network evidence, metrics, or recorded artifacts when they materially reduce uncertainty.

## Report evidence precisely

At completion distinguish:
- checks actually run and passed;
- checks not available or not run;
- semantic/manual observations;
- residual risks or assumptions.

Never convert "I inspected it" into "tests pass" or "likely correct" into "verified."
