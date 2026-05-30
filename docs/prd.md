# Product Requirements Document

## Product

`harness-trainer` is an agile project for training and improving agent
harnesses. The product must preserve a traceable path from requirement to epic
to story to implementation to commit.

## Requirement Taxonomy

Every PRD must separate these requirement classes:

- Business Requirements (`BR-XXX`): business outcomes, operating model, and
  governance goals.
- User Requirements (`UR-XXX`): needs of maintainers, contributors, reviewers,
  and agent operators.
- Functional Requirements (`FR-XXX`): behavior the system must provide.
- Non-Functional Requirements (`NFR-XXX`): quality attributes such as security,
  reliability, maintainability, usability, auditability, performance, and
  observability.
- Constraints: technical, process, compliance, dependency, and schedule limits.
- Assumptions and Dependencies: conditions the plan relies on.
- Out of Scope: explicit non-goals.
- Success Metrics: measurable evidence that the product is working.

Functional requirements drive epic and story decomposition. Non-functional
requirements must be reflected in acceptance criteria, architecture decisions,
or quality gates when relevant.

## Business Requirements

### BR-001: Governed Harness Development

The project must support a disciplined agile workflow where agent-harness
changes are planned, traceable, reviewed, and gated before integration.

## User Requirements

### UR-001: Maintainer Traceability

Maintainers must be able to inspect a change and identify the originating
requirement, epic, story, implementation plan, and commit.

### UR-002: Agent Operating Clarity

Agents working in the repository must have clear rules for branch naming,
editable surfaces, required checks, and evidence before implementation.

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

The repository must use `main` as the integration branch and `feat/<feature>`
branches as development branches. Sub-feature work is performed on a named
`feat/<feature>` branch, validated by gates, and then merged into `main`.

### FR-008: Feature Branch Naming

Every development branch must use the `feat/<feature-description>` format. The
description must identify the function being changed, for example
`feat/branch-naming-rules` or `feat/ci-gates`. The bare branch name `feat` is
not allowed for implementation work.

### FR-009: PRD Requirement Classes

The PRD must define and preserve the project requirement classes beyond
functional requirements, and CI must reject PRDs that omit required classes.

## Non-Functional Requirements

### NFR-001: Auditability

The repository must preserve enough structured evidence for reviewers to audit
why a change exists and whether it followed the agile process.

### NFR-002: Maintainability

Gate logic must remain dependency-free and small enough to run locally and in CI
without bootstrapping a separate toolchain.

### NFR-003: Fail-Closed Governance

When CI cannot prove that PRD, epic, story, code, and commit metadata are
consistent, it must reject the change.

## Constraints

- The early quality gate must use only the Python standard library.
- All implementation branches must follow `feat/<feature-description>`.
- The sibling `autoresearch` checkout is reference material only and must not be
  modified or submitted as part of this project.

## Assumptions and Dependencies

- GitHub Actions is the initial CI environment.
- BMad artifacts may be added later, but the core gate must remain runnable
  without BMad-specific commands.
- The repository uses Markdown documents as the source of product truth until a
  richer issue tracker is introduced.

## Out of Scope

- Training language models.
- Tuning the sibling `autoresearch` benchmark.
- Building a large harness runtime before the agile planning and gate spine is
  stable.

## Success Metrics

- CI can validate the PRD -> Epic -> Story -> Code chain without external
  dependencies.
- A reviewer can identify why a code change exists from IDs in the commit and
  source file.
- No code is merged without a corresponding story implementation plan.
- CI rejects unsupported branch flows and malformed feature branch names when
  running in GitHub Actions.
- CI rejects PRDs that omit required requirement classes.
