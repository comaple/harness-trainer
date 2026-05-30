# Architecture

## Overview

`harness-trainer` uses documentation-first traceability as the first system
boundary. Requirements are declared in the PRD, decomposed in epics, planned in
stories, and enforced by a local CI gate.

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

## Traceability Model

```text
FR-XXX in docs/prd.md
  -> EPIC-XXX in docs/epics/
    -> STORY-XXX in docs/stories/
      -> Traceability marker in code
        -> Commit message containing FR-XXX and STORY-XXX
```

## Quality Gate Policy

CI must fail closed. If the gate cannot prove that code and documentation are
consistent, the change is rejected.

## Branching Model

The project uses one protected integration branch and named feature branches:

- `main`: protected integration branch.
- `feat/<feature-description>`: development branch for sub-feature work.

Feature implementation happens on a named `feat/<feature-description>` branch.
After local checks and CI pass, that branch is merged into `main`.

Branch naming rules:

- Must start with `feat/`.
- Must include a non-empty feature description after the slash.
- Prefer lowercase kebab-case, such as `feat/branch-naming-rules`.
- Must not be the bare branch name `feat`.

CI rejects pull requests that do not target `main`, do not originate from a
valid `feat/<feature-description>` branch, or push to unsupported branch names.
