---
id: SPEC-budget-hooks-side-effects
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #54. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Budget Hooks and Side Effects

## Why

`harness-trainer` needs budget, hook, and side-effect contracts so spend limits,
usage accounting, redaction, logging, alerts, and custom side effects can be
added or replaced without changing turn orchestration. Budget and hook behavior
must decide whether execution is blocked, warned, degraded, or allowed before
unsafe cost, logging, or side effects occur.

## Capabilities

- id: CAP-1
  intent: The runtime can check budget before spend occurs.
  success: Budget checks accept turn ID, session ID, actor or workspace scope,
    provider/model context, requested usage estimate, budget rule ID, and
    accounting unit; the result is `allow`, `warn`, or `block` with a redacted
    reason and remaining-budget metadata.

- id: CAP-2
  intent: The runtime can record usage after provider or tool calls.
  success: Usage recording persists turn ID, tool or provider call reference,
    accounting unit, measured usage, cost or spend metadata, budget scope,
    provenance, and idempotency key after the call result is known.

- id: CAP-3
  intent: Budget alerts, forecasts, and rollovers are explicit budget outcomes.
  success: The contract declares alert thresholds, forecast inputs, rollover
    boundary, rollover state writes, and emitted `budget.checked` or
    `budget.exceeded` evidence without requiring a specific billing backend.

- id: CAP-4
  intent: Before-call and after-call hooks can run in a controlled order.
  success: Hook execution declares hook IDs, phase, fanout rule, timeout,
    ordering, criticality, input redaction level, output status, and whether a
    failure blocks execution, degrades execution, or is recorded without
    blocking.

- id: CAP-5
  intent: Redaction and logging hooks preserve privacy and auditability.
  success: Redaction hooks run before logging hooks, emit redaction reports,
    and prevent raw secrets, raw credentials, private keys, or unsafe production
    data from reaching logs, events, traces, hook outputs, or custom side
    effects.

- id: CAP-6
  intent: Custom side effects execute only when eligible and idempotent.
  success: Side-effect execution declares eligibility decision, side-effect
    class, policy or hook decision reference, idempotency key, ordering rule,
    failure outcome, emitted event, and trace tag before the side effect runs.

## Constraints

- The capability must be technology-neutral and must not require a specific
  billing provider, budget store, hook runner, logging backend, event bus,
  queue, database, tracing backend, or side-effect runtime.
- Budget checks must run before spend or side effects that require budget
  approval; `block` outcomes fail closed before the dependent call.
- Usage recording must occur after provider or tool calls when measured usage
  is available, and duplicate recording must be prevented by idempotency.
- Budget exhaustion and hook policy violations must fail closed.
- Non-critical hook failures may allow degraded execution only when the hook
  contract marks the hook non-critical and records the degraded outcome.
- Redaction hooks must precede logging hooks and any hook or side effect that
  could expose sensitive data.
- Hook fanout must define whether hooks run sequentially, in parallel, or by
  phase, and must define timeout behavior for each phase.
- Custom side effects must not execute unless budget, policy, credential, and
  required hook gates have passed.
- Events and traces must not include secret values, private keys, raw
  credentials, raw business data, or unsafe production data beyond approved
  metadata.
- Replacement implementations must preserve budget accounting units, hook
  ordering, redaction-before-log behavior, side-effect eligibility, emitted
  events, trace tags, state writes, and failure categories.
- The contract must align with `HC-006`, `FR-019`, `STORY-015`, the worker
  contract model, and the turn orchestration budget gate.

## Non-goals

- This SPEC does not implement a billing system, budget store, hook runner,
  logging backend, alerting system, side-effect runtime, event bus, queue,
  database, or tracing backend.
- This SPEC does not define concrete budget amounts, alert thresholds, rollover
  calendars, or billing rates for a specific business Agent.
- This SPEC does not authorize custom side effects that bypass policy,
  credential, approval, budget, or redaction gates.
- This SPEC does not replace provider usage measurement, policy approval,
  session memory, event streaming, or evaluator capabilities.
- This SPEC does not make logs a source of raw production data or secrets.

## Success signal

A reviewer can inspect the budget, hook, and side-effect contract and determine
how a turn checks budget before spend, records usage after calls, emits budget
alerts, runs before/after/redaction/logging hooks, orders hook fanout, handles
timeouts and failures, blocks or degrades execution, and permits custom side
effects without relying on a concrete billing, hook, or logging implementation.

## Assumptions

- Provider/model capability lookup supplies usage-accounting units that this
  budget layer can consume.
- Budget alerting and forecasting can initially be contract-shaped before an
  external billing or alerting integration exists.
- Custom side effects are treated as gated outcomes of this capability but may
  be implemented by later business-agent-specific workers.

## Open Questions

- Should budget rollover policy be global, workspace scoped, or business Agent
  scoped by default?
- Which hook phases should be allowed to run in parallel, and which must remain
  sequential because of redaction or side-effect ordering?
