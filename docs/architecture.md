# Architecture

## Overview

`harness-trainer` uses documentation-first traceability as the first system
boundary. Requirements are declared in the PRD, decomposed in epics, planned in
stories, and enforced by a local CI gate.

The product boundary is enterprise business Agent Harness delivery. A business
team brings business goals, a business PRD, and a business environment. The
system produces an Agent Harness blueprint, worker contracts, environment
integration plan, evaluator plan, implementation evidence, and training loop for
that business Agent Harness.

## Components

### Documentation Kernel

- PRD: `docs/prd.md`
- Epics: `docs/epics/`
- Stories: `docs/stories/`
- Project rules: `AGENTS.md`

The documentation kernel is the source of truth for product intent and agile
decomposition.

### Quality Gate

- Local script: `scripts/ci_check.py`
- GitHub workflow: `.github/workflows/ci.yml`

The gate validates repository hygiene, required files, Markdown links, agile
traceability, code traceability, and commit-message traceability.

### Future Harness Runtime

Future implementation should add a `harness/` package only after stories define
its behavior. Expected runtime boundaries include turn orchestration, policy,
approval, budget, session persistence, event streams, and evaluation.

The planned harness runtime is decomposed into replaceable capabilities:

- capability catalog and worker contract model
- turn intake and orchestration
- provider, credential, and model capability layer
- skill discovery and prompt assembly
- policy and approval gates
- budget tracking, hooks, and side effects
- session storage, memory, and context compaction
- event streaming and end-to-end tracing
- harness training evaluator

Each capability must declare its public contract, state boundary, failure
semantics, emitted events, and trace evidence before code is introduced.

### Business Agent Delivery Pipeline

The delivery pipeline is:

```text
Business Goal
  -> Business PRD
  -> Business Environment Inventory
  -> Business Agent Harness Blueprint
  -> Worker Contracts
  -> Harness Runtime / Implementation Plan
  -> Business Evaluator
  -> CI Evidence + Run Evidence
  -> Keep / Discard / Crash Decision
```

The pipeline is intentionally not an Agent marketplace or generic Agent
production platform. It is an engineering system for delivering the harness that
lets a specific business Agent run safely and improve over time.

## Traceability Model

```text
 BR-XXX / UR-XXX / FR-XXX / NFR-XXX in docs/prd.md
  -> EPIC-XXX in docs/epics/
    -> STORY-XXX in docs/stories/
      -> Traceability marker in code
        -> Commit message containing FR-XXX and STORY-XXX
```

Functional requirements are the required implementation traceability anchor for
epics, stories, source markers, and commits. Business, user, and non-functional
requirements provide product context and quality constraints; they are enforced
through PRD structure checks, story acceptance criteria, architecture decisions,
and quality gates.

## Quality Gate Policy

CI must fail closed. If the gate cannot prove that code and documentation are
consistent, the change is rejected.

## Branching Model

The project uses one protected integration branch and named work item branches:

- `main`: protected integration branch.
- `<type>/<description>`: development branch for issue-driven work.

Implementation happens on a named work item branch. After local checks and CI
pass, that branch is merged into `main`.

Branch naming rules:

- Must start with one allowed issue category followed by `/`.
- Must include a non-empty description after the slash.
- Prefer lowercase kebab-case, such as `feat/branch-naming-rules`.
- Must not be a bare category name such as `feat` or `docs`.

Allowed categories:

- `feat`
- `fix`
- `docs`
- `test`
- `refactor`
- `ci`
- `chore`
- `perf`
- `security`

CI rejects pull requests that do not target `main`, do not originate from a
valid `<type>/<description>` branch, or push to unsupported branch names.

## Merged Branch Cleanup

GitHub Actions listens for merged pull requests. When a pull request is closed
with `merged == true`, has base branch `main`, and has a head branch matching an
allowed `<type>/<description>` pattern, the workflow deletes the remote head
branch.

The cleanup job must fail closed:

- It must not run for unmerged closed pull requests.
- It must not delete `main`.
- It must not delete branches outside the allowed `<type>/<description>`
  pattern.
- It must use repository-scoped `contents: write` permission only for the
  cleanup job.
