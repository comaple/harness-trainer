# Source Extract: Turn Intake and Orchestration

## User Request

- Continue completing the project by standard BMad flow.
- Work issue by issue, self-validate, submit, and continue until all epics are
  complete.
- For EPIC-002, begin with `STORY-011 / FR-015` because the capability catalog
  names turn intake and orchestration but no dedicated SPEC existed yet.

## Issue #46

Source: GitHub issue `#46`

- Title: `FR-015: Create turn intake and orchestration spec`
- Scope: create the BMad SPEC for `STORY-011 / FR-015`.
- Required content: turn request intake, persistence, durable turn state, state
  transitions, assistant streaming coordination, function/tool execution
  coordination, approval waiting, steering, teardown, stopped, completed, and
  failed behavior.
- Required preservation: lifecycle events, terminal states, failure behavior,
  UI visibility, and trace evidence.
- Constraint: keep the spec technology-neutral and aligned with the capability
  catalog and worker contract model.
- Acceptance: state machine has explicit terminal states.
- Acceptance: each state declares entry conditions, output events, and failure
  behavior.
- Acceptance: teardown behavior is specified for both success and failure.

## PRD

Source: `docs/prd.md`

- `FR-015`: The harness runtime plan must include turn request intake,
  persistence, durable turn state, turn stepping, assistant streaming, tool
  execution, steering, and teardown.
- `FR-020`: The harness runtime plan must include branching session storage,
  resumable state, per-session queues, context window monitoring, and context
  compaction.
- `FR-021`: The harness runtime plan must include assistant token streaming, UI
  event streams, run/session/message/function identifiers, and one trace that
  spans the whole turn.

## EPIC-002

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

- Goal: decompose the target agent harness into replaceable, testable
  capabilities based on the harness reference article.
- `FR-015` is part of EPIC-002.
- `STORY-011` plans turn intake and orchestration.
- Acceptance requires each capability to identify public contract, state
  boundary, failure behavior, and observability evidence.
- Replacement-sensitive capabilities must identify evaluator evidence and
  replacement safety criteria before implementation begins.
- Decomposition must not require adopting a specific external harness
  framework.

## STORY-011

Source: `docs/stories/STORY-011-turn-intake-orchestration.md`

- User story: as an agent operator, I want each user turn to be accepted,
  persisted, executed, and completed through a durable state machine so that
  interrupted runs can be debugged or resumed.
- Implementation plan: specify the turn request schema.
- Implementation plan: specify the turn state record and terminal states.
- Implementation plan: define state transitions for provisioning, assistant
  streaming, function execution, approval waiting, steering, teardown, stopped,
  and failed.
- Implementation plan: define emitted lifecycle events for each state.
- Implementation plan: define how state transition errors become visible to the
  UI and trace.
- Acceptance: state machine has explicit terminal states.
- Acceptance: each state declares entry conditions, output events, and failure
  behavior.
- Acceptance: teardown behavior is specified for both success and failure.

## Capability Catalog

Source: `docs/harness/capability-catalog.md`

- `HC-001`: Turn Intake and Orchestration.
- Owning FR ID: `FR-015`.
- Owning Story ID: `STORY-011`.
- Intent: accept a business-agent turn, persist the request, advance the turn
  through deterministic steps, and coordinate model calls, tool calls,
  steering, and teardown.
- Public contract surface: `submit_turn`, `load_turn`, `step_turn`,
  `complete_turn`, and `fail_turn` operations with stable turn identifiers and
  typed turn state transitions.
- State ownership: durable turn state, step cursor, terminal status,
  interruption reason, and resume metadata.
- Emitted events: `turn.accepted`, `turn.step_started`,
  `turn.step_completed`, `turn.completed`, and `turn.failed`.
- Failure behavior: invalid turn requests fail closed before persistence;
  resumable runtime failures preserve the last successful step and expose a
  retryable status.
- Replacement boundary: replacement must preserve turn IDs, state transition
  semantics, terminal statuses, resume behavior, and emitted event names.
- Evaluator evidence: fixture turns covering accepted, failed, interrupted,
  resumed, and completed flows.
- Trace evidence: one trace span per turn and child spans for each step.

## Worker Contract Model

Source: `docs/harness/worker-contract.md`

- Worker contracts define callable or event-triggered units at capability
  boundaries.
- Required fields include function ID, capability ID, trigger name, input
  shape, output shape, recoverable errors, fail-closed errors, timeout,
  idempotency, state reads, state writes, emitted events, trace tags, version
  expectations, and fixture expectations.
- Replacement implementations must preserve accepted input shape, compatible
  output shape, equivalent failure behavior, equivalent state boundary,
  equivalent event and trace evidence, timeout and idempotency semantics, and
  fixture results.

## Harness Evaluator

Source: `harness_eval.py`

- The deterministic evaluator scores capability coverage, contract
  completeness, replacement safety, failure semantics, state boundaries, policy
  and approval safety, observability, and traceability.
- Required runtime FRs include `FR-013` through `FR-022`.
- Current evaluator expects catalog entries to name public contract surface,
  state ownership, emitted events, failure behavior, replacement boundary,
  evaluator evidence, and trace evidence.

## Preservation Notes

- All load-bearing claims above are represented in `SPEC.md` capabilities,
  constraints, non-goals, success signal, assumptions, or open questions.
- Wrapper-only API metadata, timestamps, and repetitive repository metadata were
  not carried forward because they do not change downstream implementation
  decisions.
