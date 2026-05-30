# STORY-001: Project Charter

## Epic

EPIC-001

## Functional Requirements

- FR-001
- FR-002

## User Story

As a project maintainer, I want a clear project charter and agent working rules
so that contributors understand the repository purpose and boundaries before
implementation starts.

## Implementation Plan

1. Create `AGENTS.md` with repository-specific agent rules.
2. Create `README.md` with the project purpose, references, non-goals, and
   starting point.
3. Explicitly separate `harness-trainer` from the sibling `autoresearch`
   reference checkout.

## Acceptance Criteria

- `AGENTS.md` exists and defines commit rules.
- `README.md` exists and links to `AGENTS.md`.
- Documentation says not to modify or submit sibling `autoresearch` changes.

