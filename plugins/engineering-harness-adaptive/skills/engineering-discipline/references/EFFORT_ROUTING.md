# Model and Effort Routing

This document is the detailed routing policy for the engineering harness. Model families evolve; treat the model names below as current defaults, not eternal equivalences.

## Core rule

Allocate inference-time compute instead of maximizing it.

```text
cheap bounded work      -> cheap bounded compute
semantic uncertainty    -> deeper reasoning
settled implementation  -> return to balanced compute
independent review      -> deeper bounded reasoning
failed hard subproblem  -> targeted escalation
```

Effort amplifies the problem formulation and verifier. It does not repair vague scope or a weak definition of done.

## Two independent axes

### Risk

Risk asks: **How costly would a wrong change be?**

Higher risk increases verification independence, breadth, and human approval requirements.

### Difficulty

Difficulty asks: **How much search/reasoning is needed to discover the right change?**

Higher difficulty increases reasoning effort/model capability.

Do not collapse them. A straightforward production migration step can be high-risk but low-difficulty; use strong deterministic safeguards and approval without automatically using maximum model effort.

## Phase defaults

| Phase | Default reasoning posture | Escalate when | Main overthinking risk |
| --- | --- | --- | --- |
| Locate/read | Low/Medium | Repository relationship is unclear | Unnecessary exploration |
| Explore problem | Medium | Root cause/semantics remain unclear | Inventing requirements |
| Requirements/spec | Medium/High | Subtle behavior or edge cases | Encoding implementation as requirement |
| Design | High when warranted | Security/concurrency/migration tradeoff is genuinely hard | Premature abstraction |
| Task decomposition | Medium | Dependency order is non-obvious | Oversplitting |
| Reproduction/oracle | Medium/High | Correct expected behavior is hard to establish | Circular self-validation |
| Implementation | Medium when calibrated | Implementation itself becomes a new discovery problem | Reopening settled design |
| Refactor | Medium | Behavior-preserving restructuring is genuinely complex | Opportunistic cleanup |
| Review/verify | High | High-risk subtle issue remains | Usually bounded by diff/spec |
| Specialist diagnosis | xHigh | D3 bounded question | Expanding beyond the question |
| Max | Exceptional only | xHigh failed and quality gain is worth cost | Diminishing returns/overthinking |

## Escalation state machine

```text
balanced attempt
      |
      v
   verify
   /    \
 pass   fail/uncertain
  |          |
 done     classify
             |
       mechanical? -> stay balanced and fix
             |
       semantic/causal? -> high planner/diagnosis
             |
           verify
          /      \
       pass      still stuck
        |           |
       done    xHigh specialist
                    |
             bounded conclusion
                    |
             balanced implementation
                    |
                 verify
```

Escalate the failed **step**, not the whole remaining session.

## Provider families are role bands, not equivalents

The following pairings are useful operational bands, but they are not claims of equal intelligence, price, latency, or token efficiency.

| Operational band | OpenAI | Anthropic | Intended harness use |
| --- | --- | --- | --- |
| Frontier/specialist | GPT-5.6 Sol | Claude Fable 5 | Hard bounded reasoning, critical adversarial analysis |
| Advanced/balanced agent | GPT-5.6 Terra | Claude Opus 5 | Serious routine agent work, implementation after calibration, planning/review where frontier is unnecessary |
| Efficient/high-volume | GPT-5.6 Luna | Claude Sonnet 5 | Narrow lookup, high-volume/read-only work, routine work proven by evals |

These bands deliberately follow the requested cross-family mental model while preserving provider-specific guidance. Anthropic currently recommends Opus 5 as the starting point for most agent workloads, while Fable 5 is the highest-capability option. OpenAI recommends Sol when unsure for complex reasoning/coding, Terra for intelligence/cost balance, and Luna for cost-sensitive high-volume work.

## Bootstrap policy: before local evals exist

Do not immediately optimize for cost before knowing where quality degrades.

### Codex / OpenAI

- Main serious implementation: **Sol, Medium**.
- Narrow scout: **Luna, Low**.
- Difficult planning/diagnosis: **Sol, High**.
- Independent review: **Sol, High**.
- D3 specialist: **Sol, xHigh**.
- Max: only a bounded exceptional problem after xHigh or an explicit quality-first decision.

After representative tasks show that Terra holds quality for a task class, move that class to Terra Medium. After narrow/high-volume tasks show Luna holds quality, use Luna there.

### Claude Code / Anthropic

- Main serious agent work without local evals: **Opus 5, High** (provider safe starting point).
- Narrow scout: **Sonnet 5, Low**.
- Difficult planning/diagnosis: **Opus 5, High**.
- Independent review: **Opus 5, High**.
- D3 specialist: **Fable 5, xHigh** only when capability-sensitive and permitted by data-handling policy.
- If Fable is prohibited/unavailable, use **Opus 5, xHigh** for the bounded specialist role.
- Max: exceptional quality-first cases only.

Once local evals show that Opus Medium holds for settled implementation, use it as the implementation workhorse. Sonnet Medium can be used for task classes where it is demonstrably sufficient.

## Calibrated efficiency policy

After you have local evidence, a good target shape is:

| Work | OpenAI | Anthropic |
| --- | --- | --- |
| Mechanical/narrow read-only | Luna Low | Sonnet Low |
| Routine settled implementation | Terra Medium | Opus Medium or Sonnet Medium if proven |
| Planning/root-cause diagnosis | Sol High | Opus High |
| Independent review | Sol High | Opus High |
| Bounded specialist issue | Sol xHigh | Fable xHigh (or Opus xHigh if policy requires) |
| Exceptional hardest issue | Sol Max | Fable/Opus Max after explicit justification |

This creates the desired curve: spend deeper reasoning where decisions are made and challenged, not continuously while executing a settled decision.

## Codex CLI prepared roles

Project agents in `.codex/agents/`:

- `engineering_scout`: GPT-5.6 Luna / low / read-only.
- `engineering_planner`: GPT-5.6 Sol / high / read-only.
- `engineering_reviewer`: GPT-5.6 Sol / high / read-only.
- `engineering_specialist`: GPT-5.6 Sol / xhigh / read-only.

The parent/main Codex session remains the implementer. Start it at Sol Medium before calibration; optionally use Terra Medium for task classes proven safe by local evals.

## Claude Code prepared roles

Project agents in `.claude/agents/`:

- `engineering-scout`: Claude Sonnet 5 / low / read-only tools.
- `engineering-planner`: Claude Opus 5 / high / read-only tools.
- `engineering-reviewer`: Claude Opus 5 / high / read-only tools.
- `engineering-specialist`: Claude Opus 5 / xhigh / read-only tools by default.
- Optional `.claude/agent-profiles/fable/engineering-specialist.md`: Claude Fable 5 / xhigh, installed only when explicitly permitted and justified.

Claude effort labels are calibrated per model; do not assume `high` on one model consumes the same reasoning budget as `high` on another. Claude Code supports per-subagent effort, which is why these roles are encoded separately instead of globally changing the whole session.

**Fable governance:** Fable 5 has model-specific data-handling/retention considerations in some environments, including GitHub Copilot. The shipped active Claude specialist therefore defaults to Opus 5 xHigh. Opt into the Fable profile only when organization policy permits it and the bounded task needs the extra tier.

## GitHub Copilot CLI prepared roles

Copilot CLI can run either provider family and lets custom agents declare `model` and `reasoningEffort`. The harness ships three profile sets:

- `.github/copilot-profiles/openai/`
- `.github/copilot-profiles/anthropic/` (Opus xHigh specialist; safer default)
- `.github/copilot-profiles/anthropic-fable/` (Fable xHigh specialist; explicit opt-in)

Use `python scripts/select_copilot_profile.py openai`, `anthropic`, or `anthropic-fable` to populate `.github/agents/`.

OpenAI profile:
- scout: GPT-5.6 Luna low
- planner: GPT-5.6 Sol high
- reviewer: GPT-5.6 Sol high
- specialist: GPT-5.6 Sol xhigh

Anthropic profile:
- scout: Claude Sonnet 5 low
- planner: Claude Opus 5 high
- reviewer: Claude Opus 5 high
- specialist: Claude Opus 5 xhigh

Anthropic-Fable opt-in profile changes only the specialist to Claude Fable 5 xhigh.

If Copilot session model is `Auto`, current Copilot behavior makes subagents inherit the resolved session model instead of honoring a different declared agent model. Use an explicit session/profile model when you want deterministic per-agent tier routing.

## Parallelism / Ultra / fleets

Do not conflate reasoning depth with orchestration breadth.

Parallel agents help when work decomposes cleanly, for example independent API analysis, database analysis, frontend analysis, or test investigation that can be synthesized later. They hurt when every conclusion depends on shared mutable state or a single tightly coupled causal chain.

Before enabling multi-agent/Ultra/fleet behavior, require:

1. at least two genuinely independent workstreams;
2. explicit ownership/output contract for each;
3. no concurrent writes to the same surface unless isolated by worktree;
4. a synthesis/verification step;
5. expected wall-clock or quality benefit that justifies extra tokens/context.

Otherwise stay single-agent.

## Downgrade rules

A successful harness also knows when to spend less.

Downgrade model/effort when:

- the hard design/root-cause question has been resolved;
- implementation is now a bounded transformation;
- repeated representative tasks pass at the lower setting without extra human rework;
- deterministic verification is strong enough to catch likely mistakes;
- high effort is producing broader patches, repeated searching, or speculative abstractions without measured quality gain.

## Evaluation loop

For 20-50 representative tasks when practical, compare configurations on:

- accepted-task/pass rate;
- escaped defects/human-review findings;
- files and lines changed beyond scope;
- number of attempts/retries;
- tool calls/tokens/credits when available;
- wall-clock latency;
- human review/rework time.

Optimize **cost per accepted task** and human attention, not cost per attempt or raw model prestige.
