# Plugin Marketplace Integrity Specification

## Purpose

Ensure marketplace listings only advertise installable skill packages and make missing package structure fail before release.

## Requirements

### Requirement: Listed Codex packages are structurally installable
The Codex marketplace SHALL reference a plugin root that contains a `.codex-plugin/plugin.json` manifest and a bundled `skills/` directory for every listed skills plugin.

#### Scenario: Research plugin is resolved from the Codex marketplace
- **WHEN** a maintainer resolves the `relentless-web-researcher` marketplace entry
- **THEN** its plugin root contains the required Codex manifest and its bundled skills directory

#### Scenario: A listed package is incomplete
- **WHEN** a Codex marketplace entry resolves to a root without its required manifest or skills directory
- **THEN** structural validation fails and identifies the affected marketplace entry and missing path

### Requirement: Marketplace structure is checked reproducibly
The repository SHALL provide a focused, dependency-free validation check for its checked-in marketplace entries and their declared package structure.

#### Scenario: All catalog entries resolve
- **WHEN** the focused validation check runs against the checked-in catalogs
- **THEN** it succeeds only when every checked entry resolves to its required package structure

#### Scenario: A catalog path becomes invalid
- **WHEN** a marketplace source path no longer resolves to its plugin root
- **THEN** the focused validation check fails without requiring a host installation

### Requirement: Marketplace identities match package identities
The repository SHALL provide a focused, dependency-free check that verifies each checked-in Codex and Claude marketplace plugin ID matches the name in its host package manifest. The More With Less package and both marketplace entries SHALL use `more-with-less`; they SHALL NOT advertise `s-kit` as a current ID.

#### Scenario: Renamed package is listed consistently
- **WHEN** a maintainer checks the More With Less entries in both marketplaces
- **THEN** each entry resolves to the `more-with-less` package and matching host manifest name

#### Scenario: Marketplace name differs from the package
- **WHEN** a checked-in entry uses a name different from its host manifest
- **THEN** the focused validation check fails and identifies that entry
