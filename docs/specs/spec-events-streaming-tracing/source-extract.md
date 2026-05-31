# Source Extract: Events Streaming and Tracing

## Issue

Source: GitHub issue #58

- Create the BMad SPEC for `STORY-017 / FR-021` events, streaming, and tracing.
- Scope includes assistant token streaming, UI event streams, automation
  events, full-turn trace context, lifecycle events, message updates, tool
  calls, approvals, budget decisions, compaction, completion, failures, event
  payloads, run/session/message/function identifiers, stream offsets, trace
  identifiers, span attributes, event-to-trace linkage, replay expectations,
  missing-trace handling, observability-degraded behavior, and replacement
  criteria.
- Acceptance requires every runtime capability to emit or forward trace
  context, UI-visible events to correlate to trace spans, failed turns to emit
  enough diagnostic information, and mapping to `HC-008`, `FR-021`,
  `STORY-017`, and `EPIC-002`.

## PRD

Source: `docs/prd.md`

### FR-021: Events, Streaming, and Tracing

The harness runtime plan must include assistant token streaming, UI event
streams, run/session/message/function identifiers, and one trace that spans the
whole turn.

Additional PRD evidence:

- Harness capabilities must emit enough structured events and trace
  identifiers for review and evaluation.
- The product must preserve traceability from business intent through planning,
  implementation, review, and gated integration.

## Epic

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

- `EPIC-002` decomposes the target agent harness into replaceable, testable
  capabilities.
- `STORY-017` plans events, streaming, and tracing.
- Acceptance requires each capability to identify its public contract, state
  boundary, failure behavior, and observability evidence.
- Replacement-sensitive capabilities must identify evaluator evidence and
  replacement safety criteria before implementation begins.
- The decomposition must not require adopting any specific external harness
  framework.

## Story

Source: `docs/stories/STORY-017-events-streaming-tracing.md`

- As a reviewer, token streams, UI events, and traces must share run, session,
  message, and function identifiers so a full turn can be debugged across
  capabilities.
- Functional requirements: `FR-021` and `FR-015`.
- Implementation plan:
  - Specify event names for turn lifecycle, message updates, tool calls,
    approvals, budget decisions, compaction, and completion.
  - Specify event payload requirements.
  - Specify trace identifiers and required span attributes.
  - Specify streaming behavior for assistant output.
  - Define event replay expectations for debugging.
- Acceptance:
  - Every runtime capability emits or forwards trace context.
  - UI-visible events can be correlated to trace spans.
  - Failed turns emit enough information to diagnose the failing capability.

## Capability Catalog

Source: `docs/harness/capability-catalog.md`

### HC-008: Events, Streaming, and Tracing

- Intent: Emit assistant token streams, UI events, automation events, and trace
  context that spans the full turn.
- Public contract surface: `emit_event`, `stream_assistant_token`,
  `start_trace`, `attach_trace_context`, and `finish_trace` operations.
- State ownership: Owns event IDs, stream offsets, trace IDs, span IDs, and
  event-to-trace linkage.
- Emitted events: `trace.started`, `trace.finished`,
  `assistant.token_streamed`, `ui.event_emitted`, and
  `automation.event_emitted`.
- Failure behavior: Event emission failures must not silently drop audit
  events; unrecoverable trace failures mark the turn as
  observability-degraded.
- Replacement boundary: A replacement must preserve event names, ordering,
  stream offsets, trace propagation fields, and replay compatibility.
- Evaluator evidence: Fixtures for ordered token streaming, replayable events,
  missing trace rejection, and degraded observability reporting.
- Trace evidence: Root trace for each turn and linked spans for model calls,
  tool calls, approvals, hooks, and emitted events.

## Worker Contract

Source: `docs/harness/worker-contract.md`

- Worker contracts cover callable or event-triggered units at a capability
  boundary.
- Event-triggered handlers receive named events and produce state changes,
  emitted events, or a terminal result.
- Worker contracts require emitted events and trace tags.
- The trigger is the operation or event that invokes the worker.
- Emitted events include success, failure, degraded, and audit events, and
  should match capability catalog event names where applicable.
- Trace tags are required for observability and replacement comparison.
- Idempotency prevents duplicated state writes, events, or side effects.
- Replacement comparison requires equivalent event and trace evidence:
  required events and trace tags remain stable for equivalent paths, and
  additional diagnostic events cannot affect ordering-sensitive consumers.

## Neighboring Specs

Source: `docs/specs/spec-turn-intake-orchestration/SPEC.md`

- Turn intake creates a trace root and persists trace IDs in turn state.
- State transitions emit lifecycle events with turn ID, state, step cursor,
  timestamp, trace ID, and UI-safe status or error metadata.
- Resume uses persisted state, idempotency keys, approval references, event
  offsets, and trace context.
- Events and traces must not include secret values, credentials, private keys,
  unsafe production data, or raw business data beyond approved trace metadata.

Source: `docs/specs/spec-provider-credential-model-capability/SPEC.md`

- Provider completion, streaming, capability lookup, credential lookup, and
  provider error normalization must emit compatible events, trace tags,
  failure categories, and usage fields across replacements.

Source: `docs/specs/spec-budget-hooks-side-effects/SPEC.md`

- Budget and hook spans must carry usage units, hook IDs, redaction status, and
  side-effect decision tags.

Source: `docs/specs/spec-session-memory-context-compaction/SPEC.md`

- Sessions and compaction preserve trace context references, event offsets,
  queue position, and compaction summary IDs.

## Wrapper-Only Content

- GitHub issue URLs, user avatar metadata, API node IDs, and timestamps are
  process metadata and are not part of the product contract.
