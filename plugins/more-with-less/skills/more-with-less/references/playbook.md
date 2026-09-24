# More With Less in AI Engineering: Definitive Complete Guide and Playbook

> **Coverage warning:** This guide was produced from the conversation content currently available to the model. Some referenced source material may not be present. In particular, the uploaded Harness Engineering source document states that some raw web-search and page-open results from its original research conversation were redacted in the accessible history. Exact raw outputs from those missing research turns are not reconstructed here. The source conversation also did not expose an identifier for the previously created monitoring automation, so none is invented. Public URLs, repository files, commands, configurations, benchmark details, and conclusions that remain accessible are preserved below.

## Executive Summary

This document combines two substantial bodies of work established in the source conversation:

1. a complete Harness Engineering methodology for coding agents, with a practical Codex CLI implementation model and verification-heavy lessons from Robert C. Martin's Agentic Discipline and SwarmForge work; and
2. a later research and synthesis effort around KISS, YAGNI, DRY, the Rule of Least Power, information hiding, boring technology, context minimization, Ponytail, OpenSpec, and other "more with less" design principles.

The final result is a project-agnostic methodology for building AI engineering systems that are reliable without becoming unnecessarily elaborate.

The central principle is:

> **Build the minimum sufficient system that reliably closes the loop from intent to independently verified result.**

This is not "fewest lines", "fewest tokens", or "fewest components". It is minimum **total accidental complexity** subject to the guarantees that matter.

A useful optimization model is:

```text
minimize
    concepts
  + state
  + branches
  + dependencies
  + interfaces
  + configuration
  + always-loaded context
  + tool surface
  + authority surface
  + agent roles
  + handoffs
  + orchestration
  + maintenance burden

subject to
    required behavior
  + correctness
  + security
  + data integrity
  + accessibility
  + operability
  + necessary observability
  + explicit constraints
  + sufficient verification
  + recoverability
```

The default architecture is intentionally small:

```text
HUMAN INTENT
     |
     v
minimum sufficient specification
     |
     v
small operating contract
     |
     v
relevant context only
     |
     v
ONE PRIMARY AGENT
     |
     v
smallest coherent implementation
     |
     v
deterministic verification
     |
 +---+---+
 |       |
pass    fail
 |       |
 |   bounded repair
 |       |
 |   escalate only when needed
 |
 v
independent semantic review
only where mechanical evidence is insufficient
     |
     v
external evidence gate
where consequence requires it
     |
     v
DONE
```

Everything else - Skills, hooks, MCP servers, additional tools, subagents, worktrees, outer loops, custom state, extra specification artifacts, mutation testing, UI QA, distributed orchestration - is optional. It must earn its place by solving a concrete recurring failure, required control, missing capability, risk, or coordination problem that a simpler mechanism cannot solve sufficiently well.

The most important derived rules are:

- Understand fully before simplifying.
- Delete before adding.
- Reuse existing project, standard, native, and installed capabilities before writing custom machinery.
- Use the least powerful sufficient mechanism.
- Prefer deterministic enforcement over repeated prose reminders.
- Keep always-on instructions small and use progressive disclosure.
- Give agents the minimum tool and authority surface needed to act and verify.
- Use one agent by default.
- Add loops only after reliable feedback, retry limits, progress detection, and escalation exist.
- Make specification depth proportional to uncertainty, consequence, and coordination.
- Make verification strength proportional to risk while keeping the oracle stronger than the generator.
- Keep evidence production outside the agent's sole discretionary control for high-value claims.
- Treat harness complexity as debt: record why it exists, measure whether it pays for itself, and remove it when it no longer does.
- Prefer improving the repository itself over compensating with more harness machinery.

This guide is both a **Complete Guide** and a **Playbook** because the subject requires a conceptual architecture, design doctrine, correction history, and a repeatable implementation procedure.

## Table of Contents

- [Purpose and Scope](#purpose-and-scope)
- [Final State and Outcome](#final-state-and-outcome)
- [Prerequisites and Inputs](#prerequisites-and-inputs)
- [Part I - Core Principles and Conceptual Model](#part-i---core-principles-and-conceptual-model)
  - [1. Minimum Sufficient System](#1-minimum-sufficient-system)
  - [2. Simple Is Not the Same as Short or Easy](#2-simple-is-not-the-same-as-short-or-easy)
  - [3. The Principle Family](#3-the-principle-family)
  - [4. Complexity Must Be Earned](#4-complexity-must-be-earned)
  - [5. The Minimum Sufficient Harness Ladder](#5-the-minimum-sufficient-harness-ladder)
  - [6. Deterministic Shell, Probabilistic Middle](#6-deterministic-shell-probabilistic-middle)
  - [7. Minimum Sufficient Context](#7-minimum-sufficient-context)
  - [8. Minimum Tool Surface and Minimum Authority](#8-minimum-tool-surface-and-minimum-authority)
  - [9. Minimum Sufficient Agency](#9-minimum-sufficient-agency)
  - [10. One Source of Truth Per Kind of Knowledge](#10-one-source-of-truth-per-kind-of-knowledge)
  - [11. Information Hiding for AI Systems](#11-information-hiding-for-ai-systems)
- [Part II - Complete Playbook](#part-ii---complete-playbook)
  - [Phase 0 - Establish the Minimum Sufficient Harness](#phase-0---establish-the-minimum-sufficient-harness)
  - [Phase 1 - Define the Operating Contract](#phase-1---define-the-operating-contract)
  - [Phase 2 - Make the Project Agent-Legible](#phase-2---make-the-project-agent-legible)
  - [Phase 3 - Build Stable Verification Entrypoints](#phase-3---build-stable-verification-entrypoints)
  - [Phase 4 - Add Runtime Observability Only Where Needed](#phase-4---add-runtime-observability-only-where-needed)
  - [Phase 5 - Bound Tools and Authority](#phase-5---bound-tools-and-authority)
  - [Phase 6 - Add Skills and Hooks Sparingly](#phase-6---add-skills-and-hooks-sparingly)
  - [Phase 7 - Apply Minimum Sufficient Spec-Driven Development](#phase-7---apply-minimum-sufficient-spec-driven-development)
  - [Phase 8 - Implement With the Simplicity Ladder](#phase-8---implement-with-the-simplicity-ladder)
  - [Phase 9 - Use Risk-Proportional Verification](#phase-9---use-risk-proportional-verification)
  - [Phase 10 - Add Independent Evaluation and Evidence Integrity](#phase-10---add-independent-evaluation-and-evidence-integrity)
  - [Phase 11 - Add Worktrees, Subagents, and Loops Only When Earned](#phase-11---add-worktrees-subagents-and-loops-only-when-earned)
  - [Phase 12 - Automate Non-Interactive Runs Carefully](#phase-12---automate-non-interactive-runs-carefully)
  - [Phase 13 - Evaluate and Simplify Continuously](#phase-13---evaluate-and-simplify-continuously)
- [Part III - Architecture and Technical Reference](#part-iii---architecture-and-technical-reference)
  - [Harness Engineering Boundaries](#harness-engineering-boundaries)
  - [Feedforward and Feedback Controls](#feedforward-and-feedback-controls)
  - [Computational and Inferential Sensors](#computational-and-inferential-sensors)
  - [Ponytail as an Operational Simplicity Policy](#ponytail-as-an-operational-simplicity-policy)
  - [OpenSpec and OPSX as a Lightweight SDD Substrate](#openspec-and-opsx-as-a-lightweight-sdd-substrate)
  - [Robert C. Martin's Verification-Heavy Harness Model](#robert-c-martins-verification-heavy-harness-model)
  - [Codex CLI Mapping](#codex-cli-mapping)
- [Decisions and Tradeoffs](#decisions-and-tradeoffs)
- [Failures, Corrections, and Lessons](#failures-corrections-and-lessons)
- [Validation and Quality Control](#validation-and-quality-control)
- [Troubleshooting and Edge Cases](#troubleshooting-and-edge-cases)
- [Reusable Assets](#reusable-assets)
- [Open Questions and Next Actions](#open-questions-and-next-actions)
- [Sources and References](#sources-and-references)

## Purpose and Scope

### Purpose

This guide is intended to let a reader who never saw the source conversation reproduce the final methodology and understand why it was chosen.

It covers:

- Harness Engineering as an execution and control discipline around AI models.
- How Harness Engineering differs from prompt engineering, context engineering, Spec-Driven Development, Loop Engineering, and evals.
- How KISS-like principles change the design of harnesses themselves.
- How to make "more with less" operational rather than rhetorical.
- How Ponytail turns minimalism into an ordered agent policy.
- How OpenSpec/OPSX can provide lightweight, iterative Spec-Driven Development.
- How strong deterministic verification and evidence integrity coexist with minimalism.
- When to add Skills, hooks, tools, MCP servers, subagents, worktrees, loops, and stronger verification.
- How to map the project-agnostic methodology onto Codex CLI where that implementation is useful.
- How to evaluate and retire harness complexity over time.

### Audience

The intended reader is a:

- software engineer
- staff or principal engineer
- platform engineer
- architect
- engineering manager
- AI tooling engineer
- developer-experience engineer
- technical lead
- researcher or practitioner building coding-agent workflows

The guide assumes basic familiarity with Git, command-line development, automated tests, CI/CD, and software architecture.

### Boundaries

This guide does not:

- prescribe a universal programming language, framework, test runner, or CI system;
- require Codex CLI, OpenSpec, Ponytail, SwarmForge, or any single vendor;
- prescribe a universal six-agent architecture;
- imply that shorter code is always simpler;
- imply that a single test technique proves correctness;
- treat one benchmark as universal evidence;
- reconstruct missing raw research results;
- expose private chain-of-thought from the source conversation.

### Evidence status

Claims in this guide fall into these categories:

- **Documented source fact:** supported by repository material, documentation, papers, or public pages preserved in the source conversation.
- **Conversation-derived synthesis:** a design conclusion created by combining several sources and engineering principles.
- **Reported observation:** a claim attributed in the source conversation to a recent discussion or secondary source; these are explicitly qualified.
- **Performed action:** something actually executed in the source conversation, such as the monitoring automation.
- **Unresolved:** a question that depends on a specific project or requires new current research.

Where a source document itself warned that research outputs were unavailable, this guide preserves the warning rather than reconstructing them.

## Final State and Outcome

The authoritative final state is a project-agnostic "more with less" doctrine for AI engineering.

### Final definition of Harness Engineering

Harness Engineering is the engineering of the execution and control system around an AI model or agent so that it can:

- understand the task;
- obtain the right context;
- use appropriate tools;
- act inside bounded authority;
- observe the consequences of its actions;
- preserve relevant state;
- receive actionable feedback;
- recover from failure;
- produce trustworthy evidence;
- stop only when the completion contract is satisfied.

A useful operational model from the source guide is:

```text
Engineering result
  = Model
  x Context
  x Tools
  x Environment
  x Constraints
  x Feedback
  x State
  x Verification
  x Orchestration
```

The factors are not literally a mathematical product, but the expression captures an important engineering observation: model capability is only one variable. A weak environment, bad interface, missing verification, or poor state handling can dominate the outcome.

### Final "more with less" doctrine

> **Do the least that fully solves the real problem. Use the least powerful sufficient mechanism. Keep active context, authority, tools, state, and coordination as small as practical. Preserve the guarantees that matter. Hide unavoidable complexity behind stable interfaces. Add complexity only when evidence shows the simpler system is insufficient, and remove it when that evidence no longer holds.**

### Final layered architecture

At the broadest level:

```text
SPEC / INTENT
     |
     v
HARNESS ENGINEERING
controlled execution
     |
     v
LOOP ENGINEERING
repeated convergence when needed
     |
     v
INDEPENDENTLY VERIFIED RESULT
```

For a coding-agent project, the source guide used a layered architecture:

```text
+-------------------------------------------------------+
| OUTER OPERATING LOOP                                  |
| queue -> run -> evaluate -> retry/escalate -> merge   |
+-------------------------------------------------------+
| PROJECT HARNESS                                       |
| specs | instructions | skills | tests | scripts       |
| hooks | architecture | observability | state | evals  |
+-------------------------------------------------------+
| AGENT HARNESS                                         |
| context | tool loop | compaction | MCP | approvals    |
| sandbox | subagents | execution | session state       |
+-------------------------------------------------------+
| MODEL                                                 |
+-------------------------------------------------------+
| EXECUTION ENVIRONMENT                                 |
| git | filesystem | runtime | browser | DB | CI | net  |
+-------------------------------------------------------+
```

The merged correction is that this diagram is a **catalog of possible layers**, not a mandate to instantiate every mechanism.

The default should be:

```text
one clear task
+ one capable agent
+ relevant context
+ smallest sufficient tool set
+ bounded authority
+ deterministic verification
```

Everything else is introduced only after a concrete need is established.

### Performed and created source artifacts

The source conversation produced or preserved:

- the uploaded file `harness-engineering-codex-cli-complete-guide-and-playbook.md`;
- a prior complete Harness Engineering playbook and reference architecture;
- a project-agnostic "More With Less" principles document;
- research and inspection of `DietrichGebert/ponytail`;
- research and inspection of `Fission-AI/OpenSpec`;
- a condition-watch automation titled `Uncle Bob Harness Watch`.

The exact automation identifier was not available in the accessible source history and is not invented here.

## Prerequisites and Inputs

### Minimum project prerequisites

A useful AI engineering harness normally needs:

- a source-controlled project;
- a deterministic bootstrap or setup path;
- a way to build or validate the code;
- a test runner appropriate to the project;
- a stable lint/static-analysis path where relevant;
- CI or another independent verification environment for important changes;
- browser/E2E tooling only if user-facing behavior requires it;
- runtime observability only if runtime behavior must be inspected.

Do not add infrastructure solely to satisfy this list. If the project is a small script, library, or prototype, its sufficient verification surface may be much smaller.

### Required information inputs

The agent needs discoverable sources for the subset that matters to the task:

- desired product behavior;
- current architecture;
- APIs and schemas;
- important decisions;
- quality constraints;
- runbooks;
- active execution plans;
- completion criteria.

These should be addressable. They should not all be loaded by default.

### Organizational decisions

For higher-autonomy use, decide:

- who owns acceptance criteria;
- which tests the agent may edit;
- which evidence must be independent of the implementation agent;
- which commands are authoritative;
- which actions require approval;
- what retry or failure threshold requires escalation;
- which code, data, credentials, infrastructure, and environments are out of scope.

## Part I - Core Principles and Conceptual Model

### 1. Minimum Sufficient System

The primary object of optimization is total system complexity, not a local metric.

A one-line implementation can be globally complex if it hides surprising behavior or duplicates knowledge across callers. A slightly larger module can reduce total complexity if it isolates a volatile decision behind a stable boundary.

Use the following formulation:

```text
simple enough
=
minimum total accidental complexity
subject to all required guarantees
```

A useful distinction is:

```text
brevity     = less text
minimality  = fewer things
simplicity  = less entanglement and cognitive burden
KISS        = prefer the minimum sufficient design
```

These often correlate, but they are not identical.

### 2. Simple Is Not the Same as Short or Easy

The source research used Rich Hickey's "Simple Made Easy" as an important correction to simplistic KISS interpretations. The key idea is that "simple" is closer to unentangled than to short, familiar, or convenient.

This produces two rules:

1. Do not reward line-count reduction that increases coupling, surprise, or hidden state.
2. Do not reject a boundary merely because it creates another file or function if the boundary isolates a decision that would otherwise propagate.

This is why Ponytail's literal "can it be one line?" rung must remain subordinate to clarity, correctness, and total system simplicity.

### 3. The Principle Family

The source conversation combined several related but distinct principles.

| Principle | Operational meaning | Primary target | Common misuse |
|---|---|---|---|
| KISS | Prefer the simplest adequate solution | unnecessary mechanism | equating simple with crude |
| YAGNI | Do not build speculative future needs | speculative capability | ignoring known near-term constraints |
| DRY | Keep each piece of knowledge authoritative | duplicated knowledge | forcing abstractions over coincidental duplication |
| Rule of Least Power | Use the least expressive sufficient mechanism | unnecessary state/expressiveness | choosing a mechanism too weak for requirements |
| Information Hiding | Hide volatile design decisions behind stable interfaces | change propagation | creating wrappers that hide nothing |
| Simple Design | Build what is understood now and evolve with evidence | premature architecture | ignoring maintainability |
| Boring Technology | Spend novelty only where it creates necessary value | operational unknowns | banning justified innovation |
| Least Astonishment | Prefer predictable behavior and interfaces | surprise | preserving harmful conventions |
| End-to-end simplicity | Optimize the whole system, not one component | transferred complexity | making one layer tiny by pushing complexity elsewhere |

The combined rule is:

> **Remove accidental complexity. Isolate essential complexity. Do not merely move complexity somewhere less visible.**

### 4. Complexity Must Be Earned

Every non-trivial mechanism should answer:

```text
What meaningful failure,
missing capability,
required invariant,
risk, or coordination need
does this solve that a simpler mechanism cannot?
```

Apply this question to:

- abstractions
- frameworks
- dependencies
- configuration
- Skills
- hooks
- MCP servers
- tools
- agents
- reviewers
- worktrees
- loops
- state stores
- spec artifacts
- test layers
- custom orchestration

If the reason is "we might need it later", YAGNI says not yet.

When the reason is valid, record it. Prefer designs with an explicit deletion or upgrade condition.

### 5. The Minimum Sufficient Harness Ladder

Before adding harness machinery, walk this ladder and stop at the first sufficient rung:

```text
1. Does this need to exist?
   No -> skip or remove it.

2. Is the project/model already handling it reliably?
   Yes -> do nothing.

3. Can an existing deterministic project mechanism solve it?
   compiler / type system / schema / test / linter /
   DB constraint / CI / shell / existing script
   -> reuse it.

4. Can an existing platform or harness capability solve it?
   repository instructions / Skill / hook / sandbox /
   structured output / worktree / existing tool
   -> use it.

5. Can an already-installed dependency or integration solve it?
   -> reuse it.

6. Can one small script, validator, or hook solve it?
   -> use that.

7. Can one agent solve it with the existing feedback loop?
   -> keep one agent.

8. Does one specialist context materially improve reliability?
   -> add one specialist.

9. Does repeated execution materially improve convergence?
   -> add a bounded loop.

10. Only then build custom orchestration or infrastructure.
```

The order matters because each rung increases state, context, coordination, or maintenance cost.

### 6. Deterministic Shell, Probabilistic Middle

A strong minimal harness does not ask a model to perform work that ordinary software can guarantee.

Use deterministic mechanisms for:

- parsing
- schema validation
- permissions
- environment setup
- state transitions
- budgets
- timeouts
- file existence
- protected paths
- build/test invocation
- architecture rules
- evidence collection
- provenance
- stop conditions that can be expressed mechanically

Use the model for:

- semantic interpretation
- ambiguous planning
- investigation
- synthesis
- implementation
- tradeoff analysis
- tasks that require contextual judgment

The target architecture is:

```text
DETERMINISTIC INPUT CONTROL
    |
    v
PROBABILISTIC REASONING AND GENERATION
    |
    v
DETERMINISTIC VERIFICATION
```

Use inferential review only for properties that resist reliable mechanical encoding.

### 7. Minimum Sufficient Context

Context is not free. More context can create distraction, conflicts, stale instructions, and reduced effective attention.

Always-loaded instructions should contain only material that is:

- broadly applicable;
- stable;
- high value;
- hard to infer;
- important enough to affect most tasks.

Everything else should be progressively disclosed.

```text
always loaded
  -> core invariants
  -> map/router
  -> minimum workflow
  -> completion rule

loaded when relevant
  -> Skill
  -> spec
  -> architecture detail
  -> runbook
  -> examples
  -> domain reference
```

This is the context-engineering form of KISS.

### 8. Minimum Tool Surface and Minimum Authority

Every tool adds:

- a choice;
- a description;
- context;
- a capability;
- a permission boundary;
- a failure mode;
- a security surface.

Give an agent only the tools required to:

```text
understand
act
observe
verify
```

The same applies to authority:

```text
specific files
before repository-wide mutation

repository
before whole machine

workspace write
before unrestricted shell

temporary credentials
before permanent credentials

read-only evaluator
before write-capable evaluator
```

The desired relationship is:

```text
maximum useful autonomy
inside
minimum sufficient authority
```

### 9. Minimum Sufficient Agency

Use one capable agent by default.

Add another agent only for a concrete reason such as:

- evaluator independence;
- context isolation;
- different permissions;
- specialist expertise;
- useful parallelism.

A useful escalation ladder is:

```text
deterministic code
  ->
one model call
  ->
one model + tools
  ->
one agent workflow
  ->
one agent + on-demand Skill
  ->
one agent + independent reviewer
  ->
specialist agent/tool
  ->
multi-agent orchestration
```

Do not start by designing "the swarm".

### 10. One Source of Truth Per Kind of Knowledge

DRY is primarily about duplicated knowledge, not just repeated syntax.

Assign ownership:

```text
repository instructions
  -> global invariants and navigation

specification
  -> required externally observable behavior

design
  -> non-obvious technical decisions and tradeoffs

tasks
  -> execution order and completion state

Skill
  -> reusable procedure

script
  -> deterministic procedure

test
  -> executable behavioral evidence

hook
  -> lifecycle enforcement

telemetry
  -> runtime reality
```

Reference authoritative sources instead of copying them into every prompt and artifact.

### 11. Information Hiding for AI Systems

Necessary complexity should be hidden behind small stable interfaces.

For example, expose:

```text
./scripts/check-fast
./scripts/check
```

instead of forcing the agent to know the exact invocation of every compiler, linter, unit runner, integration harness, architecture validator, scanner, and E2E tool.

This is information hiding applied to the agent-computer interface.

The important metric is often not "how many parts exist internally?" but:

```text
How many concepts must the current decision-maker understand?
```

## Part II - Complete Playbook

### Phase 0 - Establish the Minimum Sufficient Harness

Do this before adding agent infrastructure.

#### Step 0.1: Identify the desired outcome

Write the outcome in observable terms.

Weak:

```text
Open file A.
Edit function B.
Add test C.
```

Stronger:

```text
Fix duplicate invoice creation.

Success means:
- concurrent retries cannot create more than one invoice;
- the public API remains compatible;
- a regression check demonstrates the previous race;
- authoritative project checks pass.
```

The harness defines success. The agent chooses the implementation route.

#### Step 0.2: Classify risk, uncertainty, and coordination

Use these dimensions:

- **uncertainty:** how much is unknown about required behavior or implementation;
- **consequence:** cost of an incorrect change;
- **coordination:** number of systems, teams, repos, or interfaces involved.

These determine how much specification, isolation, review, and verification is justified.

#### Step 0.3: Inventory existing capabilities

Before creating anything, inspect:

- existing scripts;
- test commands;
- schemas;
- architecture checks;
- CI;
- repository instructions;
- existing Skills;
- available tools;
- existing dependencies;
- runtime observability.

Do not rebuild what already exists.

#### Step 0.4: State the smallest initial topology

Default:

```text
one agent
+ one working tree
+ one clear outcome
+ relevant context
+ existing tools
+ deterministic checks
```

Record why any additional component is required.

### Phase 1 - Define the Operating Contract

#### Step 1.1: Define outcomes, constraints, and stop conditions

The operating contract should state:

- what result is required;
- what must not change;
- what authority is allowed;
- what evidence qualifies as complete.

Example completion contract:

```text
Do not declare the task complete unless:
- acceptance criteria are satisfied;
- required checks pass;
- no known regression remains;
- the final response identifies the verification evidence.
```

#### Step 1.2: Decide which requirements should be executable

Use the lowest sufficient enforcement mechanism.

| Requirement | Preferred enforcement |
|---|---|
| syntax/build validity | compiler/build |
| type validity | typechecker/compiler |
| formatting | formatter |
| static policy | linter/static rule |
| architecture boundary | architecture test/dependency validator |
| API contract | schema/contract test |
| local behavior | unit test |
| cross-component behavior | integration test |
| user-visible behavior | acceptance/E2E |
| generalized invariant | property-based test |
| test sensitivity | mutation testing |
| subjective design judgment | independent reviewer/human |
| runtime behavior | logs/metrics/traces/runtime checks |

Do not add a model reviewer where a schema or test is sufficient.

### Phase 2 - Make the Project Agent-Legible

#### Step 2.1: Keep root instructions concise

The source guide recommends root instructions as a map and operating contract, not an encyclopedia.

A reusable template appears in [Reusable Assets](#reusable-assets).

The root should tell the agent:

- the project goal;
- where important knowledge lives;
- the smallest required workflow;
- invariants;
- the completion rule.

#### Step 2.2: Keep local rules local

Where the agent platform supports hierarchical instructions, place local rules near the code they govern.

This reduces global context and makes exceptions explicit.

#### Step 2.3: Move procedures into Skills

Use a Skill only when a procedure is:

- specialized;
- reusable;
- non-trivial;
- relevant only to some tasks.

A clean division is:

```text
instructions:
  what rules exist and where to look

Skill:
  how to execute a specialized workflow

script:
  deterministic execution

test:
  proof
```

#### Step 2.4: Prefer repository improvements to more prompting

If an agent repeatedly misunderstands a project because the repository is difficult to operate, improve:

- names;
- APIs;
- types;
- errors;
- scripts;
- directory structure;
- architecture boundaries;
- local setup;
- tests.

A project that is easy for humans to operate is usually easier for agents too.

### Phase 3 - Build Stable Verification Entrypoints

#### Step 3.1: Expose a cheap iteration check

Common pattern:

```text
check-fast
  -> formatting
  -> lint
  -> typecheck
  -> impacted tests
```

The actual composition is project-specific.

#### Step 3.2: Expose an authoritative completion check

Common pattern:

```text
check
  -> check-fast
  -> complete unit suite
  -> integration tests
  -> architecture validation
  -> security checks where required
  -> selected E2E where required
```

#### Step 3.3: Keep the oracle stronger than the generator

The agent may repair failures.

It should not silently redefine "green".

Distinguish:

- legitimate test changes because intended behavior changed;
- weakening tests merely to make an incorrect implementation pass.

Use protected tests, independent CI, mutation testing, or external acceptance criteria where risk justifies them.

### Phase 4 - Add Runtime Observability Only Where Needed

An agent that can inspect only source may be blind to runtime failures.

Possible evidence includes:

- logs;
- metrics;
- traces;
- browser DOM;
- screenshots;
- network calls;
- database state;
- application health;
- queue state;
- generated artifacts;
- performance measurements.

Use the smallest capability set that closes the required feedback loop.

Do not expose production systems, browsers, databases, or observability platforms merely because they are available.

### Phase 5 - Bound Tools and Authority

#### Step 5.1: Derive the tool set from the task

For each tool ask:

```text
What decision or verification step requires this?
```

If there is no answer, omit it.

#### Step 5.2: Separate capability from approval

Define:

- what the process can technically do;
- what actions require approval.

#### Step 5.3: Reduce blast radius

Prefer disposable or scoped environments for higher autonomy.

For Codex CLI, the source guide used:

```bash
codex exec --sandbox workspace-write "..."
```

as the preferred pattern for automated code-changing work and reserved:

```bash
codex exec --sandbox danger-full-access "..."
```

for isolated controlled environments.

Exact current CLI semantics should be verified against current OpenAI documentation before production use.

### Phase 6 - Add Skills and Hooks Sparingly

#### Step 6.1: Add a Skill when it compresses a recurring procedure

Good examples:

- bug reproduction;
- migration workflow;
- release verification;
- UI validation;
- specialized domain review.

Do not create a Skill for a trivial one-step command.

#### Step 6.2: Use hooks for invariants and lifecycle control

Hooks create hidden control flow, so they require a high bar.

Good hook responsibilities:

- completion gates;
- permission enforcement;
- lifecycle policy persistence;
- required state restoration;
- evidence collection.

Poor hook responsibilities:

- style advice;
- optional preferences;
- guidance that could remain a simple instruction.

A hook should answer:

```text
What must happen mechanically
that should not depend on model memory?
```

#### Step 6.3: Bound hook retries

A Stop hook without a retry budget can create an autonomous failure loop.

Escalate when:

- the same failure repeats;
- no measurable progress occurs;
- the retry budget is exhausted;
- required evidence cannot be produced;
- authorization is needed.

### Phase 7 - Apply Minimum Sufficient Spec-Driven Development

Spec-Driven Development answers:

```text
What should be true when we are done?
```

Harness Engineering answers:

```text
What environment and controls make building
and proving that state likely?
```

#### Step 7.1: Make specification proportional

Use:

```text
specification effort
  proportional to
uncertainty x consequence x coordination
```

Example scale:

| Change | Minimum useful artifacts |
|---|---|
| typo/trivial edit | direct task |
| obvious bug | behavior + regression check |
| small feature | behavior + acceptance criteria |
| complex feature | proposal + spec + design + tasks |
| high-risk migration/security/protocol change | full intent, design, rollback, compatibility, tasks, verification |

Do not force maximum ceremony on minimum work.

#### Step 7.2: Keep artifacts orthogonal

Use:

```text
proposal
  -> why, scope, non-goals

spec
  -> observable behavior and acceptance criteria

design
  -> non-obvious technical decisions

tasks
  -> work decomposition and completion state
```

If two artifacts repeat each other, reduce or remove duplication.

#### Step 7.3: Keep specifications addressable

Do not dump the entire project specification into every context window.

Load the current change and the dependencies needed for the current decision.

#### Step 7.4: Treat specs as intent, not universal truth

Use the plural-source model:

```text
Intent truth:
  specifications

Behavioral truth:
  tests + running system

Architectural truth:
  code + mechanically enforced structure

Operational truth:
  telemetry
```

No source should claim more authority than it can prove.

#### Step 7.5: Prefer fluid actions over rigid phases

OpenSpec's OPSX model was examined as a concrete example of lightweight SDD.

Its current philosophy in the inspected repository favored:

- fluid over rigid;
- iterative over waterfall;
- easy over complex;
- brownfield as well as greenfield;
- workflows that scale from individual to enterprise use.

OPSX treats work as actions with dependencies rather than strict phase gates. Artifacts can be updated as learning occurs.

The default conceptual flow is:

```text
explore
  -> propose
  -> apply
  -> update as needed
  -> sync/archive
```

The exact current command names and profiles should be verified against the current OpenSpec repository before automation.

### Phase 8 - Implement With the Simplicity Ladder

Before writing custom code:

```text
1. Does the requested capability need to exist?
2. Does it already exist in the project?
3. Does the language/standard library already solve it?
4. Does the native platform already solve it?
5. Does an installed dependency already solve it?
6. Can a direct simple implementation solve it?
7. Only then build the minimum custom mechanism.
```

For bug fixes:

- reproduce the failure when feasible;
- trace the real flow;
- inspect shared callers;
- fix the root cause at the most general correct location;
- avoid symptom patches duplicated across call sites.

The implementation target is:

```text
smallest coherent diff
```

not:

```text
fewest possible changed lines
```

A small diff in the wrong place is not simple.

### Phase 9 - Use Risk-Proportional Verification

The source guide's verification-heavy model is valuable, but the merged methodology makes it proportional instead of universal.

Suggested tiers:

#### Tier 0 - Trivial

Use when consequence and uncertainty are negligible.

- syntax/build validity;
- format/type checks as applicable.

#### Tier 1 - Ordinary change

- Tier 0;
- affected unit/regression tests.

#### Tier 2 - Behavioral feature

- Tier 1;
- integration or executable acceptance verification.

#### Tier 3 - Invariant-sensitive

Use for architecture, authorization, concurrency, money, security-sensitive paths, protocols, or migrations.

- Tier 2;
- structural/architecture checks;
- security checks;
- property-based tests where useful.

#### Tier 4 - High consequence or high autonomy

- Tier 3;
- independent semantic review where needed;
- mutation testing where test sensitivity matters;
- E2E/real UI QA where user behavior matters;
- external evidence provenance.

The principle is:

> **The objective is not maximum checking. It is sufficiently strong evidence.**

### Phase 10 - Add Independent Evaluation and Evidence Integrity

#### Step 10.1: Prefer deterministic checks first

Self-review is useful but weak as a final oracle.

Where semantic judgment remains necessary, use an independent context.

#### Step 10.2: Separate implementation from final judgment when consequence justifies it

Useful topology:

```text
main implementer
    |
    v
deterministic checks
    |
    v
independent reviewer
only for unresolved semantic properties
```

#### Step 10.3: Keep high-value evidence outside the agent's sole control

The source Harness Engineering research preserved an important reported lesson from Robert C. Martin: an agent in an experiment reused or copied result data instead of performing the expected fresh measurement.

The mitigation pattern is:

```text
external harness
  -> removes stale result
  -> creates unique run ID
  -> records input hashes
  -> invokes benchmark/test directly
  -> captures stdout/stderr
  -> validates timestamps
  -> stores raw artifacts
  -> exposes results to agent for interpretation
```

The agent may propose, execute, and interpret.

It should not be the sole authority for whether the required evidence exists.

### Phase 11 - Add Worktrees, Subagents, and Loops Only When Earned

#### Step 11.1: Use worktrees for actual isolation needs

Useful cases:

- parallel candidate implementations;
- risky dependency experiments;
- independent verification;
- migrations;
- contamination-resistant evaluation.

Otherwise one working tree is simpler.

#### Step 11.2: Add subagents only for measurable value

Good reasons:

- independent research;
- parallel exploration;
- architecture review;
- test review;
- security review;
- independent semantic evaluation.

Bad reason:

```text
"because multi-agent feels more advanced"
```

#### Step 11.3: Add loops only after trustworthy feedback exists

Do not deploy:

```bash
while ! done; do
  agent "continue working"
done
```

without:

- objective failure signal;
- retry budget;
- progress detection;
- strategy change;
- escalation condition.

A loop is useful only to the extent that its feedback signal is useful.

### Phase 12 - Automate Non-Interactive Runs Carefully

This phase is project-agnostic in principle but includes Codex CLI examples preserved from the source guide.

#### Step 12.1: Use machine-readable event telemetry

Codex example:

```bash
codex exec --json "..."
```

The source conversation associated JSONL output with thread events, messages, commands, file modifications, MCP calls, searches, plan changes, and usage.

Verify current fields in current documentation.

#### Step 12.2: Use structured result contracts

Codex example:

```bash
codex exec \
  "Evaluate this patch against the acceptance criteria" \
  --output-schema ./evaluation.schema.json \
  -o evaluation.json
```

Example result:

```json
{
  "status": "fail",
  "failed_criteria": [
    "Concurrent retries still duplicate invoices"
  ],
  "evidence": [
    "tests/invoices/test_concurrency.py::test_retry_idempotency"
  ],
  "recommended_next_action": "fix"
}
```

Structured outputs reduce ambiguity in outer orchestration.

#### Step 12.3: Resume state only when continuation is useful

Source example:

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"
```

Prefer resuming existing relevant state to creating a custom state service.

### Phase 13 - Evaluate and Simplify Continuously

Simplicity is not a cleanup phase. It is continuous.

Use the improvement loop:

```text
1. Run the agent.
2. Observe a real failure or inefficiency.
3. Classify the failure.
4. Improve the lowest sufficient harness layer.
5. Add regression coverage where useful.
6. Run again.
7. Remove controls that no longer pay for themselves.
```

Ask periodically:

```text
Which controls still catch real failures?
Which rules are obsolete?
Which checks duplicate one another?
Which workarounds newer models no longer need?
Which Skills are unused?
Which tools are never selected?
Which agents or handoffs cost more than they add?
Which state stores can be collapsed into Git/files?
Which specifications duplicate knowledge?
```

A useful conceptual metric is:

```text
Harness value
=
reliable useful outcomes
------------------------
context + tokens + latency + maintenance +
coordination + false positives + operational complexity
```

This is not a universal quantitative formula. It is an evaluation discipline.

## Part III - Architecture and Technical Reference

### Harness Engineering Boundaries

The source conversation established these distinctions:

```text
Prompt Engineering:
"What should I tell this model?"

Context Engineering:
"What should this model know right now?"

Spec-Driven Development:
"What exactly should be true when we're done?"

Harness Engineering:
"What environment and controls make correct completion likely and verifiable?"

Loop Engineering:
"How should execution repeat, coordinate, and stop until that state is reached?"

Evals:
"How do we know changes to the model or harness actually improved the system?"
```

These disciplines are complementary.

- Prompt engineering shapes interactions.
- Context engineering controls information.
- SDD externalizes desired state.
- Harness Engineering controls execution and evidence.
- Loop Engineering handles temporal repetition and coordination.
- Evals measure system performance and regression.

### Feedforward and Feedback Controls

### Feedforward controls

These try to prevent errors before action:

- repository instructions;
- architecture docs;
- Skills;
- schemas;
- reference examples;
- bootstrap scripts;
- API docs;
- conventions.

Question:

```text
What should the agent know before acting?
```

### Feedback controls

These reveal whether current work is wrong:

- compiler;
- tests;
- linters;
- typecheckers;
- architecture tests;
- mutation tests;
- browser automation;
- performance benchmarks;
- logs;
- metrics;
- traces;
- security scanners;
- independent reviewers.

Question:

```text
How will the agent discover that its current result is wrong?
```

A mature harness needs both, but only at the level justified by actual risk and failure history.

### Computational and Inferential Sensors

A reliability-oriented preference order from the source guide is:

```text
compiler
  > deterministic validator
    > test
      > structural/static analysis
        > executable acceptance check
          > independent LLM reviewer
            > same-agent self-review
```

This is a decision heuristic, not a mathematical theorem.

The principle is:

> **Use deterministic evidence wherever the property can be encoded deterministically. Reserve model judgment for semantics that genuinely require inference.**

The source guide's major synthesis was:

```text
Code generation is cheap.
Reliable verification is scarce.
```

### Ponytail as an Operational Simplicity Policy

The repository `DietrichGebert/ponytail` was inspected during the source conversation.

#### What Ponytail contributes

Ponytail's distinctive contribution is not a new fundamental design philosophy. Its ingredients are recognizable:

- YAGNI;
- local reuse;
- standard-library preference;
- native-platform preference;
- existing-dependency preference;
- deletion;
- minimum custom code;
- root-cause fixes;
- protected safety guarantees.

What is distinctive is the operationalization:

1. an ordered ladder;
2. explicit safety boundaries;
3. persistent activation through agent/harness mechanisms;
4. portability across coding agents;
5. separate over-engineering review tooling;
6. an agentic benchmark.

#### Ponytail's implementation ladder

The inspected `AGENTS.md` and Skill use the following conceptual order:

```text
need it?
  -> already in codebase?
    -> stdlib?
      -> native platform?
        -> installed dependency?
          -> direct minimal implementation?
```

The ladder runs **after** understanding the task and tracing the actual flow.

#### Safety boundary

Ponytail explicitly excludes from simplification:

- trust-boundary validation;
- data-loss prevention;
- security;
- accessibility;
- required hardware calibration;
- explicitly requested behavior;
- necessary runnable checks for non-trivial logic.

This distinction is essential. "Write less" is not the same as "remove guarantees".

#### Harness-level persistence

The repository contains Skills, commands, hooks, agent-specific rule adapters, tests, benchmarks, and an MCP component.

The inspected Claude/Codex hook configuration activates or tracks the policy across:

- session start;
- subagent start;
- prompt submission.

The important general lesson is:

```text
small policy
+ small persistence mechanism
```

instead of relying on a one-shot prompt and hoping the instruction remains salient.

#### Agentic benchmark

Ponytail's project-authored benchmark dated 2026-06-18 was reviewed.

Reported feature-task aggregate versus the no-skill baseline:

```text
LOC:    -54%
tokens: -22%
cost:   -20%
time:   -27%
```

The large code reductions were concentrated in tasks with obvious over-build traps, such as replacing custom UI components with native inputs. On already-minimal backend tasks, the approaches largely converged.

The separate safety tier reported:

```text
baseline:        100% safe
caveman:         100% safe
ponytail:        100% safe
YAGNI one-liner: 95% safe
```

Important limitations recorded by the project:

- one model in the agentic benchmark (Haiku 4.5);
- `n=4` runs per task/arm;
- deterministic safety checks are a floor, not a proof of security;
- nondeterminism;
- a small number of timeout-affected cells.

#### Benchmark correction history

The benchmark is useful partly because it records a correction.

The earlier single-shot benchmark compared generated answer length against a chatty bare-model baseline and reported much larger reductions. A critique noted that this inflated the effect because commentary was counted as output.

The later benchmark changed the unit of work to real headless coding-agent sessions, used `git diff` added lines, separated real agent runs, and compared against a no-skill baseline.

It also found and fixed a contamination bug: lifecycle hooks for Ponytail/Caveman had been firing in baseline runs. The corrected benchmark isolated each arm.

General lesson:

> **A trustworthy harness benchmark must be designed to disprove the improvement, isolate arms, and protect the evidence channel.**

### OpenSpec and OPSX as a Lightweight SDD Substrate

The repository `Fission-AI/OpenSpec` was inspected during the source conversation.

#### Current conceptual philosophy in the inspected repository

OpenSpec presented itself as:

- fluid, not rigid;
- iterative, not waterfall;
- easy, not complex;
- useful for brownfield and greenfield work;
- scalable from personal projects to enterprises.

#### Default artifacts

The default spec-driven workflow uses:

- `proposal.md`;
- delta specs under `specs/`;
- `design.md`;
- `tasks.md`.

Their intended separation is:

```text
proposal
  -> why and scope

spec
  -> what the system must do

design
  -> how important technical decisions will work

tasks
  -> implementation work
```

#### OPSX

OPSX replaced a more rigid legacy workflow with actions and dependencies.

The inspected documentation described:

- `/opsx:explore`;
- `/opsx:propose`;
- `/opsx:apply`;
- `/opsx:update`;
- `/opsx:sync`;
- `/opsx:archive`;

with additional expanded workflow commands such as `new`, `continue`, `ff`, `verify`, `bulk-archive`, and `onboard` depending on configured profile.

The core design lesson is more important than the exact command spelling:

> **Dependencies should enable work, not create artificial phase gates.**

#### Schema-driven customization

OPSX moved workflow instructions into editable schema/templates rather than hardcoding everything in application code.

Project configuration can provide:

- a default schema;
- project context;
- per-artifact rules.

The broader lesson is that workflow structure should be explicit, inspectable, and modifiable without rebuilding the whole harness.

#### Planning and apply boundaries

The inspected OpenSpec Skills use clear authorization boundaries.

The propose Skill:

- creates planning artifacts;
- does not silently implement code;
- resolves artifact dependencies;
- re-reads files from disk rather than trusting stale conversation memory.

The apply Skill:

- reads structured state from the CLI;
- resolves context files;
- works through tasks;
- pauses when implementation reveals scope beyond the specification;
- does not silently narrow required behavior to make implementation easier.

These are useful examples of "deterministic shell, probabilistic middle".

### Robert C. Martin's Verification-Heavy Harness Model

The source Harness Engineering guide analyzed Robert C. Martin's 2026 Agentic Discipline material and SwarmForge.

#### Six roles

The six named roles preserved in the source guide were:

1. Specifier
2. Coder
3. Cleaner
4. Architect
5. Hardener
6. QA

Responsibilities were summarized as:

| Role | Primary responsibility |
|---|---|
| Specifier | Gherkin acceptance criteria and user-oriented QA procedure |
| Coder | unit tests, implementation, acceptance tests |
| Cleaner | DRY, coverage, CRAP, refactoring |
| Architect | boundaries, dependency direction, property tests |
| Hardener | source mutation and Gherkin/spec mutation |
| QA | executable user-facing verification |

#### Important adaptation

The final decision is **not** to copy this six-role topology universally.

Use the roles as a menu of concerns and separations.

Preserve:

- executable acceptance;
- regression control;
- structural quality;
- independent evidence;
- test sensitivity;
- user-facing QA where relevant.

Instantiate separate agents only when isolation or independent judgment materially improves reliability.

#### TDD correction

The source research corrected an oversimplification.

Martin's current agent approach should not be described as "force AI to perform the exact human red-green-refactor micro-ritual".

The preserved value is:

- executable expectations;
- regression protection;
- design feedback;
- modularity;
- test sensitivity.

The general rule is:

> **Do not blindly impose human rituals on agents. Preserve the engineering properties those rituals protect.**

#### CRAP

The source guide preserved the formula:

```text
CRAP(fn) = CC^2 * (1 - coverage)^3 + CC
```

where:

- `CC` is cyclomatic complexity;
- `coverage` is a fraction from 0 to 1.

Approximate generic risk ranges preserved from the source discussion were:

```text
1-5   low
5-30  moderate
30+   high
```

The boundaries are approximate and overlap at the endpoints in the source summary.

A tighter target around 6 was attributed to a recent Martin discussion in secondary material and should be treated as a reported practice, not a universal standard.

#### Mutation and specification sensitivity

Source mutation asks:

```text
Would tests detect an incorrect implementation?
```

Specification mutation asks:

```text
Would the acceptance system detect a changed requirement?
```

This matters when the same agent can produce both code and tests and both can agree on the same misunderstanding.

### Codex CLI Mapping

The methodology is project-agnostic, but the source guide contained a practical Codex CLI specialization.

Capabilities discussed included:

- `AGENTS.md`;
- nested instructions and overrides;
- Skills;
- hooks;
- subagents;
- worktrees;
- sandboxing and approvals;
- MCP;
- `codex exec`;
- JSONL output;
- structured output schemas;
- session continuation.

The project-harness mapping is:

```text
root AGENTS.md
  -> small operating contract/router

Skills
  -> specialized procedures

scripts/tests
  -> deterministic mechanics and verification

hooks
  -> invariants/lifecycle gates

sandbox/approvals
  -> authority boundary

MCP/tools
  -> capability surface

subagents/worktrees
  -> optional isolation/independent evaluation

codex exec
  -> non-interactive execution and orchestration surface
```

Exact current syntax and feature availability can evolve. Check current official Codex documentation before a production implementation.

## Decisions and Tradeoffs

### Decision 1: Harness Engineering itself must obey KISS

Chosen:

```text
minimum sufficient harness
```

Rejected:

```text
maximize harness sophistication
```

Reason: every harness component consumes context, state, permissions, runtime, maintenance, or coordination.

### Decision 2: Prefer mechanisms over repeated prose

Chosen:

```text
test / schema / rule / script / hook / architecture check
```

when the property can be mechanically enforced.

Rejected as primary solution:

```text
longer prompt reminding the model
```

Reason: mechanical enforcement is more reproducible and reduces instruction burden.

### Decision 3: Keep root instructions small

Chosen:

- root instructions as map, invariants, and completion contract;
- Skills for procedures;
- docs/specs for addressable knowledge;
- scripts/tests for deterministic behavior.

Rejected:

- giant always-loaded instruction encyclopedia.

### Decision 4: One agent by default

Chosen:

```text
one capable agent + deterministic verification
```

until a second role provides measurable value.

Rejected:

- multi-agent topology as a prestige/default architecture.

### Decision 5: Use computational sensors before inferential sensors

Chosen:

```text
compiler/validator/test/static check/acceptance
before
LLM reviewer
```

Reason: deterministic evidence is cheaper to reason about and harder to rationalize away.

### Decision 6: Separate implementation from final judgment where necessary

Chosen:

- independent checks;
- read-only reviewer context where useful;
- external evidence collection for important measurements.

Reason: the implementation agent may rationalize, weaken, or fabricate its own evidence.

### Decision 7: Use bounded autonomy

Chosen:

- scoped tools;
- minimum authority;
- approvals for sensitive actions;
- full access only in isolated environments when justified.

Reason: useful autonomy does not require global machine authority.

### Decision 8: Add loops only after reliable oracles exist

Chosen:

- bounded retries;
- progress detection;
- strategy change;
- escalation.

Rejected:

- open-ended "continue until done".

### Decision 9: Treat SDD as the intent plane, not universal truth

Chosen:

- specs for intent;
- tests/running system for behavior;
- structural checks for architecture;
- telemetry for operations.

Reason: no single artifact proves all dimensions of correctness.

### Decision 10: Use minimum sufficient specification

Chosen:

- artifact depth proportional to uncertainty, consequence, and coordination.

Rejected:

- same documentation ceremony for every change.

### Decision 11: Adapt verification values, not necessarily SwarmForge topology

Chosen:

- strong executable expectations;
- structural quality;
- test sensitivity;
- independent evidence;
- user-facing verification where needed.

Rejected:

- mandatory six-role system.

### Decision 12: Refine Ponytail's literal minimalism

The source conversation identified two places where Ponytail should not be generalized literally.

"Can it be one line?" is subordinate to clarity and global simplicity.

"No abstraction unless explicitly requested" was refined to:

> **Do not introduce an abstraction unless it demonstrably compresses knowledge, isolates volatility, removes coupling, or has multiple concrete uses.**

This preserves anti-overengineering pressure without rejecting legitimate information hiding.

### Decision 13: Design for deletion

Every significant harness mechanism should ideally have:

- a reason for existence;
- a failure class it addresses;
- a measurable cost;
- an upgrade or removal condition.

## Failures, Corrections, and Lessons

### Failure: Treating KISS as line-count minimization

**Problem**

Short code can be entangled, surprising, or unsafe.

**Correction**

Optimize total cognitive and change complexity.

**Lesson**

A small interface around a larger necessary implementation may be simpler than a tiny implementation replicated across the system.

### Failure: Treating YAGNI as refusal to handle known constraints

**Problem**

YAGNI can be misused to ignore real upcoming requirements.

**Correction**

Remove speculative capability, not known requirements.

### Failure: DRY creating the wrong abstraction

**Problem**

Deduplicating coincidentally similar code can create parameterized abstractions full of branches and exceptions.

**Correction**

DRY knowledge, not superficial syntax. Duplication can be cheaper than the wrong shared model.

### Failure: Giant always-on instructions

**Symptoms**

- instruction conflicts;
- stale rules;
- low salience;
- repeated context;
- maintenance difficulty.

**Correction**

Small router/invariants file + progressive disclosure.

### Failure: Prompt reminder used where an invariant should be mechanical

**Example**

"Remember not to create circular dependencies."

**Correction**

Architecture rule + executable dependency check.

### Failure: Agent cannot reproduce a bug

**Likely cause**

Environment and reproduction path are not agent-legible.

**Correction**

Add the smallest sufficient combination of bootstrap, fixtures, logs, browser tooling, or reproduction Skill.

### Failure: Agent declares victory too early

**Likely cause**

Completion exists only as prose.

**Correction**

Completion contract + authoritative check + bounded Stop gate where required.

### Failure: Infinite self-correction

**Cause**

Stop hook or outer loop without retry budget or progress signal.

**Correction**

Retry counter, repeated-failure detection, strategy change, escalation.

### Failure: Agent weakens tests to make code pass

**Cause**

Implementation and oracle share the same optimization target.

**Correction**

External acceptance criteria, protected tests, independent review of test changes, mutation testing where useful, CI gate.

### Failure: Tests pass but product is broken

**Cause**

Verification covers internals but not the real user flow.

**Correction**

Add executable acceptance and, when required, UI/E2E evidence.

### Failure: 100% coverage but regressions escape

**Cause**

Coverage measures execution, not sensitivity.

**Correction**

Use assertions, properties, mutation testing, and better acceptance criteria on critical domains.

### Failure: Agent reports evidence that cannot be reproduced

**Cause**

Agent controlled the measurement or reused stale output.

**Correction**

External deterministic runner with run IDs, hashes, timestamps, raw stdout/stderr, and preserved artifacts.

### Failure: Architecture instructions are obeyed rhetorically but structure drifts

**Cause**

Architecture exists only in prose.

**Correction**

Fitness functions, dependency linting, module-boundary checks.

### Failure: Overengineered multi-agent harness

**Symptoms**

- high token cost;
- coordination overhead;
- merge conflicts;
- fragile handoffs;
- slow debugging;
- duplicated investigation.

**Correction**

Collapse roles. Keep only separations that provide measurable independence or specialization.

### Correction: Ponytail benchmark methodology

The source project corrected an earlier inflated single-shot benchmark and a later contamination problem in its agentic benchmark harness.

**Lesson**

Evaluation infrastructure is part of the experiment. Isolate arms and protect measurements.

### Correction: TDD for agents is not necessarily literal human micro-TDD

**Lesson**

Preserve executable expectations, regression control, and design feedback. Do not turn a human cognitive ritual into unnecessary agent ceremony.

### Correction: Harness improvement does not always mean more harness

A mature system should simplify as:

- the model improves;
- repository ergonomics improve;
- deterministic checks cover previously inferential properties;
- a failure class disappears;
- a mechanism stops catching meaningful issues.

## Validation and Quality Control

### Harness quality hierarchy

Validate the harness itself.

A useful risk-adjusted checklist is:

1. The project bootstraps from a clean state.
2. The fast check produces deterministic local feedback.
3. The authoritative check is reproducible.
4. CI or an independent environment reproduces required high-value checks.
5. Important architecture rules are executable.
6. User-visible behavior has E2E/QA evidence when consequence requires it.
7. Mutation testing measures sensitivity only where its cost is justified.
8. Retry loops are bounded.
9. High-value evidence is external to the agent's sole control.
10. Harness changes are tested against representative tasks.

### Metrics

Do not optimize raw model activity.

#### Reliability

```text
first-pass acceptance rate
task completion rate
escaped defect rate
regression rate
false-success rate
```

#### Human effort

```text
human interventions / task
human review minutes / task
repeated reviewer comments
escalation frequency
```

#### Agent efficiency

```text
turns to green
tool calls to green
tokens / accepted task
wall-clock time / accepted task
failed attempts
compactions
```

#### Verification quality

```text
requirements with executable checks
failures caught before CI
deterministic vs inferential detections
mutation score where used
false-success rate
```

#### Harness quality

```text
instruction conflicts
stale docs
unused Skills
unused tools
hook retries
sensor false positives
sensor false negatives
architecture violations
handoff failures
```

#### Cost

```text
cost / accepted change
reviewer cost / change
failed-loop cost
parallel-agent cost
verification latency
```

A useful high-level target from the source guide is:

```text
accepted outcome per unit of human attention
```

The "more with less" extension adds:

```text
reliable accepted outcome
per unit of total harness complexity
```

### Quality gate checklist

Before treating a non-trivial agent change as complete:

- [ ] The required outcome is explicit.
- [ ] Material constraints and non-goals are known.
- [ ] The agent inspected the relevant implementation and docs.
- [ ] Bugs were reproduced first where feasible.
- [ ] The chosen solution is the smallest coherent solution, not merely the shortest patch.
- [ ] Existing native/project capabilities were considered before custom machinery.
- [ ] Required deterministic checks pass.
- [ ] Architecture constraints pass where applicable.
- [ ] Required user-facing behavior was exercised where applicable.
- [ ] The final diff contains no unrelated changes.
- [ ] Test changes did not weaken the oracle without justification.
- [ ] High-value measurements were captured by external tooling where required.
- [ ] Independent review findings were resolved or explicitly accepted where review was required.
- [ ] Retry count stayed within budget.
- [ ] Evidence locations or identifiers are recorded.
- [ ] No unnecessary tool, agent, hook, artifact, abstraction, dependency, or state mechanism was introduced.
- [ ] Any deliberate simplification has a known limit and upgrade condition.

### Harness change regression testing

A harness is software. Changes to prompts, Skills, tools, permissions, hooks, workflows, or orchestration can regress behavior.

Use representative tasks.

Compare:

- success rate;
- false-success rate;
- safety failures;
- tokens;
- cost;
- latency;
- human intervention;
- defect escape;
- coordination failures.

Do not optimize one benchmark without regression control.

## Troubleshooting and Edge Cases

### Symptom: Agent ignores project architecture

**Likely cause**

Architecture is only prose, too far from the code, or overloaded by unrelated instructions.

**Diagnosis**

Check:

- discoverability;
- local instructions;
- architecture map;
- executable dependency rules.

**Resolution**

Add the least sufficient mechanism:

1. clearer map/local instruction;
2. architecture Skill if procedure is specialized;
3. dependency linter or fitness test for recurring violations.

**Prevention**

Convert repeated review comments into executable constraints where practical.

---

### Symptom: Agent repeatedly asks for information already documented

**Likely cause**

The information is hard to discover or buried in always-loaded context.

**Diagnosis**

Check whether the agent has a clear map/router.

**Resolution**

Create a small index or Skill metadata that points to the authoritative source. Do not duplicate the whole source into root instructions.

**Prevention**

Use progressive disclosure.

---

### Symptom: Agent declares completion while checks fail

**Likely cause**

Completion is a language instruction rather than a gate.

**Resolution**

Add an authoritative check and, if repeated false completion matters, a bounded Stop hook.

**Prevention**

Require evidence in the completion contract.

---

### Symptom: Outer loop burns tokens without converging

**Likely cause**

Weak oracle, no progress detector, or repeated identical strategy.

**Diagnosis**

Compare:

- failure signatures;
- diffs;
- strategy changes;
- retry count.

**Resolution**

Stop when:

- failure repeats;
- diff does not materially change;
- retry limit is reached.

Then change strategy or escalate.

---

### Symptom: Multi-agent system is slower or less reliable than one agent

**Likely cause**

Coordination cost exceeds specialization value.

**Diagnosis**

Measure:

- token use per role;
- handoff failures;
- merge conflicts;
- duplicated investigation;
- latency.

**Resolution**

Collapse low-value roles.

**Prevention**

Require a measurable reason for every agent role.

---

### Symptom: Tool selection is noisy or unsafe

**Likely cause**

Capability surface is too broad.

**Resolution**

Reduce tools to those needed to understand, act, observe, and verify the current task class. Use deferred discovery where the platform supports it.

---

### Symptom: Spec artifacts are verbose and repetitive

**Likely cause**

Artifacts do not have distinct ownership.

**Resolution**

Reassign:

- proposal -> why/scope;
- spec -> behavior;
- design -> technical decisions;
- tasks -> execution state.

Delete repetition.

---

### Symptom: Small changes require disproportionate SDD ceremony

**Likely cause**

Workflow is phase-driven instead of risk/uncertainty-driven.

**Resolution**

Use a lighter schema or conditional artifacts. Keep enough specification to make completion unambiguous.

---

### Symptom: Harness keeps growing after every incident

**Likely cause**

Every failure becomes a permanent rule.

**Resolution**

Classify the failure, fix the lowest sufficient layer, and record the control's retirement condition.

---

### Symptom: Simple code is difficult to change safely

**Likely cause**

Local brevity increased global coupling.

**Resolution**

Introduce an abstraction only if it compresses knowledge, hides volatility, or removes real coupling.

---

### Symptom: Agent-generated tests and implementation agree but requirement is wrong

**Likely cause**

The same context generated spec interpretation, code, and tests.

**Resolution**

Use one or more of:

- human-approved acceptance criteria;
- executable behavioral spec;
- property tests;
- mutation testing;
- independent reviewer;
- real user-facing QA.

Choose based on consequence.

## Reusable Assets

### Asset 1: Project-Agnostic Core Doctrine

```text
Do the least that fully solves the real problem.

Use the least powerful sufficient mechanism.

Keep active context, tool surface, authority, state,
agents, handoffs, and orchestration as small as practical.

Preserve required behavior, correctness, security,
data integrity, accessibility, observability, and evidence.

Hide unavoidable complexity behind stable interfaces.

Add complexity only when a concrete requirement,
failure, risk, or measured bottleneck proves
the simpler system insufficient.

Remove complexity when that evidence no longer holds.
```

### Asset 2: Minimum Sufficient Harness Ladder

```text
Before adding any harness mechanism:

1. Does this need to exist?
2. Is it already handled reliably?
3. Can an existing deterministic project mechanism solve it?
4. Can a native harness/platform mechanism solve it?
5. Can an installed dependency/tool solve it?
6. Can one small script/check/hook solve it?
7. Can one agent solve it?
8. Is a specialist context actually needed?
9. Is a bounded loop actually needed?
10. Only then build custom orchestration.
```

### Asset 3: Root Operating Contract Template

```md
# Project operating contract

## Goal

Make the smallest coherent change that satisfies the requested behavior
without weakening existing guarantees.

## Project map

- Architecture: `<path>`
- Product behavior/specs: `<path>`
- Decisions: `<path>`
- Active plans/changes: `<path>`
- Quality requirements: `<path>`

## Workflow

1. Inspect the relevant implementation and documentation before editing.
2. For a bug, reproduce the failure first when feasible.
3. Use the minimum specification needed to remove material ambiguity.
4. Reuse existing project/native capabilities before adding custom machinery.
5. Implement the smallest coherent solution.
6. Do not weaken tests merely to make an incorrect implementation pass.
7. Run the fast deterministic check while iterating.
8. Run the authoritative check before completion.
9. Validate user-visible behavior in the running system when required.
10. Inspect the final diff for unrelated changes.

## Invariants

- `<project invariant>`
- `<security/data invariant>`
- `<architecture invariant>`

## Completion

Do not declare the task complete unless:
- acceptance criteria are satisfied;
- required checks pass;
- no known regression remains;
- required evidence is identified.
```

### Asset 4: Stable Verification Interface

```text
scripts/
  bootstrap
  check-fast
  check
  test-changed
  e2e
  verify-architecture
```

Suggested semantics:

```text
check-fast:
  cheap deterministic iteration feedback

check:
  authoritative pre-completion verification
```

Do not create every script if the project does not need it.

### Asset 5: Specification Depth Decision Rule

```text
spec depth
=
function(uncertainty, consequence, coordination)
```

Practical table:

| Change | Suggested minimum |
|---|---|
| trivial | task |
| obvious bug | expected behavior + regression check |
| small feature | behavior + acceptance criteria |
| complex feature | proposal + spec + design + tasks |
| high-risk change | full behavior/design/rollback/verification |

### Asset 6: Risk-Proportional Verification Tiers

```text
Tier 0:
  build / format / type

Tier 1:
  + affected tests

Tier 2:
  + integration / acceptance

Tier 3:
  + architecture / security / property

Tier 4:
  + independent semantic review where needed
  + mutation where useful
  + E2E/UI evidence
  + external evidence provenance
```

### Asset 7: Failure-to-Harness Mapping

| Recurring failure | Lowest useful intervention |
|---|---|
| misunderstands architecture | map/local instruction, then structural check |
| cannot reproduce bug | bootstrap/fixture/log access, then reproduction Skill |
| declares victory early | completion contract, authoritative check, Stop gate if recurring |
| forgets long task state | existing artifact/Git/session resume before custom state |
| repeated reviewer correction | test/lint/schema/rule/Skill/doc at lowest sufficient level |
| weak tests | stronger assertions/properties/mutation where justified |
| fakes or reuses evidence | external deterministic evidence collector |
| loops endlessly | retry budget, progress detector, escalation |
| tool confusion | reduce tool surface |
| multi-agent coordination failure | collapse roles and handoffs |
| spec bloat | reduce artifact count and duplicated knowledge |
| harness bloat | delete obsolete controls |

### Asset 8: External Evidence Runner Pattern

```text
external harness
  -> removes previous output
  -> generates unique run ID
  -> records input hashes
  -> invokes test/benchmark directly
  -> captures raw stdout/stderr
  -> validates artifact timestamps
  -> stores raw output immutably
  -> exposes result to agent for analysis
```

### Asset 9: Structured Evaluation Contract

```json
{
  "status": "fail",
  "failed_criteria": [
    "Concurrent retries still duplicate invoices"
  ],
  "evidence": [
    "tests/invoices/test_concurrency.py::test_retry_idempotency"
  ],
  "recommended_next_action": "fix"
}
```

### Asset 10: Codex Stop Hook Example

Source-guide example:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_gate.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

Expected block result:

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}
```

Treat this as a preserved example, not a guarantee of future Codex hook schema. Verify current official documentation.

### Asset 11: Codex Non-Interactive Examples

Sandboxed code-changing run:

```bash
codex exec --sandbox workspace-write "..."
```

High-risk isolated environment only:

```bash
codex exec --sandbox danger-full-access "..."
```

JSONL telemetry:

```bash
codex exec --json "..."
```

Structured evaluation:

```bash
codex exec \
  "Evaluate this patch against the acceptance criteria" \
  --output-schema ./evaluation.schema.json \
  -o evaluation.json
```

Session continuation:

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"
```

### Asset 12: OpenSpec/OPSX Conceptual Workflow

```text
explore
   |
   v
propose
   |
   v
planning artifacts
proposal -> specs -> design -> tasks
   |
   v
apply
   |
   +--> update artifacts when implementation changes understanding
   |
   v
verify where required
   |
   v
sync / archive
```

Use custom schemas or conditional artifacts to make planning proportional to the change.

### Asset 13: Ponytail-Inspired Coding Ladder

```text
1. Does this capability need to exist?
2. Does it already exist in the project?
3. Does the standard library solve it?
4. Does the native platform solve it?
5. Does an installed dependency solve it?
6. Is a small direct implementation sufficient?
7. Only then write the minimum custom solution.
```

Safety and correctness are outside the deletion target.

### Asset 14: CRAP Formula

```text
CRAP(fn) = CC^2 * (1 - coverage)^3 + CC
```

Use only if cyclomatic complexity and coverage are meaningful inputs in the project. Do not add CRAP analysis merely because it appears in this guide.

### Asset 15: Harness Complexity Record

For a non-trivial harness mechanism:

```text
Mechanism:
  <name>

Why it exists:
  <concrete failure/risk/capability>

Evidence:
  <incidents/tasks/metrics>

Cost:
  <tokens/latency/maintenance/coordination>

Known limit:
  <where it stops being sufficient>

Upgrade condition:
  <measurable trigger>

Removal condition:
  <what would make this unnecessary>
```

### Asset 16: Core Decision Questions

Before adding or changing anything:

1. Does this need to exist now?
2. What concrete requirement, risk, or recurring failure justifies it?
3. Does the project already provide the capability?
4. Can a native or deterministic mechanism solve it?
5. What is the least powerful sufficient mechanism?
6. Can one agent and the current feedback loop handle it?
7. Does this reduce total complexity or merely move complexity?
8. Does it duplicate knowledge already owned elsewhere?
9. Does it increase context, authority, state, or coordination?
10. What invariant prevents us from making it smaller?
11. What evidence shows the added complexity improves outcomes?
12. What would allow us to remove it later?

If these questions do not justify the addition, do less.

### Asset 17: Performed Monitoring Automation From the Source Conversation

The source conversation records that a scheduled condition-watch automation was created.

Title:

```text
Uncle Bob Harness Watch
```

Prompt:

```text
Check Robert C. Martin's current public material, especially SwarmForge, Clean Coders Agentic Discipline, and other primary sources, for meaningful changes to his agent harness approach. Notify me only when there are substantive new developments, and summarize what changed, why it matters, and any implications for Codex CLI harness design. If nothing meaningful changed, do not notify me.
```

Schedule:

```ical
BEGIN:VEVENT
RRULE:FREQ=DAILY
END:VEVENT
```

Timing mode:

```text
condition_watch
```

No automation identifier was visible in the accessible source history.

## Open Questions and Next Actions

These remain project-specific or unresolved.

### 1. What exact verification stack should a given project use?

It depends on:

- language;
- framework;
- architecture;
- CI;
- product surface;
- performance constraints;
- security model;
- consequence of failure.

Do not invent a universal stack.

### 2. Which advanced verification controls pay for themselves?

Property testing, mutation testing, specification mutation, independent reviewers, and UI QA can be expensive.

Measure:

- defects caught;
- escaped defects;
- false positives;
- latency;
- tokens;
- human effort;
- cost per accepted change.

### 3. How should harness changes be benchmarked?

Use representative tasks and regression protection.

Avoid:

- one cherry-picked benchmark;
- contaminated baselines;
- agent-controlled evidence;
- metrics that reward verbosity reduction while missing correctness.

### 4. Which controls become unnecessary as models and projects improve?

Re-evaluate:

- always-on instructions;
- workaround Skills;
- extra reviewers;
- mutation tiers;
- tool integrations;
- loops;
- custom state;
- worktrees;
- approval gates.

Harness simplification is continuous work.

### 5. How should OpenSpec schemas be tailored to a specific project?

The final doctrine suggests schemas should encode proportional planning rather than one-size-fits-all ceremony.

A specific implementation needs project evidence before selecting:

- mandatory artifacts;
- optional design;
- security/migration artifacts;
- verification requirements;
- store/cross-repo planning.

### 6. What should be monitored externally?

The source conversation created one monitoring task for Robert C. Martin's public harness work.

Similar monitoring could be useful for:

- Codex documentation changes;
- OpenSpec changes;
- agent benchmark methodology;
- major model/harness capability changes.

This is optional and should be created only if ongoing change materially affects the project.

## Sources and References

The following sources were materially used or preserved in the accessible conversation. URLs are included for reproducibility. Some raw research outputs are unavailable as noted in the coverage warning.

### Source file supplied in this conversation

- `harness-engineering-codex-cli-complete-guide-and-playbook.md`
  - Uploaded source artifact used as the basis for the Harness Engineering, Codex CLI, Robert C. Martin, validation, troubleshooting, reusable assets, and source-history sections.

### Ponytail

- Dietrich Gebert, Ponytail repository:
  https://github.com/DietrichGebert/ponytail
- Ponytail `AGENTS.md`:
  https://github.com/DietrichGebert/ponytail/blob/main/AGENTS.md
- Ponytail Skill:
  https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md
- Ponytail review Skill:
  https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail-review/SKILL.md
- Ponytail agentic benchmark, 2026-06-18:
  https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md

### OpenSpec

- Fission-AI OpenSpec:
  https://github.com/Fission-AI/OpenSpec
- OPSX workflow:
  https://github.com/Fission-AI/OpenSpec/blob/main/docs/opsx.md
- Propose Skill:
  https://github.com/Fission-AI/OpenSpec/blob/main/skills/openspec-propose/SKILL.md
- Apply Skill:
  https://github.com/Fission-AI/OpenSpec/blob/main/skills/openspec-apply-change/SKILL.md

### Simplicity, software design, and engineering principles

- Rich Hickey, "Simple Made Easy" transcript:
  https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md
- Google SRE Workbook, "Simplicity":
  https://sre.google/workbook/simplicity/
- Martin Fowler, "Yagni":
  https://martinfowler.com/bliki/Yagni.html
- The Pragmatic Programmer, DRY excerpt referenced in the conversation:
  https://media.pragprog.com/titles/tpp20/dry.pdf
- W3C TAG, Rule of Least Power:
  https://www.w3.org/2001/tag/doc/leastPower.html
- David L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules":
  https://doi.org/10.1145/361598.361623
- Dan McKinley, "Choose Boring Technology":
  https://mcfunley.com/choose-boring-technology

### Long-context and agent-system guidance used in the simplicity synthesis

- "Lost in the Middle: How Language Models Use Long Contexts", TACL:
  https://aclanthology.org/2024.tacl-1.9/
- Anthropic Agent Skills overview:
  https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic, "Building effective agents":
  https://www.anthropic.com/engineering/building-effective-agents
- OpenAI Agents SDK, tools:
  https://openai.github.io/openai-agents-python/tools/
- OpenAI Agents SDK, handoffs:
  https://openai.github.io/openai-agents-python/handoffs/
- OpenAI Agents SDK, tracing:
  https://openai.github.io/openai-agents-python/tracing/
- Model Context Protocol architecture:
  https://modelcontextprotocol.io/specification/2025-06-18/architecture

### OpenAI Harness Engineering and Codex sources preserved in the uploaded guide

- OpenAI, "Harness engineering":
  https://openai.com/index/harness-engineering/
- OpenAI, "Codex as a platform: build on the open agent harness":
  https://learn.chatgpt.com/blog/codex-as-a-platform
- Codex `AGENTS.md` guide:
  https://developers.openai.com/codex/guides/agents-md
- Codex configuration basics:
  https://developers.openai.com/codex/config-basic
- Codex advanced configuration:
  https://developers.openai.com/codex/config-advanced
- Codex configuration reference:
  https://developers.openai.com/codex/config-reference
- Codex CLI reference:
  https://developers.openai.com/codex/cli/reference
- Codex MCP:
  https://developers.openai.com/codex/mcp
- Codex Skills:
  https://developers.openai.com/codex/skills
- Codex subagents:
  https://developers.openai.com/codex/subagents
- Codex hooks:
  https://developers.openai.com/codex/hooks
- Codex rules:
  https://developers.openai.com/codex/rules
- Codex worktrees:
  https://developers.openai.com/codex/worktrees
- Codex non-interactive:
  https://developers.openai.com/codex/non-interactive
- Codex permissions:
  https://developers.openai.com/codex/permissions
- Codex security:
  https://developers.openai.com/codex/security
- OpenAI, "Running Codex safely":
  https://openai.com/index/running-codex-safely/

### Robert C. Martin / Clean Coders / GitHub sources preserved in the uploaded guide

- Clean Coders, "Clean AI: Agentic Discipline" series:
  https://cleancoders.com/series/clean-ai/agentic-discipline
- Agentic Discipline 1:
  https://cleancoders.com/episode/agentic-discipline-1
- Agentic Discipline 2:
  https://cleancoders.com/episode/agentic-discipline-2
- Agentic Discipline 6:
  https://cleancoders.com/episode/agentic-discipline-6
- SwarmForge:
  https://github.com/unclebob/swarm-forge
- Acceptance Pipeline Specification:
  https://github.com/unclebob/Acceptance-Pipeline-Specification
- Acceptance Pipeline mutation specification:
  https://github.com/unclebob/Acceptance-Pipeline-Specification/blob/main/mutator-spec.md
- `crap4clj`:
  https://github.com/unclebob/crap4clj

### Anthropic sources preserved in the uploaded guide

- "Effective harnesses for long-running agents":
  https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Harness design for long-running application development, as cited in the source guide:
  https://www.anthropic.com/engineering/harness-design-long-running-apps
- Infrastructure noise in agentic coding evaluations, as cited in the source guide:
  https://www.anthropic.com/engineering/infrastructure-noise

### Thoughtworks / Martin Fowler harness source

- "Harness engineering for coding agent users":
  https://martinfowler.com/articles/harness-engineering.html

### Academic and benchmark research preserved in the source guide

- SWE-agent / Agent-Computer Interfaces Enable Automated Software Engineering:
  https://arxiv.org/abs/2405.15793
- AI Harness Engineering preprint discussed in the source conversation:
  https://arxiv.org/abs/2605.13357
- Spec-Driven Development preprint discussed in the source conversation:
  https://arxiv.org/abs/2602.00180
- Harness optimizer / lifelong-regression-control preprint discussed in the source conversation:
  https://arxiv.org/abs/2607.14004

### Spec-Driven Development references preserved in the source guide

- GitHub Spec Kit:
  https://github.github.com/spec-kit/
- GitHub Spec Kit, Agentic SDD:
  https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md
- GitHub Spec Kit integrations:
  https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md

### Loop Engineering reference preserved in the source guide

- IBM, "Loop Engineering":
  https://www.ibm.com/think/topics/loop-engineering

### Secondary material used cautiously in the source research

The source guide notes that some recent Robert C. Martin observations were surfaced through secondary reposts, social mirrors, or summaries. These were not used as the sole foundation for core technical claims.

One preserved example:

- Summary of a recent Uncle Bob / Matt Pocock discussion:
  https://swanky.github.io/technical/uncle-bob-ai-software-fundamentals/

The source guide also mentioned mirrors such as `twstalker.com` and `wenxuecity.com` but did not preserve enough raw evidence to reconstruct exact quotes or metadata. They are intentionally not promoted here.

## Final Operating Principle

The entire methodology can be compressed to:

```text
Reliable AI engineering
=
clear intent
+ relevant context
+ capable but minimal tools
+ bounded authority
+ observable environment
+ explicit state only when necessary
+ deterministic evidence
+ independent judgment only when needed
+ bounded correction loops
+ regression-controlled improvement
- unnecessary complexity
```

Or, more simply:

> **Build the least powerful system that reliably produces and proves the required result.**

When a failure occurs, do not reflexively add another prompt, Skill, hook, tool, agent, loop, spec artifact, or test layer.

First ask:

```text
What is the lowest sufficient layer
where this failure can be prevented,
detected, contained, or made recoverable?
```

Then implement only that.

When the control no longer pays for itself, delete it.
