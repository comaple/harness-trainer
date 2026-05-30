# STORY-003: Branch Workflow Gate

## Epic

EPIC-001

## Functional Requirements

- FR-007
- FR-005

## User Story

As a project maintainer, I want all issue-driven work to happen on named
`<type>/<description>` branches and merge into `main` only after gates pass so
that the repository follows a simple agile integration model.

## Implementation Plan

1. Document the `main` and `<type>/<description>` branch roles in the
   architecture.
2. Update GitHub Actions to run on pushes to `main` and allowed work branches.
3. Extend `scripts/ci_check.py` to validate branch flow when GitHub Actions
   environment variables are present.
4. Keep local execution permissive so developers can run the gate before any
   branch exists.

## Acceptance Criteria

- CI runs on pushes to `main` and allowed work branch patterns.
- CI accepts pull requests from valid `<type>/<description>` branches to `main`.
- CI rejects pull requests targeting a branch other than `main`.
- CI rejects pull requests whose source branch is not a valid work item branch.
- Local `python3 scripts/ci_check.py` still runs outside GitHub Actions.
