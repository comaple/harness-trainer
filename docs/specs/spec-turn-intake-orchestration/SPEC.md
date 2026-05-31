---
id: SPEC-turn-intake-orchestration
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #46. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Turn Intake and Orchestration

## Why

`harness-trainer` needs turn intake and orchestration because every business
Agent Harness must accept, persist, execute, observe, and finish each user turn
through a durable state machine. Interrupted runs must remain debuggable and
resumable without losing request metadata, approval state, tool execution
status, UI-visible errors, lifecycle events, or trace evidence.

## Capabilities

- id: CAP-1
  intent: Operators can submit a turn request that is validated before runtime
    execution begins.
  success: Invalid requests fail closed before persistence; valid requests
    receive a stable turn ID, accepted timestamp, actor/session metadata,
    target business Agent Harness reference, input payload reference, and trace
    root.

- id: CAP-2
  intent: The runtime can persist and reload durable turn state.
  success: The turn state record stores turn ID, session ID, current state,
    step cursor, terminal status, retry/resume metadata, interruption reason,
    approval wait reference, tool/function call references, event offsets,
    trace IDs, and teardown status.

- id: CAP-3
  intent: The turn runtime can advance through explicit state transitions.
  success: The state machine defines entry conditions, output events, allowed
    next states, and failure behavior for intake, provisioning, model
    streaming, function execution, approval waiting, steering, teardown,
    completed, stopped, and failed states.

- id: CAP-4
  intent: UI and automation consumers can observe lifecycle progress.
  success: Each state transition emits a lifecycle event with turn ID, state,
    step cursor, timestamp, trace ID, and UI-safe status or error metadata.

- id: CAP-5
  intent: Interrupted or approval-waiting turns can be resumed without
    duplicating unsafe work.
  success: Resume uses persisted state, idempotency keys, approval references,
    event offsets, and trace context to continue only from a valid resumable
    state.

- id: CAP-6
  intent: Teardown is deterministic for successful and failed turns.
  success: Success teardown records final output metadata, usage summary,
    emitted completion event, trace closure, and terminal `completed` status;
    failure teardown records failure class, UI-safe diagnostic, preserved state,
    emitted failure event, trace closure, and terminal `failed` or `stopped`
    status.

## Constraints

- Turn orchestration must be technology-neutral and must not require adopting a
  specific external harness framework.
- The state machine must have explicit terminal states: `completed`, `failed`,
  and `stopped`.
- State transitions must be durable before side effects that depend on them.
- Tool/function execution must not occur before policy, credential, budget, and
  approval gates required by neighboring capabilities have passed.
- Approval waiting must preserve enough state to resume or reject the turn
  without replaying prior side effects.
- Failure behavior must distinguish invalid request, policy denial, approval
  rejection, budget failure, provider/tool failure, timeout, interruption, and
  teardown failure.
- Events and traces must not include secret values, credentials, private keys,
  unsafe production data, or raw business data beyond approved trace metadata.
- The contract must align with `HC-001` in the capability catalog and the
  worker contract model.

## Non-goals

- This SPEC does not implement the provider, credential, model capability,
  policy, approval, budget, session, memory, event bus, tracing, or evaluator
  capabilities.
- This SPEC does not choose a concrete database, queue, event bus, tracing
  backend, model provider, or tool runtime.
- This SPEC does not define business-domain behavior for a specific Agent.
- This SPEC does not grant approval for unsafe tool calls or side effects.
- This SPEC does not replace worker contracts; it defines the orchestration
  contract those workers must integrate with.

## Success signal

A reviewer can inspect the turn intake and orchestration contract and determine
how a turn is accepted, persisted, advanced, observed, resumed, completed,
stopped, or failed. The reviewer can see explicit terminal states, entry
conditions, lifecycle events, failure behavior, and success/failure teardown
without relying on chat history or a specific runtime framework.

## Assumptions

- The first downstream implementation can be Markdown-first and later become a
  machine-readable state-machine schema.
- Durable state can initially be specified before a concrete persistence layer
  exists.
- Neighboring capabilities own their own contracts, but turn orchestration owns
  the state cursor and lifecycle coordination between them.

## Open Questions

- Should the first implementation create a state-machine template only, or also
  add CI checks for individual state-machine instances?
- Which failure classes should be terminal immediately, and which should remain
  resumable after operator intervention?
