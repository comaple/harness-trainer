# Source Extract

## GitHub Issue

- Issue: `#3`
- Title: `BR-001: Governed Harness Development`
- URL: `https://github.com/comaple/harness-trainer/issues/3`
- State when read: `open`

Issue text:

> The project must support a disciplined agile workflow where agent-harness
> changes are planned, traceable, reviewed, and gated before integration.

Issue acceptance:

- Requirement is decomposed into Epic/Story work before implementation.
- Any implementation commit references this issue, `BR-001`, and the relevant
  Story ID.

## PRD Extract

Source: `docs/prd.md`

`BR-001: Governed Harness Development`

> The project must support a disciplined agile workflow where agent-harness
> changes are planned, traceable, reviewed, and gated before integration.

Related governance requirements include:

- `FR-002`: Agile Requirement Traceability
- `FR-003`: Epic and Story Decomposition
- `FR-004`: Story Implementation Planning
- `FR-005`: Commit and CI Gate Traceability
- `FR-007`: Main and Work Branch Workflow
- `FR-008`: Work Branch Naming
- `FR-011`: Issue Category Taxonomy
- `FR-012`: Commit Issue Binding
- `NFR-008`: Local Secret Hygiene

## Epic Extract

Source: `docs/epics/EPIC-001-governance-and-gates.md`

`EPIC-001: Governance and Gates`

Goal:

> Establish the repository governance needed for agile harness development
> before feature implementation begins.

Acceptance criteria:

- The project has a PRD, architecture document, epic file, and story files.
- CI validates requirement traceability from PRD through code.
- CI validates the `<type>/<description>` -> `main` branch workflow.
- CI validates required PRD requirement classes.
- CI validates allowed issue categories.
- CI deletes merged work item branches.
- CI validates issue binding for every commit.
- CI validates local secret files are ignored and untracked.
- Code changes include traceability markers.
- Commit messages can be checked for FR and Story IDs.

## Story Extract

Initial stories implementing the governance spine:

- `STORY-001`: Project Charter
- `STORY-002`: Traceability Gate
- `STORY-003`: Branch Workflow Gate
- `STORY-004`: Work Branch Naming
- `STORY-005`: PRD Requirement Classes
- `STORY-006`: Delete Merged Work Branches
- `STORY-007`: Issue Category Taxonomy
- `STORY-008`: Commit Issue Binding
- `STORY-025`: Ignore Local Secret Files

## Preservation Notes

- The issue's core business requirement is preserved in `SPEC.md` Why and
  Success signal.
- The issue's acceptance criteria are preserved in `CAP-2` and `CAP-3`.
- The PRD/Epic governance details are preserved as constraints and capability
  success criteria.

