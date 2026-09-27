# Design: Improve AI fingerprint audit

## Context

See `proposal.md` for motivation and
`specs/ai-fingerprint-mitigation/spec.md` for behavior requirements. The
current audit is a single standard-library script that emits aggregate
metrics, heuristic flags, and partial phrase matches. The Codex skill owns
the actual prose revision and semantic review.

## Goals / Non-Goals

**Goals:**

- Add useful source locations and bounded excerpts to stock-phrase hits.
- Count Unicode words correctly while retaining a dependency-free script.
- Make the Codex revision check more explicit about claim-level changes.
- Preserve the existing audit's aggregate metrics and advisory nature.

**Non-Goals:**

- No text rewriting, authorship classification, detector scoring, or evasion.
- No external API, model download, NLP library, or runtime dependency.
- No general multilingual phrase catalog or Markdown parser.

## Decisions

1. **Enrich the existing result instead of adding another output model.**
   Keep the current top-level metrics, stock-phrase groups, repeated openers,
   and signals. Format each stock-phrase hit as a bounded string containing
   its one-based line number and excerpt. Keep repeated openers and other
   document-level patterns aggregate. This avoids a duplicate `findings`
   collection and preserves the existing JSON shape.

2. **Use Python's Unicode-aware regular expressions for word counting.**
   Keep the existing English phrase patterns and structural heuristics.
   Record line numbers against the original input so locations do not depend
   on text rewriting or normalization.

3. **Disclose scope without detecting language.** State in the audit output
   that stock-phrase checks are English-specific. Keep structural metrics
   language-neutral. Language detection would add cost and uncertain behavior
   without improving the requested audit.

4. **Keep findings advisory and editing in Codex.** The script reports
   possible style patterns; the skill decides whether they matter in context.
   Update the semantic checklist in the existing revision protocol instead
   of adding an NLP model or another tool stage.

5. **Add two focused regression cases.** Cover Unicode counts plus scope
   disclosure in one case, and located bounded phrase hits plus retained JSON
   keys in the other. Use the repository's existing test setup; do not add a
   testing dependency.

## Risks / Trade-offs

- **Heuristics may flag correct prose or code examples** → keep findings
  advisory, bounded, and contextual; do not auto-rewrite.
- **Line numbers can drift if offsets are computed from transformed text**
  → derive locations from the original input only.
- **Unicode word boundaries vary across scripts and tokenization conventions**
  → define this as a word-count improvement, not language-aware linguistic
  analysis; add language-specific rules only for a demonstrated need.

## Migration Plan

No migration is required. Preserve existing JSON fields and add location
details within `stock_phrase_hits`. No dependency or configuration changes
are planned.
