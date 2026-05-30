# STORY-004: Feature Branch Naming

## Epic

EPIC-001

## Functional Requirements

- FR-008
- FR-007
- FR-005

## User Story

As a project maintainer, I want development branches to include the function
name in `feat/<feature-description>` format so that branch purpose is visible
before opening a PR.

## Implementation Plan

1. Add `FR-008` to the PRD for feature branch naming.
2. Document the naming rule in the architecture, README, and agent rules.
3. Update CI triggers from bare `feat` to `feat/**`.
4. Extend `scripts/ci_check.py` to reject bare `feat` and malformed feature
   branch names in GitHub Actions.
5. Rename the current local development branch to `feat/branch-naming-rules`.

## Acceptance Criteria

- Valid feature branch example: `feat/branch-naming-rules`.
- Invalid feature branch examples: `feat`, `feature/branch-naming-rules`,
  `feat/`, and `feat/branch naming rules`.
- PRs from valid `feat/<feature-description>` branches to `main` pass the
  branch-flow check.
- PRs from any other branch pattern fail the branch-flow check.
