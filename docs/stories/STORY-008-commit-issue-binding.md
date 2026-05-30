# STORY-008: Commit Issue Binding

## Epic

EPIC-001

## Functional Requirements

- FR-012
- FR-005

## User Story

As a project maintainer, I want every commit to reference an issue so that each
code or documentation change can be traced back to a tracked work item.

## Implementation Plan

1. Add `FR-012` to the PRD for commit issue binding.
2. Document the accepted issue reference formats in README and agent rules.
3. Update CI checkout settings so commit history is available during PR checks.
4. Extend `scripts/ci_check.py` so every checked commit message must include
   `ISSUE-123` or `#123`, in addition to valid FR and Story IDs.
5. Keep local execution permissive when no CI commit range is available.

## Acceptance Criteria

- Commits containing `ISSUE-123`, `FR-XXX`, and `STORY-XXX` pass commit-message
  validation.
- Commits containing `#123`, `FR-XXX`, and `STORY-XXX` pass commit-message
  validation.
- Commits missing an issue reference fail commit-message validation in CI.
- Existing FR and Story commit-message checks remain active.
