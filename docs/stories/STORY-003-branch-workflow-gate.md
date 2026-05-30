# STORY-003: Branch Workflow Gate

## Epic

EPIC-001

## Functional Requirements

- FR-007
- FR-005

## User Story

As a project maintainer, I want all sub-feature work to happen on `feat` and
merge into `main` only after gates pass so that the repository follows a simple
agile integration model.

## Implementation Plan

1. Document the `main` and `feat` branch roles in the architecture.
2. Update GitHub Actions to run on pushes to both `main` and `feat`.
3. Extend `scripts/ci_check.py` to validate branch flow when GitHub Actions
   environment variables are present.
4. Keep local execution permissive so developers can run the gate before any
   branch exists.

## Acceptance Criteria

- CI runs on pushes to `main` and `feat`.
- CI accepts pull requests from `feat` to `main`.
- CI rejects pull requests targeting a branch other than `main`.
- CI rejects pull requests whose source branch is not `feat`.
- Local `python3 scripts/ci_check.py` still runs outside GitHub Actions.

