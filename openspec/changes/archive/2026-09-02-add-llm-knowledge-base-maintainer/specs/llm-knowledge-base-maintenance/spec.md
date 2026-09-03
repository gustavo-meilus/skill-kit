## Purpose

Provide a reusable workflow for creating and maintaining concise Markdown reference collections whose portable LLM indexes remain complete, current, and grounded in authoritative source material.

## ADDED Requirements

### Requirement: Maintenance scope follows the user's intent
The skill SHALL support creating, revising, expanding, reorganizing, auditing, and explicitly authorized removal of LLM-oriented reference collections. It SHALL use supplied context and inspect an existing target collection before changing it, and SHALL ask for input only when the target or authoritative content cannot be determined safely.

#### Scenario: New collection is requested
- **WHEN** the user provides a target and usable source material for a new reference collection
- **THEN** the skill creates the collection and its portable indexes without requiring unrelated configuration

#### Scenario: Existing collection is changed
- **WHEN** the user asks to revise, expand, reorganize, audit, or remove content from an existing collection
- **THEN** the skill inspects the current references and indexes before applying the requested maintenance operation

#### Scenario: Required authority is missing
- **WHEN** the requested reference facts cannot be established from supplied, repository, or otherwise authorized sources
- **THEN** the skill identifies the missing authority instead of inventing the content

### Requirement: Canonical references are retrieval-ready
The skill SHALL keep canonical reference content in Markdown pages that use stable document identities, consistent terminology, descriptive hierarchy, concise factual prose, and sufficient local context for a retrieved section to remain interpretable. Each page SHALL record a title and summary plus applicable version, update, and provenance information. Related references SHALL use resolvable cross-links when their relationship materially helps navigation.

#### Scenario: Reference page is created
- **WHEN** the skill adds a reference topic
- **THEN** the resulting Markdown page has a stable identity, concise purpose, structured factual content, and the metadata applicable to its sources and lifecycle

#### Scenario: Reference page is revised
- **WHEN** the meaning or wording of an existing reference changes without replacing its logical topic
- **THEN** the page retains its stable identity and uses the collection's established terminology and structure

#### Scenario: Related reference is added
- **WHEN** a new reference has a material relationship to an existing reference
- **THEN** the relevant pages contain resolvable cross-links that make the relationship navigable

### Requirement: Portable indexes remain synchronized
The skill SHALL maintain a curated `llms.txt` navigation map and an exhaustive `manifest.jsonl` inventory from the current canonical references. Index entries SHALL resolve to existing references, use their stable identities and metadata, and exclude references removed within the authorized task.

#### Scenario: Collection is created
- **WHEN** the skill completes a new reference collection
- **THEN** `llms.txt` describes and links its useful entry points and `manifest.jsonl` contains one current inventory entry for every canonical reference

#### Scenario: Reference is added or revised
- **WHEN** a canonical reference is added or its index-relevant metadata changes
- **THEN** both static indexes reflect the new current collection without duplicate identities

#### Scenario: Reference is removed
- **WHEN** the user explicitly authorizes removal of a canonical reference
- **THEN** the reference and all of its stale index entries are absent after maintenance completes

### Requirement: Existing collections and unrelated content are preserved
The skill SHALL reuse an existing collection's equivalent layout, metadata, naming, and index conventions. When no usable convention exists, it SHALL establish only the minimal documented structure needed for the references and portable indexes. It SHALL leave unrelated files and reference content outside the requested scope unchanged.

#### Scenario: Equivalent conventions already exist
- **WHEN** the target collection already represents stable identity, metadata, and static indexes in an equivalent form
- **THEN** the skill follows those conventions instead of introducing a parallel schema or layout

#### Scenario: No conventions exist
- **WHEN** a new or unstructured target has no equivalent knowledge-base convention
- **THEN** the skill creates a minimal layout and records enough format guidance for later maintenance

#### Scenario: One reference is revised
- **WHEN** a maintenance request affects one reference and its index entries
- **THEN** unrelated reference pages remain unchanged

### Requirement: Claims preserve evidence and uncertainty
The skill SHALL ground reference claims in authoritative available sources, preserve provenance needed to review them, and distinguish established facts from unresolved conflicts or missing evidence. It SHALL not silently choose among materially conflicting sources or publish unsupported claims as facts.

#### Scenario: Sources conflict
- **WHEN** authoritative sources materially disagree about a reference fact
- **THEN** the skill records or reports the conflict and does not assert an unsupported resolution

#### Scenario: Evidence is insufficient
- **WHEN** available sources do not support a requested claim
- **THEN** the skill leaves the claim unresolved and identifies the evidence gap

### Requirement: Completion includes integrity validation
Before reporting completion, the skill SHALL validate the maintained scope for missing or invalid required reference metadata, duplicate document identities, unresolved internal links, missing referenced files, stale or duplicate manifest entries, and disagreement between canonical references and both portable indexes. It SHALL repair in-scope defects when authorized and otherwise report them without claiming a clean result.

#### Scenario: Maintained collection is consistent
- **WHEN** all relevant integrity checks pass after a create or maintenance operation
- **THEN** the skill reports the changed scope and the checks that passed

#### Scenario: Integrity defect remains
- **WHEN** an integrity defect cannot be repaired within the authorized scope
- **THEN** the skill identifies the defect and does not report the collection as fully synchronized

#### Scenario: Required metadata is invalid
- **WHEN** a canonical reference lacks required metadata or contains a metadata value invalid under the collection's conventions
- **THEN** the integrity result identifies the reference and invalid field until the defect is repaired

### Requirement: Invocation remains discriminating
The skill SHALL be discoverable for requests to create or maintain LLM-ready reference knowledge bases and SHALL avoid capturing ordinary prose editing, unrelated deep research, website generation, or requests concerned only with vector or hosted retrieval infrastructure.

#### Scenario: Knowledge-base maintenance is requested
- **WHEN** a user asks to create, revise, update, expand, reorganize, or audit an LLM-ready reference collection
- **THEN** the skill applies its reference and static-index maintenance workflow

#### Scenario: Adjacent task is requested
- **WHEN** a request concerns only general documentation prose, deep research, website deployment, embeddings, vector databases, or hosted RAG infrastructure
- **THEN** the skill does not claim that request as knowledge-base maintenance
