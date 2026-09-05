# Skill Kit - Full Branding and Launch Plan

## 1. Executive direction

### Brand idea

**Skill Kit gives coding agents better working methods.**

It is a cross-agent collection of installable skills and workflow plugins for developers using Claude Code, Codex, and Copilot CLI. The collection covers engineering discipline, specification, release work, and writing, ranging from lightweight reusable instructions to stricter plugins with hooks, verification gates, and specialist roles.

The brand should not present Skill Kit as:

- a prompt library;
- a giant agent framework;
- another autonomous coding system;
- a collection of random personal prompts;
- an "AI productivity" bundle.

The strongest territory is narrower:

> **Reusable working methods for coding agents.**

The attached playbook correctly treats repository branding as alignment between product truth, positioning, identity, README, proof, and distribution rather than logo decoration alone.

### Primary brand promise

**Better defaults for coding agents.**

### Secondary line

**Install the working methods you keep repeating.**

### Category descriptor

**Cross-agent skills and workflow plugins for disciplined engineering, planning, release, and writing.**

---

# 2. Product truth

The current repository contains six separately installable plugins:

| Public product | Core job | Product type |
| --- | --- | --- |
| More With Less Engineering (`s-kit`) | Minimize unnecessary complexity without weakening guarantees | Skill plus optional hook behavior |
| Cutting a Release | Evidence-driven Git release preparation, publication, verification, and recovery | Procedural skill |
| OpenSpec Brainstorming | Turn rough ideas into approved, validated OpenSpec changes | Planning skill |
| Engineering Harness Adaptive | Risk-scaled engineering workflow with verification and specialist roles | Skill + agents + hooks |
| Lite Writing | Make professional and technical prose concise without losing meaning | Writing skill |
| AI Fingerprint Mitigator | Remove formulaic AI-style prose patterns while preserving authorship and facts | Editing skill |

The marketplace manifests expose all six as separate installable plugins. 

The README currently documents native marketplace installation for Claude Code, Codex, and Copilot CLI. 

This cross-host packaging should be one of the main public differentiators.

### What is especially defensible

The collection has a recognizable operating philosophy.

More With Less explicitly optimizes for the "minimum sufficient system" while preserving correctness, security, data integrity, accessibility, operability, and verification. 

Cutting a Release applies evidence-over-convention, pinned release state, irreversible-action gates, and explicit verification. 

OpenSpec Brainstorming separates observed facts, decisions, assumptions, and open questions and prevents implementation before the planning contract is approved. 

Engineering Harness Adaptive goes further than instructional prose: the plugin declares skills, agents, and hooks, while host lifecycle hooks can enforce verification at completion.  

Lite Writing and AI Fingerprint Mitigator similarly emphasize preserving meaning, provenance, uncertainty, and the author's actual voice rather than optimizing superficial outputs.  

This produces a strong umbrella idea:

> **Skill Kit turns recurring judgment about how an agent should work into reusable operating methods.**

---

# 3. Current launch gaps

Branding should not proceed as if this is already a mature public product surface.

At present the repository has:

- no GitHub description;
- no homepage;
- no topics;
- no recognized license;
- only limited GitHub release history;
- no visible community/trust layer at the repository root.

 

### Critical blocker: license

Do not market Skill Kit as "open source" until an appropriate license is actually committed and recognized by GitHub.

Choose the license deliberately before launch. MIT would be a common low-friction option for this type of repository, but the legal choice belongs to the maintainer.

### Critical naming issue

"Skill Kit" is highly descriptive and already collides with multiple agent-related projects.

Two particularly relevant examples are:

- Contentful's `skill-kit`, a TypeScript SDK for building agent skills as state machines;
- Crafter Station's `skill-kit`, a local analytics tool for installed AI-agent skills.



This creates:

- GitHub search ambiguity;
- weak SEO ownership;
- social mention ambiguity;
- future package/domain problems;
- a harder trademark story;
- confusion over whether "Skill Kit" is a product or a generic category.

### Recommendation

Run a naming gate before final logo production.

If keeping the current name, consistently use:

**Skill Kit by Gustavo Meilus**

in metadata, search-oriented copy, social cards, and external announcements, while keeping the visual wordmark simply **Skill Kit**.

If this is intended to become a substantial ecosystem rather than a personal repository, renaming now is materially cheaper than renaming after releases, inbound links, package distribution, and community adoption.

The rest of this plan assumes **Skill Kit** remains the working name.

---

# 4. Positioning

## Primary audience

Developers and maintainers who actively use coding agents for real project work and have started repeating the same behavioral instructions across sessions and tools.

They are not looking for another AI application.

They are trying to make the agents they already use:

- scope work more intelligently;
- avoid unnecessary engineering;
- respect verification;
- plan before implementing when needed;
- release software more carefully;
- write more concisely;
- behave consistently across different agent hosts.

## Job to be done

> Help developers install recurring engineering judgment into the coding agents they already use instead of re-explaining the same working rules every session.

## Primary failure mode

### Named enemy: workflow drift

"Workflow drift" is when the agent gradually departs from the working method the developer actually wants:

- adding architecture the task did not require;
- reopening settled decisions;
- skipping meaningful verification;
- using an expensive agent or process where a deterministic check would do;
- producing release claims without evidence;
- turning concise prose into generic assistant language;
- forgetting important operating constraints between sessions.

This is broad enough to unify the collection while remaining connected to the actual mechanisms.

Do not frame ordinary model imperfections as a catastrophe. The playbook specifically recommends naming a recognizable existing failure rather than manufacturing fear.

## Precise positioning sentence

> **Skill Kit is a cross-agent toolkit for developers who want coding agents to follow repeatable engineering and writing methods, using installable skills and optional deterministic workflow controls without replacing the agent host with a heavyweight framework.**

## Short promise

> **Better defaults for coding agents.**

## Problem-oriented message

> Stop re-teaching your coding agent how to work.

## Mechanism-oriented message

> Install reusable working methods directly into Claude Code, Codex, and Copilot CLI.

---

# 5. Differentiation

Skill Kit should not compete on "number of skills."

That race produces a commodity catalog.

Compete on **curation and method quality**.

### Differentiation pillars

#### 1. Methods, not prompt snippets

Each skill represents an opinionated operating procedure, decision model, or editing contract rather than a collection of clever phrases.

#### 2. Evidence before claims

Verification, explicit completion conditions, and truthful reporting appear repeatedly across the collection.

#### 3. Process proportional to risk

The skills tend to reject both under-engineering and excessive ceremony.

#### 4. Native to existing agent hosts

The user does not adopt an entirely new agent framework just to use the methods.

#### 5. Determinism where determinism belongs

Some packages move beyond "remember this instruction" and use hooks, scripts, tests, or verification gates when the host supports them.

#### 6. Explicit boundaries

The project frequently states what a skill does not do.

That should become a public trust signal.

---

# 6. Brand architecture

Use a **branded house**.

Do not create six independent brands.

## Parent

### Skill Kit

Meaning:

> The trusted collection.

Parent-level promise:

> Better defaults for coding agents.

## Product families

### BUILD

Engineering and implementation behavior.

- More With Less
- Adaptive Engineering Harness

### SHIP

Planning and delivery.

- OpenSpec Brainstorming
- Cutting a Release

### WRITE

Technical and professional prose.

- Lite Writing
- AI Fingerprint Mitigator

This family structure should appear in the README and visual system, but installation names remain unchanged.

## Public display names

I recommend shortening the human-facing labels while retaining technical slugs.

| Technical slug | Preferred display name |
| --- | --- |
| `s-kit` | More With Less |
| `engineering-harness-adaptive` | Adaptive Engineering Harness |
| `openspec-brainstorming` | OpenSpec Brainstorming |
| `cutting-a-release` | Cutting a Release |
| `lite-writing` | Lite Writing |
| `ai-fingerprint-mitigator` | AI Fingerprint Mitigator |

### Special treatment: AI Fingerprint Mitigator

Always put its boundary next to the name:

> Removes formulaic AI-style prose patterns. Not an AI-detector evasion tool.

The skill itself already makes this distinction explicitly. 

Longer term, consider renaming this product to something less easily misunderstood, such as a formulation around "de-templating" or "prose patterns." Do not change the existing technical slug casually once users depend on it.

---

# 7. Visual brand concept

## Core metaphor

### A precision bit set for agent work

Avoid the obvious literal toolbox.

The more useful metaphor is a **compact set of interchangeable precision bits**:

- each bit has one job;
- you choose only what is needed;
- the same tool body can accept different bits;
- more tooling is not automatically better;
- the kit stays compact;
- specialized pieces can still enforce precise behavior.

This mirrors the project's own "least powerful sufficient mechanism" philosophy.

The visual execution should remain abstract rather than drawing actual screwdrivers.

### Graphic translation

Build the identity around:

- a compact enclosing frame;
- modular inserts;
- slots;
- brackets;
- alignment marks;
- small technical labels;
- restrained geometric glyphs.

Think **instrument cassette**, not hardware-store toolbox.

## Parent mark

Recommended construction:

A compact square containing three modular vertical or diagonal inserts held between two structural brackets.

At small sizes it reads as one strong technical symbol.

At larger sizes the inserts communicate modularity.

Optional negative-space construction can suggest an abstract `S` without requiring a literal monogram.

### Avoid

- robot heads;
- AI sparkles;
- brains;
- magic wands;
- circuit-board clichés;
- literal toolbox illustrations;
- wrenches/hammers;
- vendor logos inside the identity;
- six permanent slots representing the six current products;
- tiny text inside the mark.

The brand must remain extensible when the seventh or twentieth skill arrives.

---

# 8. Logo brief

Design a professional 1:1 identity mark for **Skill Kit**, a collection of installable working methods for coding agents.

**Audience:** software developers, maintainers, and frequent users of Claude Code, Codex, and Copilot CLI.

**Outcome:** make the collection feel compact, deliberate, technically credible, and reusable rather than like a random prompt repository.

**Core metaphor:** interchangeable precision modules held inside a compact technical frame. Each module represents a working method that can be installed into an existing coding-agent environment.

**Personality:**

- precise;
- compact;
- disciplined;
- pragmatic;
- quietly opinionated.

**Visual language:**

- strong geometric silhouette;
- modular construction;
- subtle bracket/interface references;
- restrained technical detail;
- vector-first;
- recognizable at 24-32 px.

**Composition:**

- square;
- symbol first;
- generous internal spacing;
- no embedded wordmark at icon size.

**Avoid:**

- robots;
- brains;
- sparkles;
- magic;
- literal toolboxes;
- famous brand structures;
- vendor marks;
- photorealism;
- gradients required for recognition;
- excessive details.

The attached playbook recommends exactly this mechanism-first approach and calls for a small-size, vector-friendly, symbol-first identity rather than decorative branding.

---

# 9. Color system

The repository already contains a small OpenSpec icon using cobalt/periwinkle tones, so evolving toward a disciplined blue system avoids unnecessary visual discontinuity. 

## Parent palette

**Ink**
`#11151B`

Primary dark background and text.

**Paper**
`#F7F8FA`

Primary light background.

**Kit Cobalt**
`#4B61E6`

Primary identity color.

**Interface Blue**
`#7183F3`

Secondary brand tone.

**Signal Mint**
`#35C5A4`

Positive state, verification, success, active module.

**Signal Amber**
`#E9AD3C`

Warnings, release state, caution.

**Signal Coral**
`#E96B67`

Exceptions, boundaries, destructive actions.

**Slate**
`#687180`

Secondary copy and diagrams.

## Usage rule

Parent identity should normally use only:

- Ink/Paper;
- Cobalt;
- one status accent where semantically useful.

Do not make every README section a different color.

---

# 10. Skill color accents

Use the same parent frame and typography for every skill, changing only a restrained accent and internal glyph.

| Skill | Accent | Glyph concept |
| --- | --- | --- |
| More With Less | Cobalt | nested forms reducing to one essential block |
| Adaptive Engineering Harness | Mint | gate / bounded loop |
| OpenSpec Brainstorming | Violet-blue | branching nodes |
| Cutting a Release | Amber | pinned tag / verified marker |
| Lite Writing | Cool teal | several lines compressing into fewer lines |
| AI Fingerprint Mitigator | Coral | repetitive pattern broken into natural variation |

The existing OpenSpec branching icon can be redesigned into this system rather than discarded outright.

---

# 11. Typography

## Brand graphics

**IBM Plex Sans**

Use for:

- wordmark support text;
- social cards;
- diagrams;
- product cards.

## Technical text

**IBM Plex Mono**

Use for:

- commands;
- plugin slugs;
- host labels;
- diagrams;
- technical annotation.

For normal GitHub README prose, let GitHub use its native interface typography. Do not convert documentation into image text merely to enforce the brand font.

---

# 12. Wordmark

Preferred form:

**Skill Kit**

Supporting lockup:

**Skill Kit**  
*Better defaults for coding agents.*

External/search-oriented lockup when necessary:

**Skill Kit by Gustavo Meilus**

Avoid stylizing the product as `SKILLKIT`, `skillkit.ai`, or `S-KIT` at the parent level.

`S-Kit` already refers to the More With Less plugin and should not simultaneously become the parent brand.

---

# 13. Graphic language

The identity should have a repeatable visual grammar beyond the logo.

## Module cards

Each skill gets a compact card:

```text
[BUILD]

MORE WITH LESS
Minimum-sufficient engineering

Claude Code  Codex  Copilot
```

## Technical rails

Use thin horizontal/vertical rules with small labels:

```text
METHOD / VERIFY / SHIP
```

## State vocabulary

Use small labels consistently:

- SKILL
- HOOK
- AGENT
- SCRIPT
- VERIFIED
- OPTIONAL
- HOST-SPECIFIC

This turns architectural truth into part of the identity.

## Diagrams

Prefer:

- compact flows;
- before/after behavior;
- host capability matrices;
- method ladders;
- verification paths.

Avoid decorative illustration when the product mechanism itself provides a better visual.

---

# 14. Brand voice

## Voice principles

### Direct

Say:

> Use the least powerful mechanism that works.

Not:

> Unlock a revolutionary approach to streamlined software development.

### Specific

Say:

> Runs the project's normal verification command before completion.

Not:

> Ensures superior engineering quality.

### Opinionated, but bounded

Say:

> One agent by default. Add another only when isolation or independent judgment buys something.

Not:

> Multi-agent systems are bad.

### Evidence-led

Say:

> The plugin includes a deterministic completion gate.

Not:

> Makes agents more reliable.

Unless reliability has actually been measured.

### Developer-native

Use the language already present in the product:

- scope;
- verification;
- invariant;
- acceptance criteria;
- hook;
- agent;
- host;
- skill;
- release;
- evidence;
- deterministic;
- progressive context.

## Avoid

- "10x";
- "supercharge";
- "revolutionary";
- "game-changing";
- "AI-powered";
- "magic";
- "battle-tested" without evidence;
- "production-ready" without a release bar;
- "guarantees quality";
- "humanizes AI text";
- AI-detector avoidance language.

---

# 15. Messaging hierarchy

## Level 1 - Recall

**Better defaults for coding agents.**

## Level 2 - Problem

You already know how you want your coding agent to work. The problem is having to explain it again.

## Level 3 - Mechanism

Install reusable skills and workflow plugins directly into the agent CLI you already use.

## Level 4 - Differentiation

Some skills are lightweight operating methods. Others add deterministic verification, hooks, or specialist roles where stronger controls are useful.

## Level 5 - Proof

Show:

- exact plugin manifests;
- executable hooks;
- tests;
- reproducible examples;
- host capability differences.

---

# 16. Repository description

Recommended GitHub description:

> **Cross-agent skills and workflow plugins for disciplined engineering, planning, release, and writing.**

Shorter alternative:

> **Better working methods for Claude Code, Codex, and Copilot CLI.**

---

# 17. GitHub topics

Use a focused set rather than filling the 20-topic maximum.

Recommended:

- `agent-skills`
- `coding-agents`
- `ai-agents`
- `claude-code`
- `codex`
- `github-copilot`
- `developer-tools`
- `engineering-workflows`
- `software-engineering`
- `verification`
- `openspec`
- `writing-tools`

Avoid making `prompt-engineering` a primary topic because it pulls the brand toward the "prompt collection" category you should be differentiating against.

---

# 18. README strategy

The current README jumps quickly from a generic category line into installation and the inventory. 

It should become a conversion path:

**recognize -> see -> choose -> install -> trust -> explore**

This follows the playbook's recommended structure of hero, recognizable problem, demonstration, quick start, proof, workflow, safety, compatibility, architecture, documentation, and contribution.

## Proposed top-level README

### Hero

Logo.

# Skill Kit

**Better defaults for coding agents.**

Install reusable engineering, planning, release, and writing methods into Claude Code, Codex, and Copilot CLI.

Use a lightweight skill when instructions are enough. Use hooks, verification gates, or specialist roles when stronger controls are warranted.

`[Install] [Browse skills] [How it works]`

### Problem

## Stop re-teaching your agent how to work

Your coding agent can already edit files, search repositories, run commands, and reason about code.

The recurring problem is the operating method around that work:

- how much architecture is enough;
- when planning is worth the ceremony;
- what evidence counts as done;
- how a release should be gated;
- how much prose is enough;
- when another agent or another tool actually helps.

Skill Kit packages those methods so they can be reused.

### See it

Use the flagship More With Less skill as the demonstration.

```text
Task
  "Add the requested behavior."

Generic path
  new abstraction
  new helper
  speculative extension points
  broad cleanup
  tests

More With Less
  inspect requirement
  reuse existing mechanism
  smallest coherent change
  required verification
  stop
```

Then link to the actual skill doctrine.

This demonstrates the philosophy without claiming measured superiority.

### Pick a skill

Group the plugins as BUILD / SHIP / WRITE.

For each card include:

- job;
- mechanism;
- hosts;
- whether hooks/agents are included;
- link.

### Install

Make marketplace addition a one-time first step.

Then show host tabs or subsections for:

- Claude Code;
- Codex;
- Copilot CLI.

Every command must be tested verbatim immediately before launch.

### How Skill Kit works

Explain the hierarchy:

```text
Skill
  reusable operating method

Plugin
  distributable package

Hook
  deterministic lifecycle behavior when needed

Agent
  isolated specialist context when needed

Script
  deterministic mechanism where model judgment is unnecessary
```

### Proof, not promises

Lead with structural facts, not benchmark language.

Examples:

- six current plugins;
- cross-host marketplace manifests;
- executable hook files;
- focused tests where present;
- read-only role definitions for the adaptive engineering harness.

Do not add a performance benchmark merely because marketing wants a percentage.

### Host support

Build an explicit matrix:

| Capability | Claude Code | Codex | Copilot CLI |
| --- | --- | --- | --- |
| Marketplace installation | Verify | Verify | Verify |
| Skills | Verify | Verify | Verify |
| Lifecycle hooks | Exact behavior | Exact behavior | Exact behavior |
| Specialist roles | Exact behavior | Manual/automatic status | Exact behavior |
| Project integration | Exact status | Exact status | Exact status |

Do not use generic green checkmarks until each row has been mechanically verified.

### Philosophy

A compact section can state the collection-wide principles:

1. Use the least powerful sufficient mechanism.
2. Let risk determine verification strength.
3. Use model judgment only where deterministic checks are insufficient.
4. Keep authority and context narrow.
5. Report evidence rather than implying success.
6. Add process only when it removes real uncertainty.

### Trust and boundaries

Explicitly distinguish:

**Skill Kit can**

- provide reusable agent procedures;
- install host-native plugin surfaces;
- provide hooks/scripts where included;
- supply read-only specialist roles where supported.

**Skill Kit cannot**

- guarantee model correctness;
- make every host enforce identical boundaries;
- prove better software quality merely by being installed;
- make AI-generated text "undetectable";
- replace repository-specific requirements.

### Contribution/security/license

Do not bury these.

---

# 19. Claim ledger

Before publishing the redesigned README, maintain this ledger.

| Claim | Current evidence | Public status |
| --- | --- | --- |
| Contains six plugins | Both marketplace manifests | Safe |
| Supports Claude Code, Codex, Copilot CLI | README plus host-specific manifests | Use after clean-install smoke tests |
| Provides reusable engineering and writing skills | Skill files | Safe |
| More With Less uses minimum-sufficient engineering doctrine | Skill content | Safe |
| Adaptive Harness includes deterministic verification | Scripts/hooks/manifests | Safe with exact qualification |
| Adaptive Harness includes specialist roles | Role files/manifests | Safe with host qualification |
| All platforms behave identically | Not supported | Do not claim |
| Improves code quality | No comparative evidence inspected | Do not claim |
| Saves tokens | No comparative evidence inspected | Do not claim |
| Makes agents faster | No benchmark inspected | Do not claim |
| AI Fingerprint Mitigator evades detection | Explicitly rejected by implementation | Never claim |
| Open source | No recognized license currently | Do not claim yet |

The playbook's core rule is that marketing must move toward executable and shipped truth, never the reverse.

---

# 20. Proof program

You do not need a large benchmark campaign for launch.

Start with structural and functional evidence.

## Proof artifact 1 - clean install matrix

For each supported host:

1. fresh environment;
2. add marketplace;
3. install each plugin;
4. invoke/discover skill;
5. uninstall;
6. record host and version.

Publish the matrix.

## Proof artifact 2 - More With Less case study

Choose one small real repository task.

Show:

- requirement;
- initial implementation temptation;
- selected mechanism;
- final diff;
- verification;
- what was intentionally not added.

Do not turn a single case into a universal productivity claim.

## Proof artifact 3 - deterministic completion gate

Demonstrate:

```text
implementation
    |
    v
agent attempts completion
    |
    v
verification hook
   / \
pass fail
 |    |
done continue
```

This is particularly useful because it communicates why some Skill Kit products are more than Markdown instructions.

## Proof artifact 4 - release ledger

Publish an anonymized/example release ledger produced by Cutting a Release.

## Proof artifact 5 - writing before/after

Show a short prose sample with repetitive AI-style scaffolding and the revised output.

Describe visible differences rather than claiming authorship transformation.

---

# 21. Asset matrix

Produce:

| Asset | Specification |
| --- | --- |
| Master mark | SVG, square |
| GitHub avatar | 512x512 PNG |
| README mark | 256 or 512 px optimized PNG/SVG |
| Light hero | SVG/PNG |
| Dark hero | SVG/PNG |
| Social preview | 1280x640 PNG |
| Skill badge frame | SVG |
| 6 skill icons | SVG |
| Host support diagram | SVG |
| Installation visual | SVG or terminal recording |
| Favicon | 32/64 px |
| OpenGraph/card source | deterministic SVG or layout source |

The playbook recommends preserving one selected mark and generating deterministic derivatives instead of regenerating the logo independently for every asset.

---

# 22. Social preview

Recommended layout:

```text
[mark]

SKILL KIT

Better defaults
for coding agents.

Engineering / Planning / Release / Writing

Claude Code · Codex · Copilot CLI
```

Do not put "6 skills" in the main design because the number will become stale.

Use a flat, self-contained 1280x640 PNG for reliable rendering.

---

# 23. Trust and community layer

Before promotion, add at minimum:

- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `SUPPORT.md` or a clear support section
- issue forms
- pull-request template

For this project specifically, also add:

### `docs/HOSTS.md`

Exact behavioral differences between Claude Code, Codex, and Copilot CLI.

### `docs/PLUGIN-AUTHORING.md`

How a new skill/plugin should be structured before it enters Skill Kit.

### `docs/PHILOSOPHY.md`

Short parent-level doctrine distilled from the common principles.

### `docs/VERIFICATION.md`

What "verified" means at the repository level.

### `docs/BRANDING.md`

Logo files, palette, product-card construction, display naming, and attribution.

The attached playbook recommends README plus task guides plus deeper maintainer evidence rather than forcing everything into one front page.

---

# 24. Curation policy

A curated brand becomes more valuable if inclusion means something.

Define entry requirements for future Skill Kit plugins.

A plugin belongs in Skill Kit only when it has:

1. one clear recurring job;
2. explicit trigger/use conditions;
3. explicit non-use conditions;
4. no unnecessary always-loaded context;
5. bounded authority;
6. host-specific behavior documented;
7. deterministic mechanisms used where appropriate;
8. completion criteria;
9. truthful limitations;
10. a maintainer-level review.

This transforms Skill Kit from "Gustavo's folder of skills" into a recognizable product standard.

---

# 25. Launch narrative

Do not launch with:

> I made a repository with six AI skills.

Launch with the recurring problem.

### Core launch story

Developers keep teaching coding agents the same working rules:

- don't over-engineer this;
- verify before you say it is done;
- plan this before coding;
- release from evidence, not assumptions;
- make this shorter without deleting meaning.

Skill Kit packages those recurring methods into installable plugins for the coding-agent CLIs you already use.

Some are deliberately just skills.

Some add deterministic controls when instructions alone are not enough.

That is the product.

The playbook's launch hierarchy similarly recommends pain -> memorable product idea -> demonstration -> proof/boundary -> shortest install path -> focused feedback.

---

# 26. Launch headline

Recommended:

> **Skill Kit: better defaults for coding agents**

Alternative:

> **Stop re-teaching your coding agent how to work**

Technical alternative:

> **Reusable engineering methods for Claude Code, Codex, and Copilot CLI**

---

# 27. Launch channels

Priority order:

### 1. GitHub itself

Complete:

- description;
- topics;
- social preview;
- license;
- community files;
- tagged release;
- polished README.

### 2. Maintainer network

Personal GitHub profile, existing repositories, and relevant existing users.

Cross-link only where the tool is genuinely relevant.

### 3. Hacker News

A Show HN is appropriate once:

- clean installs are verified;
- README is complete;
- licensing is resolved;
- the naming issue is consciously accepted;
- there is at least one real demonstration.

The technical angle should be the interesting part, not branding.

### 4. Agent communities

Use host-specific demonstrations:

- Claude Code communities;
- Codex communities;
- Copilot CLI communities;
- OpenSpec users for the OpenSpec plugin.

### 5. Technical writing

This is likely the strongest durable channel.

Publish useful artifacts rather than generic announcements.

---

# 28. Content strategy

Each plugin can generate one useful piece of technical content.

## More With Less

**Article:** "The least powerful sufficient mechanism"

Use real examples of:

- a prompt vs script;
- an agent vs test;
- an abstraction vs direct code;
- an orchestration loop vs one bounded retry.

## Adaptive Engineering Harness

**Article:** "When agent instructions are not enough"

Explain:

- lifecycle hooks;
- completion gates;
- specialist isolation;
- deterministic verification.

## Cutting a Release

**Artifact:** reusable release ledger.

## OpenSpec Brainstorming

**Article:** "Separate facts, decisions, assumptions, and open questions before implementation."

## Lite Writing

**Before/after:** technical documentation compressed without information loss.

## AI Fingerprint Mitigator

**Article:** "AI-style prose is a writing problem, not proof of authorship."

This also reinforces its safety boundary.

Useful evidence and reusable artifacts should do more marketing work than slogans, which is a central recommendation in the attached playbook.

---

# 29. Release strategy

Do not create a ceremonial v1 release only to make the repository appear mature.

First complete the launch gate:

### Product

- all six plugin manifests consistent;
- installation commands tested;
- host differences documented;
- references resolve;
- no stale skill descriptions.

### Brand

- naming decision;
- final mark;
- README hero;
- social preview;
- six skill badges/icons.

### Trust

- license;
- security policy;
- contribution guidance;
- issue templates;
- support expectations.

### Proof

- clean install matrix;
- representative flagship demonstration;
- no unsupported performance claims.

### Repository

- description;
- topics;
- social card manually uploaded in settings.

Then cut the first branded release.

---

# 30. First-release message

The release should emphasize the system rather than every internal file.

Suggested hierarchy:

**Skill Kit 1.0**

Better defaults for coding agents.

Initial collection:

**BUILD**
- More With Less
- Adaptive Engineering Harness

**SHIP**
- OpenSpec Brainstorming
- Cutting a Release

**WRITE**
- Lite Writing
- AI Fingerprint Mitigator

Supports installation through Claude Code, Codex, and Copilot CLI, subject to the host capability matrix documented in the repository.

Then link:

- installation;
- host matrix;
- security;
- contribution;
- individual skill documentation.

---

# 31. Metrics

Do not use stars as the primary success measure.

## Awareness

Track:

- qualified repository visits;
- stars/forks as directional signals;
- relevant external mentions;
- launch-post engagement from developers actually using agent CLIs.

## Activation

Track what can be measured without adding invasive telemetry:

- install-related issues;
- clean-install verification failures;
- release downloads where applicable;
- marketplace references;
- user reports of first successful invocation.

## Adoption

Track:

- repeat community participation;
- downstream references;
- people installing multiple Skill Kit plugins;
- external repositories adopting project-integration fragments;
- upgrade adoption where observable.

## Community

Track:

- first-time contributors;
- repeat contributors;
- time to first issue response;
- issue themes;
- documentation friction.

## Evidence

Track:

- reproduced case studies;
- externally reported workflows;
- independent comparisons;
- claims that required correction.

The playbook likewise recommends separating awareness, activation, adoption, community, reliability, and evidence instead of optimizing a single popularity number.

---

# 32. 30-day execution plan

## Phase 1 - truth and naming

Before design:

- decide whether Skill Kit remains the permanent name;
- choose license;
- verify exact host installation paths;
- audit all six manifests;
- create the claim ledger;
- document host differences.

## Phase 2 - identity

Produce:

- parent mark;
- palette;
- type system;
- product badge system;
- skill glyphs;
- light/dark hero;
- social preview.

Do not independently redesign each plugin.

## Phase 3 - repository

Rewrite README around:

1. promise;
2. problem;
3. demonstration;
4. skill selection;
5. install;
6. mechanism;
7. proof;
8. host matrix;
9. philosophy;
10. trust/community.

Add all missing repository metadata and community files.

## Phase 4 - verification

Run clean installation against all three claimed hosts.

Record:

- host version;
- commands;
- result;
- plugin discovery;
- hook behavior where relevant;
- uninstall/update behavior.

## Phase 5 - launch

Publish:

1. verified release;
2. social preview;
3. technical launch post;
4. flagship case study;
5. targeted community posts.

---

# 33. Brand acceptance criteria

The branding pass is complete only when a new visitor can answer these questions within roughly two minutes:

**What is Skill Kit?**  
Reusable working methods for coding agents.

**Why would I want it?**  
I keep re-explaining engineering, release, planning, or writing rules to my agents.

**What makes it different?**  
It is curated around disciplined working methods, uses host-native distribution, and can use deterministic controls when instructions alone are insufficient.

**Does it replace my coding agent?**  
No.

**Which agents does it target?**  
Claude Code, Codex, and Copilot CLI, with exact host differences documented.

**What should I install first?**  
The skill matching my current job, not the entire collection.

**Can I trust the claims?**  
Claims point to executable structure, tests, demonstrations, or clearly stated limitations.

**What does the brand look like?**  
Compact, modular, technical, and recognizable without depending on AI clichés.

---

# 34. Final brand platform

## Name

**Skill Kit**

Pending the naming decision caused by current ecosystem collisions.

## Category

**Cross-agent working-method toolkit**

## Audience

Developers who use coding agents for real software work.

## Problem

**Workflow drift:** recurring good engineering judgment gets lost between tasks, sessions, and hosts.

## Promise

**Better defaults for coding agents.**

## Mechanism

Installable skills plus deterministic workflow controls where appropriate.

## Philosophy

Use the least powerful sufficient mechanism and require evidence proportional to the risk.

## Personality

Precise. Compact. Pragmatic. Disciplined. Slightly opinionated.

## Primary metaphor

A compact precision-bit system: specialized methods that fit the tools developers already use.

## Core CTA

**Pick a skill. Install the method.**

## Brand test

Every addition to Skill Kit should make this sentence more credible:

> **You should not have to re-teach a capable coding agent the same good working method every time.**
