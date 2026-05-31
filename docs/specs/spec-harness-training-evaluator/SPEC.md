---
id: SPEC-harness-training-evaluator
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #60. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Harness Training Evaluator

## Why

`harness-trainer` needs a deterministic harness training evaluator so harness
designs, worker contracts, implementation artifacts, and replacement candidates
can be improved without relying on subjective review alone. The evaluator must
score declared harness capability coverage, contract completeness, failure
semantics, state boundaries, policy and approval safety, observability,
traceability, and replacement safety against repository artifacts that reviewers
and CI can inspect.

## Capabilities

- id: CAP-1
  intent: The evaluator can score current harness artifacts against the
    required runtime capability catalog.
  success: Evaluation input names the capability catalog, worker contract,
    governing SPEC, optional fixture set, and artifact list; output records
    `harness_score`, pass/fail status, missing coverage, score dimensions, and
    evaluation run ID.

- id: CAP-2
  intent: The evaluator can detect missing or incomplete capability and
    contract coverage.
  success: Coverage checks verify required runtime FRs, capability IDs,
    required catalog fields, required worker contract fields, catalog linkage,
    and traceability markers before reporting a passing score.

- id: CAP-3
  intent: Replacement safety is evaluated as a first-class result.
  success: Replacement comparison checks cover contract compatibility,
    state-boundary compatibility, failure-mode equivalence, event
    compatibility, trace compatibility, regression fixture result, rejection
    reason, and replacement-safety status.

- id: CAP-4
  intent: Evaluator fixtures make passing, failing, accepted, and rejected
    outcomes reproducible.
  success: Fixture evaluation distinguishes harness design fixtures from
    replacement-candidate fixtures and reports expected versus actual status
    for passing design, failing design, accepted replacement, and rejected
    replacement cases.

- id: CAP-5
  intent: CI can use evaluator output as an integration gate.
  success: Strict mode exits non-zero when required score, fixture, coverage,
    replacement-safety, or report-structure expectations fail, and CI can
    reject a harness contract package from that output.

- id: CAP-6
  intent: Evaluation results are explainable and traceable to source artifacts.
  success: Reports include score dimensions, missing coverage list,
    replacement-safety result, failed checks, artifact references, governing
    PRD/epic/story/catalog/contract links, and UI-safe diagnostics without
    requiring prior chat history.

## Constraints

- The evaluator must be deterministic and must not depend on model calls,
  subjective reviewer judgment, network access, external services, or
  environment-specific secrets.
- The evaluator must remain dependency-free unless a future story explicitly
  changes the runtime contract and CI gate.
- Evaluator criteria must trace to `FR-022`, `STORY-018`, `EPIC-002`,
  `HC-009`, the capability catalog, the worker contract model, and the
  governing replaceable-harness SPEC.
- Missing required catalog or contract evidence must fail evaluation instead
  of passing with warnings.
- Invalid replacement evidence must be reported as rejected, not accepted with
  warnings.
- Replacement implementations must preserve score dimensions, required
  evidence checks, rejection semantics, fixture expectations, report shape,
  and CI failure behavior.
- Evaluation output must distinguish generic replacement-safety evaluation
  from business-specific evaluation mapping.
- Reports, events, and traces must not include secret values, raw credentials,
  unsafe production data, or raw business data beyond approved metadata.

## Non-goals

- This SPEC does not implement a model trainer, language-model fine-tuning
  loop, subjective review workflow, telemetry backend, dashboard, or business
  evaluation mapper.
- This SPEC does not choose a third-party evaluation framework or hosted
  scoring service.
- This SPEC does not replace business evaluation mapping for a specific target
  Agent.
- This SPEC does not make evaluator output the only release, security,
  compliance, or business approval required.
- This SPEC does not allow missing replacement evidence to pass because the
  current implementation appears reasonable.

## Success signal

A reviewer can inspect the evaluator contract and determine how a harness
artifact package is scored, why missing coverage or replacement evidence fails,
which fixtures prove passing/failing/replacement behavior, and how CI can
accept or reject the package without relying on chat history, subjective review,
or external services.

## Assumptions

- The current dependency-free `harness_eval.py` is the first concrete evaluator
  implementation and may later be replaced if report shape and rejection
  semantics are preserved.
- JSON fixtures under `examples/harness-eval/` are sufficient for the first
  self-test suite.
- Machine-readable schemas can be added later without weakening the Markdown
  source-of-truth contracts.

## Open Questions

- Should evaluator reports be persisted as build artifacts on every CI run?
- Should score thresholds remain all-or-nothing at 100, or should future
  stories introduce non-blocking advisory thresholds?
