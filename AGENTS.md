# AGENTS.md

This repository trains agent harnesses.

The goal is not to train a language model. The goal is to improve the operating
system around an agent: its turn loop, tool policy, approval handling, budget
control, session durability, context management, observability, and evaluation
loop.

`autoresearch` is a reference methodology only. Do not commit changes to the
local `autoresearch` checkout from this project.

## Project Objective

Build a small, iterative harness-training system inspired by autoresearch:

1. Define a fixed local benchmark for harness quality.
2. Let an agent propose one harness improvement at a time.
3. Apply the smallest useful change.
4. Run the harness benchmark.
5. Keep the change if the score improves or the same score is achieved with a
   meaningful simplification.
6. Log the result.

The object under optimization is the harness, not the benchmark task executed by
the harness.

## Working Directory

All implementation work for this project must happen inside this repository:

```text
/Users/data/proj/autoharness/harness-trainer
```

Do not edit, stage, commit, or push files from:

```text
/Users/data/proj/autoharness/autoresearch
```

That repository is a fork/reference checkout and must remain separate.

## Harness Responsibilities

A high-quality harness should make these jobs explicit and replaceable:

1. Accept and persist turn requests.
2. Resolve provider credentials.
3. Track model capabilities.
4. Drive a durable turn state machine.
5. Load skills and tool instructions on demand.
6. Assemble prompts from mode, identity, workspace, and skills.
7. Stream assistant output to the client.
8. Check every tool call against policy.
9. Pause and resume calls that require human approval.
10. Track spend, tokens, and budget limits.
11. Run before-call and after-call hooks.
12. Persist sessions as resumable and branchable state.
13. Compact context when the window fills.
14. Emit events for UI, automation, and replay.
15. Carry trace context across the full turn.

Each responsibility should have a clear contract:

- Inputs
- Outputs
- Error behavior
- Timeout behavior
- Persisted state
- Events emitted
- Policy boundary

## Editable Surface

Prefer editing project-owned files such as:

- `AGENTS.md`
- `README.md`
- `harness_eval.py`
- `harness_program.md`
- files under `harness/`
- files under `examples/`
- files under `tests/`

Do not introduce dependencies unless the task clearly requires them. Prefer the
Python standard library for early benchmark and harness logic.

## Experiment Loop

For harness-training changes, use this loop:

1. Inspect the current repository state.
2. Add or update product context in `docs/prd.md` before implementation. Use
   `BR-XXX` for business requirements, `UR-XXX` for user requirements, `FR-XXX`
   for functional requirements, and `NFR-XXX` for non-functional requirements.
3. Decompose the relevant functional requirement in a matching epic under
   `docs/epics/`.
4. Create or update a story under `docs/stories/` with a concrete
   implementation plan.
5. Run the local harness benchmark if one exists.
6. Choose exactly one hypothesis.
7. Edit the smallest relevant files.
8. Run the benchmark and `python3 scripts/ci_check.py`.
9. Record the result.
10. Keep, revise, or discard based on evidence.

The first version of this repository may not have a benchmark yet. In that case,
the next engineering priority is to create one before adding complex harness
features.

## Result Logging

Use `harness_results.tsv` for experiment results. It should remain untracked.

Expected columns:

```text
commit	harness_score	status	description
```

Rules:

- `commit`: short git commit hash, or `uncommitted` for failed attempts.
- `harness_score`: numeric score from the benchmark.
- `status`: `keep`, `discard`, or `crash`.
- `description`: short text without tabs.

## Keep Criteria

Keep a change when it does one or more of these:

- Improves the benchmark score.
- Adds a missing harness responsibility with a clear contract.
- Makes policy, approval, budget, session, or event behavior testable.
- Improves recovery from failed, interrupted, or resumed turns.
- Simplifies the harness while preserving behavior and safety.

Discard or revise a change when it:

- Adds wording without changing behavior.
- Weakens policy or approval semantics.
- Makes the agent more likely to operate outside this repository.
- Makes the benchmark less objective.
- Couples unrelated harness responsibilities.

## Initial Build Order

Start with a minimal but useful spine:

1. `README.md`: human-facing project overview.
2. `harness_eval.py`: deterministic local evaluator.
3. `harness_program.md`: executable agent procedure for harness experiments.
4. `harness_results.tsv`: ignored experiment log.
5. Optional `harness/` package once there is real code to evaluate.

Avoid building a large framework before the benchmark exists.

## Commit Rules

Before committing:

1. Confirm `git status` only shows intended files inside this repository.
2. Run `python3 scripts/ci_check.py`.
3. Make sure source files include a valid `Traceability: FR-XXX, STORY-XXX`
   marker.
4. Use a commit message that includes at least one issue reference
   (`ISSUE-123` or `#123`), one valid `FR-XXX`, and one valid `STORY-XXX` ID.
5. Do not stage files from sibling repositories.
6. Keep commits focused on one harness-training improvement.

CI must run the same gate on pull requests and pushes to `main`. Treat a failing
gate as a blocker, not advisory output.

## Branch Workflow

Use `main` as the protected integration branch and `<type>/<description>` as
the development branch pattern. All issue-driven work happens on a named work
branch, for example `feat/branch-naming-rules`, `docs/prd-rules`, or
`ci/delete-merged-branches`; after tests and gates pass, merge that branch into
`main`.

Allowed issue categories are `feat`, `fix`, `docs`, `test`, `refactor`, `ci`,
`chore`, `perf`, and `security`.

Bare category names such as `feat` or `docs` are not valid for implementation
work. Merged remote work branches are deleted automatically by GitHub Actions
after successful merge.
