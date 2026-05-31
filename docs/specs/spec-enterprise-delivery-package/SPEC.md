---
id: SPEC-enterprise-delivery-package
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #38. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Enterprise Delivery Package

## Why

`harness-trainer` needs an Enterprise Delivery Package because enterprise
reviewers need one auditable handoff artifact for each target business Agent
Harness. The package must connect business intent, environment access,
architecture, worker contracts, implementation plan, evaluator plan, CI
evidence, run evidence, operational handoff, and harness-training decisions
without relying on chat history.

## Capabilities

- id: CAP-1
  intent: Enterprise reviewers can audit delivery from business goal to run
    evidence.
  success: The package cites PRD requirements, epic, story, spec, intake,
    inventory, blueprint, evaluation mapping, CI evidence, evaluator evidence,
    and run evidence for the same target business Agent Harness.

- id: CAP-2
  intent: Delivery leads can verify that required delivery artifacts exist
    before handoff.
  success: The package lists required artifacts and records status for PRD
    traceability, architecture, worker contracts, implementation plan,
    environment integration plan, evaluator plan, CI evidence, run evidence,
    and operational handoff evidence.

- id: CAP-3
  intent: Platform and business reviewers can inspect environment access and
    governance evidence.
  success: The package links environment inventory items to access boundaries,
    approval needs, policy rules, secret-handling expectations, audit evidence,
    and integration readiness.

- id: CAP-4
  intent: Harness trainers can preserve evidence across improvement
    iterations.
  success: The package records each harness-training iteration, changed
    artifact or implementation slice, validation command, evaluator result,
    keep/discard/crash decision, reviewer, and follow-up action.

- id: CAP-5
  intent: Downstream code-agent or programmer execution can be audited as part
    of the final delivery package.
  success: The package references bounded work packages by issue, story, spec,
    worker contract, allowed edit surface, validation command, and review
    evidence when implementation work exists.

- id: CAP-6
  intent: Delivery teams can determine whether the package is complete enough
    to hand off.
  success: Completion criteria identify missing required artifacts, unresolved
    risks, blocked environment access, missing evaluator evidence, failing CI,
    missing run evidence, or unapproved operational handoff.

## Constraints

- A delivery package must be scoped to one target business Agent Harness.
- The package must preserve traceability from business goal and PRD requirement
  to implementation evidence, evaluator evidence, and run evidence.
- The package must reference source artifacts rather than duplicating or
  redefining business goals, acceptance criteria, access boundaries, policy
  rules, approval decisions, budget limits, or evaluator expectations.
- The package must not expose secret values, production credentials, private
  data, or unsafe operational details.
- The package must separate confirmed evidence from assumptions, open risks,
  missing artifacts, unresolved decisions, and reviewer approvals.
- The package must be usable by reviewers without prior chat history.
- Code-agent execution package work is referenced as a package component but is
  not defined by this SPEC; that belongs to `FR-029` and `STORY-026`.

## Non-goals

- This SPEC does not implement the Agent Harness runtime.
- This SPEC does not create or grant environment access.
- This SPEC does not replace business owner, security, compliance, platform, or
  release approval.
- This SPEC does not implement the code-agent execution package.
- This SPEC does not replace upstream intake, inventory, blueprint, evaluation
  mapping, worker contract, or evaluator artifacts.
- This SPEC does not make delivery evidence immutable; it defines how evidence
  is updated after harness-training iterations.

## Success signal

An enterprise reviewer can open one delivery package and audit the target
business Agent Harness from business goal and PRD requirement through
architecture, worker contracts, implementation plan, environment integration
plan, evaluator plan, CI evidence, run evidence, operational handoff evidence,
and keep/discard/crash decisions.

## Assumptions

- Initial delivery packages can be Markdown-first before a machine-readable
  schema exists.
- Some implementation evidence may reference external systems, but repository
  artifacts must retain enough metadata to audit the evidence without chat
  history.
- `FR-029` may later define a reusable code-agent execution package that this
  delivery package references.

## Open Questions

- Which missing artifacts should block package handoff, and which should remain
  reviewer warnings?
- Should the first implementation create only a template, or should it also
  validate package instances in CI?
