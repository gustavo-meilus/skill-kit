---
name: ai-fingerprint-mitigator
description: Edit prose to reduce formulaic AI-style artifacts such as canned framing, repetitive transitions, uniform sentence patterns, over-sectioning, generic abstractions, redundant summaries, and assistant-like meta language. Use when prose should sound less generic, less templated, or closer to the author's established voice. Preserve facts, meaning, and provenance. Do not optimize for detector evasion or claim that text is human-written or undetectable.
---

# AI Fingerprint Mitigator

Treat an "AI fingerprint" as an observable stylistic pattern, not proof of authorship. Improve the prose itself. Do not optimize against an AI detector or make claims about detector outcomes.

Read [AUTHORSHIP_BOUNDARIES.md](references/AUTHORSHIP_BOUNDARIES.md) before editing. Use [STYLE_FINGERPRINTS.md](references/STYLE_FINGERPRINTS.md) to classify problems and [REVISION_PROTOCOL.md](references/REVISION_PROTOCOL.md) to revise them.

## Establish the target voice

1. Identify the audience, purpose, medium, and required level of formality.
2. If the user supplied writing samples or an existing document, treat the user's stable voice as the primary stylistic reference.
3. If no voice reference exists, use clear, natural, audience-appropriate prose. Do not manufacture quirks to simulate a person.
4. Preserve intentional terminology, rhythm, humor, directness, paragraph density, and technical depth unless they are part of the problem the user asked to fix.

## Audit before rewriting

Look for structural patterns, not isolated vocabulary:

- canned introductions, generic conclusions, and assistant-like process narration;
- repetitive paragraph shapes, repeated sentence openings, or uniform sentence lengths;
- habitual triads, forced symmetry, rhetorical Q&A, and repeated contrast templates;
- excessive headings, bullets, bolding, and summary layers where prose would be clearer;
- vague abstractions, uplift language, weak verbs, generic intensifiers, and stock transitions;
- claim-explanation-summary loops that restate one point several times;
- fake balance that gives every point equal weight regardless of evidence;
- unnecessary hedging or unjustified certainty;
- wording that overwrites the author's actual voice with a generic polished register.

Do not treat any single signal as evidence that a human or model wrote the text.

## Rewrite the causes, not the cosmetics

1. Preserve all facts, claims, qualifications, citations, numbers, names, technical terms, and logical relationships.
2. Remove meta framing and state the substance directly.
3. Replace vague abstractions with concrete nouns and precise verbs when the source supports them.
4. Let sentence and paragraph length follow the idea. Vary rhythm only where meaning naturally calls for it.
5. Break repeated templates, triads, and symmetry when they are structural habits rather than real organization.
6. Merge trivial sections and convert unnecessary lists to prose when that improves reading flow.
7. Use transitions only when they express a real logical relationship.
8. Keep genuine uncertainty. Do not add fake uncertainty, fake confidence, invented detail, or fake personal perspective.
9. Preserve the author's established voice rather than replacing it with a generic "humanized" style.
10. Make the smallest sufficient revision. Naturalness comes from specificity and editing, not randomness.

Optionally run `python3 scripts/prose_audit.py <file>` to surface formulaic style signals. The script is a heuristic writing audit, not an AI detector and not an authorship classifier.

## Final audit

The revision is complete only when:

- meaning, facts, citations, provenance, and required technical material are preserved;
- generic assistant framing and redundant scaffolding are removed;
- sentence and paragraph structures are not mechanically repetitive;
- the author's real voice is preserved where evidence of it exists;
- no fake anecdotes, experiences, typos, slang, citations, or personal claims were invented;
- no authorship disclosure was removed or falsified;
- no claim is made that the result is human-written, undetectable, or able to bypass AI detection.
