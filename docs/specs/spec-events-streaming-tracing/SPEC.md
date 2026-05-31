---
id: SPEC-events-streaming-tracing
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #58. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Events Streaming and Tracing

## Why

`harness-trainer` needs events, streaming, and tracing so every business Agent
Harness turn can be observed, debugged, replayed, and compared across
replacement implementations. Token streams, UI-visible events, automation
events, and trace spans must share stable run, session, message, function,
turn, and trace identifiers so reviewers can diagnose failures across
capabilities without inspecting implementation internals.

## Capabilities

- id: CAP-1
  intent: The runtime can start, propagate, and finish one trace that spans a
    full turn.
  success: Trace operations produce a root trace ID, turn ID, run ID, session
    ID, root span ID, child span IDs, capability IDs, start/finish timestamps,
    terminal status, and redacted failure metadata.

- id: CAP-2
  intent: Runtime capabilities can emit structured events with stable
    identifiers.
  success: Events include event ID, event name, event type, sequence or offset,
    run ID, turn ID, session ID, message ID when applicable, function or tool
    call ID when applicable, trace ID, span ID, timestamp, payload schema
    version, and UI-safe payload metadata.

- id: CAP-3
  intent: Assistant output can stream as ordered token events.
  success: Token streaming emits `assistant.token_streamed` events with stream
    ID, message ID, provider/model reference, token offset, chunk content or
    redacted content reference, trace/span linkage, completion marker, and
    retry-safe offset semantics.

- id: CAP-4
  intent: UI and automation consumers can correlate visible events to trace
    spans.
  success: UI events and automation events carry trace ID, span ID, event ID,
    run ID, turn ID, session ID, display-safe status, and source capability so
    a visible update can be mapped to the producing span.

- id: CAP-5
  intent: Event streams can be replayed for debugging without duplicating
    side effects.
  success: Replay uses event IDs, stream offsets, sequence numbers,
    idempotency keys, trace IDs, and terminal markers to reconstruct the
    visible run history while distinguishing replay from live execution.

- id: CAP-6
  intent: Observability failures are explicit and diagnosable.
  success: Event emission failures do not silently drop audit events; missing
    trace context is rejected when required; unrecoverable trace failures mark
    the turn `observability-degraded` with failing capability, error class,
    preserved offsets, and UI-safe diagnostics.

## Constraints

- The capability must be technology-neutral and must not require a specific
  event bus, stream transport, tracing backend, browser UI, model provider, or
  storage system.
- Event names, ordering rules, stream offsets, trace propagation fields, replay
  semantics, and failure categories must remain stable across replacements.
- Every runtime capability must emit or forward trace context when it performs
  work that affects turn state, user-visible output, side effects, approvals,
  budget, session state, or evaluator evidence.
- Event payloads must include enough identifiers to correlate UI-visible
  events, automation events, token streams, and trace spans without inspecting
  implementation internals.
- Token stream offsets must be monotonic within a stream and safe to resume or
  replay without duplicating already emitted chunks.
- Audit-critical events must not be silently dropped; if delivery fails, the
  failure must be recorded or surfaced as observability-degraded according to
  severity.
- Failed turns must emit enough UI-safe information to identify the failing
  capability, failure class, trace/span location, and preserved state needed
  for debugging.
- Events and traces must not include secret values, private keys, raw
  credentials, unsafe production data, or raw business data beyond approved
  trace metadata.
- Replacement implementations must preserve event names, ordering, stream
  offsets, trace propagation fields, replay compatibility, required span
  attributes, failure behavior, and fixture outcomes.

## Non-goals

- This SPEC does not implement an event bus, streaming server, tracing backend,
  UI renderer, browser client, log sink, storage system, or replay tool.
- This SPEC does not choose a concrete telemetry product, protocol, queue,
  database, browser framework, or model streaming API.
- This SPEC does not define business-domain event semantics for a specific
  Agent.
- This SPEC does not authorize event payloads or traces to carry secrets,
  credentials, raw business data, or unsafe production data.
- This SPEC does not replace turn orchestration, provider/model capability,
  policy, budget/hooks, session/memory, or evaluator capabilities.

## Success signal

A reviewer can inspect the events, streaming, and tracing contract and
determine how token streams, UI events, automation events, trace roots, spans,
event IDs, stream offsets, replay, missing-trace failures, and
observability-degraded outcomes work across a full turn without relying on chat
history or a concrete telemetry framework.

## Assumptions

- The first implementation can be contract-first documentation and fixtures
  before a concrete event transport or tracing backend exists.
- Event payload schemas can begin as Markdown contract fields and later become
  machine-readable schemas.
- Some trace failures can be degraded rather than terminal, but missing trace
  context remains fail-closed for operations that require audit evidence.

## Open Questions

- Which event names should be globally reserved versus capability-owned?
- Should replay be implemented from the event stream alone, or from event
  stream plus durable turn/session state?
