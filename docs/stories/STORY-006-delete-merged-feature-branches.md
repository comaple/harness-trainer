# STORY-006: Delete Merged Work Branches

## Epic

EPIC-001

## Functional Requirements

- FR-010
- FR-008
- FR-007
- FR-005

## User Story

As a project maintainer, I want merged allowed `<type>/<description>` branches
to be deleted automatically after successful merge so that the remote repository
does not accumulate stale development branches.

## Implementation Plan

1. Add `FR-010` to the PRD for merged work branch cleanup.
2. Document cleanup behavior and safety boundaries in the architecture.
3. Add this story to the governance epic.
4. Extend `.github/workflows/ci.yml` with a `delete-merged-work-branch` job
   triggered by `pull_request.closed`.
5. Guard deletion with checks for `merged == true`, base branch `main`, and head
   branch matching an allowed `<type>/<description>`.
6. Use `contents: write` only on the cleanup job.

## Acceptance Criteria

- Merged PRs from allowed `<type>/<description>` branches to `main` delete the
  remote work branch.
- Closed but unmerged PRs do not delete the branch.
- PRs from unsupported branch patterns do not delete the branch.
- The cleanup job cannot delete `main`.
- The quality gate still passes locally and in PR simulation.
