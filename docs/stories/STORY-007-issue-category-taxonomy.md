# STORY-007: Issue Category Taxonomy

## Epic

EPIC-001

## Functional Requirements

- FR-011
- FR-010
- FR-008
- FR-007
- FR-005

## User Story

As a project maintainer, I want a controlled issue category taxonomy for branch
names so that work type is visible and CI can consistently validate branch
flows.

## Implementation Plan

1. Add `FR-011` to the PRD with the allowed issue categories.
2. Update architecture, README, and agent rules from feature-only branches to
   allowed work item branches.
3. Update GitHub Actions branch triggers for every allowed category.
4. Update branch-flow validation in `scripts/ci_check.py` to accept only
   allowed `<type>/<description>` branches.
5. Update merged branch cleanup to delete all allowed work item branches, not
   only `feat/...`.

## Acceptance Criteria

- Allowed branch prefixes are `feat`, `fix`, `docs`, `test`, `refactor`, `ci`,
  `chore`, `perf`, and `security`.
- Bare category branch names such as `feat` and `docs` fail validation.
- Unknown categories such as `feature/...` and `bugfix/...` fail validation.
- Valid examples such as `docs/prd-rules` and `ci/delete-merged-branches` pass.
- Merged branches from allowed categories are eligible for automatic cleanup.
