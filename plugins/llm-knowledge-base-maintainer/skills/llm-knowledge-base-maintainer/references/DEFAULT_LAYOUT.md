# Default collection layout

Use this only when the target has no equivalent convention.

```text
references/
  topic.md
llms.txt
manifest.jsonl
```

Each canonical page has YAML frontmatter:

```yaml
id: stable-topic-id
title: Human-readable title
summary: One factual sentence.
version: Applicable version or "unversioned"
updated: YYYY-MM-DD
provenance:
  - Authoritative source and date or version
```

The body uses descriptive headings, concise factual prose, and relative Markdown links for material relationships. Keep `id` stable when the page moves or is renamed.

`llms.txt` starts with the collection name and a short purpose, then lists useful entry points as Markdown links. It is curated navigation, not an inventory.

`manifest.jsonl` contains one JSON object per canonical page, with at least `id`, `title`, `summary`, `path`, `version`, `updated`, and `provenance`. Paths are relative to the collection root. Match the page's current metadata exactly; do not include `llms.txt`, the manifest, or removed pages.

Before completion, scan every canonical page and both indexes. Check required metadata and dates, duplicate IDs, relative links and target files, every manifest path and ID, no duplicate manifest entry, and that each canonical page appears once in the manifest and appropriately in `llms.txt`.
