# Plugin Marketplace Integrity Delta

## ADDED Requirements

### Requirement: Marketplace identities match package identities

The repository SHALL provide a focused, dependency-free check that verifies
each checked-in Codex and Claude marketplace plugin ID matches the name in its
host package manifest. The More With Less package and both marketplace entries
SHALL use `more-with-less`; they SHALL NOT advertise `s-kit` as a current ID.

#### Scenario: Renamed package is listed consistently

- **WHEN** a maintainer checks the More With Less entries in both marketplaces
- **THEN** each entry resolves to the `more-with-less` package and matching
  host manifest name

#### Scenario: Marketplace name differs from the package

- **WHEN** a checked-in entry uses a name different from its host manifest
- **THEN** the focused validation check fails and identifies that entry
