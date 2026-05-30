# STORY-005: PRD Requirement Classes

## Epic

EPIC-001

## Functional Requirements

- FR-009
- FR-005

## User Story

As a project maintainer, I want the PRD to distinguish functional requirements
from business, user, non-functional, constraint, dependency, scope, and metric
sections so that agile planning captures the whole product contract.

## Implementation Plan

1. Add a requirement taxonomy to `docs/prd.md`.
2. Add business, user, non-functional, constraints, assumptions/dependencies,
   out-of-scope, and success metric sections to the PRD.
3. Update architecture and agent rules to explain how non-FR requirements are
   used.
4. Extend `scripts/ci_check.py` so CI rejects PRDs that omit required
   requirement classes or stable IDs.
5. Keep functional requirements as the implementation traceability anchor for
   epics, stories, source files, and commits.

## Acceptance Criteria

- `docs/prd.md` includes all required PRD sections.
- PRD business, user, functional, and non-functional requirements use stable
  IDs.
- CI fails if a required PRD section is removed.
- CI fails if core PRD requirement classes lack IDs.
- Existing FR -> Epic -> Story -> Code traceability still passes.
