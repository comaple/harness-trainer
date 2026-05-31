# STORY-025: Ignore Local Secret Files

## Epic

EPIC-001

## Functional Requirements

- FR-005
- FR-011

## Non-Functional Requirements

- NFR-008

## User Story

As a project maintainer, I want local secret files to be ignored and rejected if
tracked so that tokens and environment-specific credentials are not uploaded to
GitHub.

## Implementation Plan

1. Add `.env` and `.env.*` to `.gitignore`.
2. Extend `scripts/ci_check.py` to require local secret ignore patterns.
3. Extend `scripts/ci_check.py` to reject tracked `.env` or `.env.*` files.
4. Verify `git check-ignore .env` succeeds locally.

## Acceptance Criteria

- `.env` is ignored.
- `.env.*` is ignored.
- `git ls-files` does not list local secret files.
- CI fails if local secret ignore patterns are removed.
