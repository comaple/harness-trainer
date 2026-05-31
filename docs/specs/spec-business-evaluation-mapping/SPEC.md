---
id: SPEC-business-evaluation-mapping
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #34. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Business Evaluation Mapping

## Why

`harness-trainer` needs business evaluation mapping because harness training
must optimize outcomes that matter to the target business Agent, not just
generic implementation correctness. Delivery teams need a traceable way to turn
business success criteria and acceptance criteria into deterministic evaluator
checks, regression fixtures, run evidence, failure classification, and
keep/discard/crash decisions.

## Capabilities

- id: CAP-1
  intent: Evaluator designers can map business success criteria and acceptance
    criteria to evaluator expectations.
  success: Each business metric or acceptance criterion links to a harness
    behavior under test, expected pass signal, and source requirement reference.

- id: CAP-2
  intent: Delivery teams can define deterministic checks for business-relevant
    harness behavior.
  success: Each mapped criterion identifies whether it is covered by a
    deterministic check, a reviewer-inspected evidence field, or an explicit
    open gap.

- id: CAP-3
  intent: Harness trainers can run regression fixtures for key workflows and
    environment-dependent behavior.
  success: Each evaluator expectation identifies a fixture, scenario, sandbox,
    mock, or documented no-fixture reason that can be used without unsafe
    production access.

- id: CAP-4
  intent: Reviewers can classify failures consistently across harness training
    runs.
  success: Evaluation output can classify incorrect tool use, missing approval,
    policy violation, unsupported data access, budget overrun, poor task
    outcome, and crash or infrastructure failure.

- id: CAP-5
  intent: Delivery leads can decide whether a harness change should be kept,
    discarded, or treated as a crash.
  success: Evaluation output records run evidence, criterion coverage, failure
    class, score or pass signal, and the evidence required for keep, discard,
    or crash decisions.

- id: CAP-6
  intent: Downstream stories and code-agent work packages can consume evaluator
    mapping without relying on chat history.
  success: The mapping cites intake, blueprint, requirement, story, contract,
    fixture, validation command, and review evidence references in repository
    artifacts or linked source documents.

## Constraints

- Evaluation mapping must consume the business context intake, business
  environment inventory, and Business Agent Harness Blueprint for the same
  target business Agent when those artifacts exist.
- Evaluation mapping must not invent, redefine, or weaken business success
  criteria, acceptance criteria, access boundaries, policy rules, approval
  expectations, or budget limits without traceable owner confirmation.
- Deterministic checks must be traceable to source criteria and runnable or
  reviewable without relying on prior chat history.
- Environment-dependent checks must use fixtures, mocks, sandboxes, linked test
  systems, or documented manual evidence; they must not require committing
  production secrets or unsafe production access.
- Keep, discard, and crash decisions must be based on recorded evidence, not
  developer intent.
- Evaluation mapping must preserve the existing separation between business
  evaluation and generic replacement-safety evaluation.

## Non-goals

- This SPEC does not implement the evaluator runtime or scoring engine.
- This SPEC does not replace `FR-022` replacement-safety evaluation for generic
  harness capability compatibility.
- This SPEC does not create the final enterprise delivery package; that belongs
  to `FR-027` and `STORY-023`.
- This SPEC does not grant access to business systems, secrets, databases,
  APIs, or production data.
- This SPEC does not make evaluator output the only approval needed for
  business, security, compliance, or release decisions.
- This SPEC does not let programmers or code agents redefine business success.

## Success signal

A harness delivery lead can take a completed evaluation mapping artifact and
see every business success criterion and acceptance criterion mapped to
evaluator expectation, deterministic check or explicit review evidence,
regression fixture or scenario, failure class, run evidence, validation command,
and keep/discard/crash decision support.

## Assumptions

- The first implementation can be Markdown-first and later gain a
  machine-readable schema.
- Some business criteria may require reviewer-inspected evidence before they
  can become fully deterministic checks.
- Business evaluation mapping can reference upstream intake, inventory, and
  blueprint artifacts instead of duplicating their full contents.

## Open Questions

- Which mapped criteria should block implementation review when they lack a
  deterministic check?
- Should business evaluation mapping become its own template under
  `docs/evaluation/`, or should it extend the existing blueprint evaluation
  expectations table first?
