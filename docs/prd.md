# Product Requirements Document

## Product

`harness-trainer` is an agile project for training and improving agent
harnesses. The product must preserve a traceable path from requirement to epic
to story to implementation to commit.

## Functional Requirements

### FR-001: Project Charter

The repository must define its purpose, non-goals, reference methodology, and
agent working rules in project-owned documentation.

### FR-002: Agile Requirement Traceability

Every product requirement must be declared in this PRD with a stable `FR-XXX`
identifier before implementation work begins.

### FR-003: Epic and Story Decomposition

Every functional requirement selected for implementation must be decomposed in
an epic document, and each epic must list the stories that implement it.

### FR-004: Story Implementation Planning

Every story must include a concrete implementation plan before code is changed
for that story.

### FR-005: Commit and CI Gate Traceability

Every code change must bind back to at least one `FR-XXX` requirement and one
`STORY-XXX` story. CI must reject changes when documentation, code, and commit
metadata are inconsistent.

### FR-006: System Architecture

The project must maintain an architecture document describing the major
components, boundaries, and quality gates for the harness-training system.

### FR-007: Main and Feat Branch Workflow

The repository must use `main` as the integration branch and `feat` as the
development branch. Sub-feature work is performed on `feat`, validated by gates,
and then merged into `main`.

## Success Metrics

- CI can validate the PRD -> Epic -> Story -> Code chain without external
  dependencies.
- A reviewer can identify why a code change exists from IDs in the commit and
  source file.
- No code is merged without a corresponding story implementation plan.
- CI rejects unsupported branch flows when running in GitHub Actions.
