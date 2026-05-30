# STORY-004: Work Branch Naming

## Epic

EPIC-001

## Functional Requirements

- FR-008
- FR-007
- FR-005

## User Story

As a project maintainer, I want development branches to include an issue
category and work description in `<type>/<description>` format so that branch
purpose is visible before opening a PR.

## Implementation Plan

1. Add `FR-008` to the PRD for work branch naming.
2. Document the naming rule in the architecture, README, and agent rules.
3. Update CI triggers from bare category names to `<type>/**` patterns.
4. Extend `scripts/ci_check.py` to reject bare category names and malformed work
   branch names in GitHub Actions.

## Acceptance Criteria

- Valid work branch examples: `feat/branch-naming-rules`, `docs/prd-rules`,
  and `ci/delete-merged-branches`.
- Invalid work branch examples: `feat`, `feature/branch-naming-rules`, `feat/`,
  and `feat/branch naming rules`.
- PRs from valid `<type>/<description>` branches to `main` pass the branch-flow
  check.
- PRs from any other branch pattern fail the branch-flow check.
