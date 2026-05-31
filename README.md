# harness-trainer

`harness-trainer` is an engineering delivery system for enterprise business
Agents.

It is not the business Agent itself. It is the construction crew for building
one: it takes a business goal, business PRD, and business environment, then
drives the work needed to produce a governed, observable, evaluable Agent
Harness for that business Agent.

The core deliverable is an Agent Harness and its training loop: turn
orchestration, tool policy, approval flow, budgets, resumable sessions, context
compaction, skills, event streams, tracing, local evaluation, and the
keep/discard loop for improving the harness.

## Product Boundary

`harness-trainer` exists to turn enterprise business intent into an engineered
Agent Harness.

### Inputs

- Business goals and success criteria
- Business PRD, workflows, roles, risks, and acceptance criteria
- Business environment inventory:
  - tools and APIs
  - databases and data sources
  - knowledge bases and documents
  - permission systems and secrets
  - approval processes
  - logging, monitoring, and audit systems
- Agent operating constraints:
  - model provider
  - budget
  - policy
  - session and memory rules
  - evaluator requirements

### Outputs

- Business Agent Harness blueprint
- Worker contracts for tools, skills, policy, approval, budget, session,
  events, and tracing
- Environment integration plan
- Agent runtime plan or implementation
- Evaluation plan and deterministic harness evaluator
- CI/CD and governance gates
- Run logs, events, traces, scores, and keep/discard records

### Non-Goals

- It does not deliver a generic Agent marketplace.
- It does not directly train language models.
- It does not replace business PRD ownership.
- It does not become a general workflow automation product.
- It does not treat prompt management as the whole product.

## References

This project is built from two main references:

- Autoresearch methodology: run fixed experiments, score the result, keep or
  discard changes, and iterate.
- Harness engineering reference:
  [How to Build Your Own Agent Harness](https://iii.dev/blog/how-to-build-your-own-agent-harness/)

The harness article frames an agent harness as a set of replaceable jobs rather
than a single monolithic framework. This repository uses that idea as the design
target: each harness responsibility should have a clear contract, state
boundary, policy boundary, failure behavior, and observable output.

## Goal

Create an autoresearch-style loop for enterprise Agent Harness delivery:

1. Ingest business goal, business PRD, and business environment.
2. Generate the Agent Harness blueprint and worker contracts.
3. Build or update the harness implementation.
4. Run deterministic business and harness evaluators.
5. Keep the change if scores improve or if behavior is preserved with a
   concrete simplification.
6. Log the result and continue.

## Non-Goals

- Do not train language models in this repository.
- Do not modify or submit changes from the sibling `autoresearch` checkout.
- Do not build a generic Agent production platform or marketplace.
- Do not build a large runtime before the business intake, harness contracts,
  and evaluator spine are stable.

## Starting Point

Read [AGENTS.md](AGENTS.md) first. It defines the working rules, editable
surface, harness responsibilities, experiment loop, result logging, and commit
rules for agents working in this repository.

## Quality Gate

Run the local gate before committing:

```bash
python3 scripts/ci_check.py
```

The same gate runs in GitHub Actions on pull requests and pushes to `main`.
Once the first commit is pushed, configure branch protection so the `Quality
Gate` workflow must pass before merging.

The gate enforces agile traceability:

- PRDs must include business requirements, user requirements, functional
  requirements, non-functional requirements, constraints, assumptions and
  dependencies, out-of-scope items, and success metrics.
- Requirements must first appear as `FR-XXX` entries in [docs/prd.md](docs/prd.md).
- Epics in `docs/epics/` must reference valid FR IDs and list stories.
- Stories in `docs/stories/` must reference valid FR and Epic IDs and include
  an implementation plan.
- Source files must include a `Traceability: FR-XXX, STORY-XXX` marker.
- CI commit messages must include at least one issue reference, valid FR ID, and
  Story ID. Accepted issue formats are `ISSUE-123` and `#123`.
- Local secret files such as `.env` and `.env.*` must be ignored and untracked.

## Branch Workflow

Use one protected integration branch and named work item branches:

- `main`: protected integration branch.
- `<type>/<description>`: development branch for issue-driven work.

Develop and test on a named branch such as `feat/branch-naming-rules`,
`docs/prd-rules`, or `ci/delete-merged-branches`. After the quality gate passes,
merge that branch into `main`. CI enforces pull requests from allowed work item
branches to `main`.

Allowed issue categories are:

- `feat`
- `fix`
- `docs`
- `test`
- `refactor`
- `ci`
- `chore`
- `perf`
- `security`

Branch names must include the category and work being changed. Bare category
names such as `feat` or `docs` are not valid for implementation work.

After a PR from an allowed work item branch to `main` is merged, GitHub Actions
automatically deletes the merged remote branch.
