---
name: lite-writing
description: Create or revise concise, clear documents and prose using the Lite Response Mode writing contract. Use for technical documentation, READMEs, specifications, reports, summaries, instructions, explanations, professional prose, and other writing where information density and clarity matter. Do not use when narrative voice, literary style, dialogue, scene description, marketing voice, or another explicit writing style is part of the requested content.
---

# Lite Writing

Use normal reasoning and information gathering. Tighten only the generated prose. The objective is high information density with normal grammar and no loss of necessary meaning.

## Classify the writing first

Read [SCOPING.md](references/SCOPING.md). Apply Lite mode only when concise explanatory or professional prose is appropriate.

Bypass Lite mode when style is part of the content: fiction, narrative description, scene prose, dialogue, character voice, diegetic text, literary writing, style exemplars, quoted wording, brand/marketing voice, or any explicit user-requested style that conflicts with Lite mode.

For a mixed document, apply Lite mode to explanatory scaffolding only. Preserve style-controlled passages according to their own writing authority.

## Write under the Lite contract

1. Start with the useful information. Remove greetings, canned introductions, unnecessary process narration, and repeated conclusions.
2. Remove filler and habitual hedging. Preserve uncertainty when the evidence is genuinely uncertain.
3. Keep ordinary grammar, articles, complete sentences, and explicit causal or logical relationships.
4. Preserve exact technical terms, code, commands, error strings, names, numbers, units, negation, scope words, exceptions, and ordering.
5. Prefer concrete nouns and precise verbs. Do not invent cryptic abbreviations, broken grammar, or artificial shorthand to look concise.
6. State each meaning once. Remove restatement, decorative transitions, redundant summaries, and needless sectioning.
7. Keep explicit sequence markers where order matters. Expand security warnings, irreversible operations, or ambiguous procedures when compression could create risk.
8. Match the user's language and the artifact's audience. Durable documentation should remain complete enough to stand on its own outside the chat.

## Revision workflow

1. Determine the audience, purpose, required facts, and requested format.
2. Preserve every necessary fact, caveat, constraint, example, and technical token before shortening prose.
3. Draft or revise directly in Lite form. Do not write a verbose version and append a second concise version.
4. Remove low-information language sentence by sentence.
5. Restore explicit wording anywhere compression creates ambiguity, safety risk, false certainty, or unclear ordering.
6. Run the checklist in [REVIEW_CHECKLIST.md](references/REVIEW_CHECKLIST.md).

Consult [LITE_RESPONSE_MODE_DETAILED.md](references/LITE_RESPONSE_MODE_DETAILED.md) for edge cases, examples, and the complete processing model.

## Completion criteria

The result is complete only when:

- the actual task is fully answered;
- no necessary fact, exception, uncertainty, number, unit, command, code symbol, or ordering constraint was lost;
- filler, empty hedging, canned framing, duplication, and unnecessary summaries are removed;
- sentences remain grammatical and natural;
- style-controlled or narrative passages were not flattened into Lite prose;
- the output contains one finished version unless the user explicitly requested alternatives.
