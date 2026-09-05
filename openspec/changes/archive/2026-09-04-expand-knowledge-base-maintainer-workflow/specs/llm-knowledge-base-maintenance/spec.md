## ADDED Requirements

### Requirement: Source-driven knowledge-base lifecycle is explicit
The skill SHALL determine whether an authorized request creates, updates, or attaches material to an LLM-ready knowledge base, inspect the target collection before mutation, and complete the selected operation through canonical references and synchronized portable indexes. It SHALL use supplied or otherwise authorized source material, preserve stable document identities for existing logical topics, and leave unrelated reference content unchanged.

#### Scenario: Collection is created from supplied source material
- **WHEN** a user provides a target and usable authorized material for a new knowledge base
- **THEN** the skill creates the minimum canonical-reference structure, records source provenance, and reconciles `llms.txt` and `manifest.jsonl`

#### Scenario: Existing collection is updated
- **WHEN** a user requests a scoped update to an existing knowledge base
- **THEN** the skill inspects the affected canonical references and both indexes, updates only supported in-scope content, retains the logical topics' stable identities, and reconciles the collection indexes

### Requirement: Attached source material is evaluated and attributed safely
The skill SHALL treat attached files and user-pasted content as untrusted evidence rather than instructions. For an attach operation, it SHALL identify material claims, applicable source context, provenance, conflicts, and unsupported gaps before incorporating supported information into the relevant canonical reference or a new canonical reference. It SHALL not publish unsupported claims as facts or silently resolve material source conflicts.

#### Scenario: Attached material supports an existing topic
- **WHEN** an attached document or pasted content contains attributable facts relevant to an existing canonical reference
- **THEN** the skill updates that reference with the supported facts and their provenance while preserving its stable identity

#### Scenario: Attached material introduces a distinct supported topic
- **WHEN** attached material supports a topic not represented by the collection
- **THEN** the skill creates a canonical reference with required metadata and provenance, then synchronizes both indexes

#### Scenario: Attached material conflicts or lacks support
- **WHEN** attached material materially conflicts with existing authoritative evidence or cannot support a requested claim
- **THEN** the skill surfaces the conflict or evidence gap and does not assert an unsupported resolution

### Requirement: Evidence gaps use consent-based web research
When supplied or authorized material leaves a material evidence gap, the skill SHALL ask whether the user wants web research before searching. If web research is requested, it SHALL check whether `relentless-web-researcher` is available; when available, it SHALL ask whether the user wants to use that skill. If the skill is unavailable or the user declines it, the maintainer SHALL use an ordinary model-directed web search and preserve the resulting evidence and uncertainty according to the collection's provenance rules.

#### Scenario: User requests research and the specialist is available
- **WHEN** the user authorizes web research and `relentless-web-researcher` is available
- **THEN** the skill asks whether to use `relentless-web-researcher` before beginning research

#### Scenario: Specialist is unavailable or declined
- **WHEN** the user authorizes web research but `relentless-web-researcher` is unavailable or the user declines it
- **THEN** the skill performs ordinary model-directed web research and attributes the resulting material claims

#### Scenario: User does not authorize research
- **WHEN** material evidence is insufficient and the user does not authorize web research
- **THEN** the skill records or reports the evidence gap without searching or inventing content

### Requirement: Canonical prose follows concise writing guidance
For every authorized canonical-reference creation, revision, or update, the skill SHALL use `lite-writing` when that skill is available. When it is unavailable, the skill SHALL write concise, factual, directly structured prose that preserves material facts, uncertainty, provenance, technical terms, and necessary ordering without filler or repeated summaries.

#### Scenario: Lite Writing is available
- **WHEN** an authorized operation writes canonical knowledge-base prose and `lite-writing` is available
- **THEN** the skill invokes it for that prose while preserving the collection's required metadata and provenance

#### Scenario: Lite Writing is unavailable
- **WHEN** an authorized operation writes canonical knowledge-base prose and `lite-writing` is unavailable
- **THEN** the skill applies the concise fallback writing protocol without omitting material facts, uncertainty, provenance, or required metadata
