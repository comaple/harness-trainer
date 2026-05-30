# EPIC-001: Governance and Gates

## Goal

Establish the repository governance needed for agile harness development before
feature implementation begins.

## Functional Requirements

- FR-001
- FR-002
- FR-003
- FR-004
- FR-005
- FR-006
- FR-007
- FR-008
- FR-009
- FR-010
- FR-011
- FR-012

## Stories

- STORY-001: Create the project charter and README.
- STORY-002: Add traceability and CI quality gates.
- STORY-003: Enforce the main/feat branch workflow.
- STORY-004: Enforce feature branch naming.
- STORY-005: Add PRD requirement class governance.
- STORY-006: Delete merged feature branches.
- STORY-007: Define issue category branch taxonomy.
- STORY-008: Require issue binding on commits.

## Acceptance Criteria

- The project has a PRD, architecture document, epic file, and story files.
- CI validates requirement traceability from PRD through code.
- CI validates the `<type>/<description>` -> `main` branch workflow.
- CI validates required PRD requirement classes.
- CI validates allowed issue categories.
- CI deletes merged work item branches.
- CI validates issue binding for every commit.
- Code changes include traceability markers.
- Commit messages can be checked for FR and Story IDs.
