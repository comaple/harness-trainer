# harness-trainer

Harness trainer is a project for iteratively improving agent harnesses.

The target is not a model checkpoint. The target is the agent operating system:
turn orchestration, tool policy, approval flow, budgets, resumable sessions,
context compaction, skills, event streams, tracing, and local evaluation.

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

Create an autoresearch-style loop for harness engineering:

1. Define a deterministic local benchmark for harness quality.
2. Let an agent propose one harness improvement.
3. Apply the smallest useful change.
4. Run the benchmark.
5. Keep the change if the score improves or if behavior is preserved with a
   concrete simplification.
6. Log the result and continue.

## Non-Goals

- Do not train language models in this repository.
- Do not modify or submit changes from the sibling `autoresearch` checkout.
- Do not build a large framework before the local harness benchmark exists.

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
- CI commit messages must include at least one valid FR ID and Story ID.

## Branch Workflow

Use one protected integration branch and named feature branches:

- `main`: protected integration branch.
- `feat/<feature-description>`: development branch for sub-feature work.

Develop and test on a named branch such as `feat/branch-naming-rules`. After
the quality gate passes, merge that branch into `main`. CI enforces pull
requests from `feat/<feature-description>` to `main`.

Branch names must include the function being changed. The bare branch name
`feat` is not valid for implementation work.
