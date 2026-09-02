# Relentless Web Research Specification

## Purpose

Provide reusable, current, evidence-backed research that builds session-level expertise on a main topic and optional specialties without overstating certainty or persistence.

## Requirements

### Requirement: Research scope follows the user's intent
The skill SHALL accept a main topic, optional subtopics, and an optional practical goal, using supplied details without asking the user to repeat them. It SHALL ask for the main topic only when no usable topic can be inferred, and SHALL otherwise begin research without blocking on absent subtopics or a goal.

#### Scenario: Topic, specialties, and goal are supplied
- **WHEN** the user supplies a main topic, one or more subtopics, and a practical goal
- **THEN** the research covers the main topic, develops added depth in the subtopics, and shapes the synthesis toward the goal

#### Scenario: Only a main topic is supplied
- **WHEN** the user supplies a usable main topic without subtopics or a practical goal
- **THEN** the research covers the topic's material foundations and clearly identifies the focus it selected

### Requirement: Research is current and source-led
The skill SHALL browse rather than rely solely on prior model knowledge. It SHALL prioritize applicable primary sources such as official documentation, standards, original research, and source documents, then use reputable expert publications for context, critique, and interpretation. Source selection SHALL account for publication date, subject-matter authority, independence, and relevance to the claim.

#### Scenario: Topic changes rapidly
- **WHEN** the topic includes versioned tools, recent events, evolving standards, or other time-sensitive facts
- **THEN** the skill verifies those facts against current authoritative sources and identifies the applicable dates or versions

#### Scenario: Primary sources do not resolve a material question
- **WHEN** available primary sources are incomplete, inaccessible, disputed, or silent on a material question
- **THEN** the skill consults the strongest available independent secondary evidence and discloses the limitation

### Requirement: Research covers material questions iteratively
The skill SHALL identify the material questions needed to understand the topic and the user's specialties or goal, search and read iteratively, and follow consequential findings into additional sources. It SHALL revisit the question set when research reveals a material missing concept, dependency, disagreement, or risk.

#### Scenario: Research reveals an unanticipated dependency
- **WHEN** a source shows that understanding the requested topic depends on another material concept or tool
- **THEN** the skill adds that dependency to the research scope and explains its relevance in the synthesis

### Requirement: Claims preserve evidence and uncertainty
The synthesis SHALL cite sources close to the claims they support, distinguish sourced facts from analysis or inference, and state material uncertainty, disagreement, or missing evidence. It SHALL not present session research as permanent model training or durable knowledge beyond the active context.

#### Scenario: Trustworthy sources conflict
- **WHEN** trustworthy sources make materially conflicting claims
- **THEN** the skill presents the conflict, evaluates the likely reasons and evidentiary weight, and avoids asserting an unsupported resolution

#### Scenario: A conclusion is inferred
- **WHEN** the synthesis reaches a useful conclusion not directly stated by a source
- **THEN** the skill labels it as an inference and cites the evidence from which it was derived

### Requirement: Related approaches are compared
The skill SHALL identify relevant adjacent tools, technologies, methods, or schools of thought and compare where they overlap, complement, contradict, or outperform the main topic. Comparisons SHALL use criteria relevant to the user's goal and SHALL avoid false equivalence.

#### Scenario: A practical goal is supplied
- **WHEN** the user supplies a practical goal and credible alternatives exist
- **THEN** the synthesis compares the main topic and alternatives on the trade-offs that materially affect that goal

#### Scenario: No credible direct alternative exists
- **WHEN** research finds no credible direct alternative to the main topic
- **THEN** the synthesis limits comparison to genuinely adjacent or complementary approaches and says that no direct alternative was established

### Requirement: Completion is bounded by evidence
The skill SHALL continue until material questions are covered, consequential claims have appropriate support, comparisons are addressed where relevant, and further searching produces diminishing decision value. It SHALL disclose remaining gaps and give a concise synthesis by default, expanding only as the topic or requested deliverable requires.

#### Scenario: Further searches repeat known evidence
- **WHEN** additional credible searches repeat established findings without changing conclusions or exposing material gaps
- **THEN** the skill stops researching and delivers the synthesis

#### Scenario: A material gap remains unresolved
- **WHEN** a material question cannot be resolved with available trustworthy evidence
- **THEN** the skill stops after reasonable avenues are exhausted, identifies the gap, and explains how it limits the conclusions
