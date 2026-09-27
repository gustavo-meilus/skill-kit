# AI fingerprint mitigation

## Purpose

Provides lightweight, actionable prose-style diagnostics and a Codex editing
workflow that improves clarity while preserving meaning, voice, and provenance.

## ADDED Requirements

### Requirement: Audit findings are actionable and advisory

The local prose audit SHALL report each stock-phrase match under its existing
category with a one-based line location and bounded excerpt. Document-level
patterns SHALL remain aggregate metrics or signals without fabricated source
locations. All results SHALL be advisory and SHALL NOT be presented as
authorship evidence, an AI-detection result, or a pass/fail score.

#### Scenario: Phrase pattern is found

- **WHEN** an English stock-phrase pattern is present in the input text
- **THEN** the audit reports its category, line location, and a short excerpt

#### Scenario: Aggregate pattern is found

- **WHEN** a document-level metric crosses an existing heuristic threshold
- **THEN** the audit reports an aggregate style cue without attributing it to
  an individual line or treating it as an authorship classification

#### Scenario: JSON output is requested

- **WHEN** the audit is run in JSON mode
- **THEN** it preserves the existing top-level fields and adds locations and
  excerpts within the existing stock-phrase results

### Requirement: Audit handles Unicode text without added dependencies

The audit SHALL count Unicode words, including accented Latin text, without
adding runtime dependencies. Its output SHALL identify phrase-pattern checks
as English-specific. Structural metrics SHALL remain language-neutral and
SHALL NOT silently treat accented letters as word boundaries.

#### Scenario: Accented prose is counted

- **WHEN** the audit receives prose containing accented words
- **THEN** those words are counted as complete words in the summary metrics

#### Scenario: Phrase-pattern scope is reported

- **WHEN** the audit reports its scope
- **THEN** it identifies stock-phrase checks as English-specific without
  attempting to detect the document language

### Requirement: Auditing does not rewrite or classify text

The local audit SHALL inspect text only. It SHALL NOT rewrite content, score
how human-like it appears, call an external service, or infer authorship.

#### Scenario: Audit is run on a file

- **WHEN** the user invokes the audit script
- **THEN** the input file remains unchanged and the script returns diagnostic
  output only

### Requirement: Revisions preserve supported meaning and provenance

The Codex editing workflow SHALL treat style findings as review cues, not
mandatory substitutions. It SHALL preserve claims, names, numbers, citations,
technical terms, negation, modality, qualifications, uncertainty, and
authorship or provenance disclosures unless the user requests and supports a
change. It SHALL review for both omitted source claims and unsupported new
claims before returning a revision.

#### Scenario: A flagged phrase is appropriate in context

- **WHEN** a heuristic flags wording that is clear and appropriate for its
  audience or genre
- **THEN** the editor may retain it rather than changing wording to reduce
  the audit count

#### Scenario: A revision changes a protected claim

- **WHEN** a proposed edit could change a claim, negation, certainty, number,
  citation, or provenance disclosure
- **THEN** the editor checks it against the source and preserves it unless a
  supported user-requested correction applies
