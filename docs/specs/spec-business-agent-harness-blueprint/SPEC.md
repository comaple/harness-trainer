---
id: SPEC-business-agent-harness-blueprint
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #30. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Business Agent Harness Blueprint

## Why

`harness-trainer` needs a Business Agent Harness Blueprint because enterprise
delivery must convert approved business context and confirmed environment
inventory into an implementable harness design before programmers or code
agents receive bounded work. The blueprint is the handoff artifact that links
business goals, user tasks, environment dependencies, harness capabilities,
worker contracts, policy, approval, budget, session, events, tracing, and
evaluation into one auditable delivery plan.

## Capabilities

- id: CAP-1
  intent: Harness architects can define the target business Agent's purpose and
    user task boundary from approved business context.
  success: The blueprint records Agent purpose, in-scope user tasks, out-of-
    scope tasks, source business goals, and acceptance criteria references.

- id: CAP-2
  intent: Delivery teams can map business requirements to harness capability
    areas.
  success: Each accepted business goal, workflow, or requirement maps to one or
    more harness areas: tools, knowledge, policy, approval, budget, session,
    events, tracing, or evaluation.

- id: CAP-3
  intent: Platform engineers can map environment inventory items to worker
    contracts and integration responsibilities.
  success: Each selected environment item links to a worker contract candidate,
    access boundary, test strategy, policy rule, and integration readiness
    status.

- id: CAP-4
  intent: Reviewers can identify policy, approval, budget, session, and
    observability needs before implementation stories are created.
  success: The blueprint identifies required policy decisions, approval gates,
    budget constraints, session or memory rules, event records, trace evidence,
    and audit expectations.

- id: CAP-5
  intent: Evaluator designers can derive deterministic evaluation expectations
    from the blueprint.
  success: The blueprint maps business success metrics and acceptance criteria
    to evaluator expectations, fixtures, run evidence, and keep/discard review
    criteria.

- id: CAP-6
  intent: Delivery leads can create bounded implementation stories from the
    blueprint without relying on chat history.
  success: The blueprint lists implementation slices with issue/story/spec
    candidates, allowed edit surfaces, required contracts, validation commands,
    missing dependencies, and open risks.

## Constraints

- Blueprint work must consume business context intake and business environment
  inventory for the same target business Agent.
- Blueprint must separate confirmed source facts from assumptions, open
  questions, missing dependencies, and reviewer decisions.
- Blueprint must not redefine business goals, acceptance criteria, or
  environment access boundaries without traceable owner confirmation.
- Blueprint must not expose secret values or grant production access.
- Blueprint must stay implementation-neutral until a downstream story,
  contract, or architecture decision intentionally selects a runtime, provider,
  SDK, or database client.
- Blueprint must preserve traceability from business requirement to harness
  capability, worker contract, evaluator expectation, and implementation story.
- Blueprint artifacts must be usable by downstream specs, stories, contracts,
  evaluators, delivery packages, and code-agent work packages without relying
  on chat history.

## Non-goals

- This SPEC does not implement the Agent Harness runtime.
- This SPEC does not create final worker contracts; it identifies contract
  candidates and required contract surfaces.
- This SPEC does not replace business owner approval of goals, risks, or
  acceptance criteria.
- This SPEC does not grant access to environment systems, secrets, data, or
  production resources.
- This SPEC does not create the enterprise delivery package; that belongs to
  `FR-027` and `STORY-023`.
- This SPEC does not make code agents product owners, architects, approvers, or
  reviewers.

## Success signal

A harness delivery lead can take a completed blueprint and create bounded,
traceable implementation stories that identify the Agent purpose, harness
capabilities, environment integrations, worker contract candidates, policy and
approval needs, evaluator expectations, risks, missing dependencies, validation
commands, and evidence required to decide keep, discard, retry, or handoff.

## Assumptions

- The business context intake and environment inventory can be cited as
  repository artifacts, linked external artifacts, or structured summaries.
- Initial blueprint creation can be document-based before a UI, API, or
  machine-readable schema exists.
- Worker contracts may start as candidates in the blueprint and become full
  contract documents in downstream implementation work.

## Open Questions

- Which blueprint gaps should block implementation story creation, and which
  should remain reviewer warnings?
- Should the first blueprint implementation be Markdown-only, or should it also
  define a machine-readable schema for later automation?
