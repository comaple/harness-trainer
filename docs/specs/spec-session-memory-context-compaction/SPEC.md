---
id: SPEC-session-memory-context-compaction
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #56. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Session Memory and Context Compaction

## Why

`harness-trainer` needs a session, memory, and context compaction capability so
business Agent Harnesses can run beyond a single turn, resume durable state,
fork session branches, maintain per-session work queues, and stay within model
context limits. Replacement implementations must preserve session lineage,
queue order, compaction retention, traceability, and resumability without
binding the harness to a specific database, queue, memory store, or compaction
algorithm.

## Capabilities

- id: CAP-1
  intent: Runtime sessions can be loaded and saved as durable, resumable state.
  success: Session records preserve session ID, owning business Agent Harness,
    actor or workspace scope, current turn references, resumable status,
    queue pointer, memory references, trace context references, version, and
    redacted diagnostic metadata.

- id: CAP-2
  intent: Operators can fork a session while preserving parent lineage.
  success: A branch operation creates a child session with a new session ID,
    parent session ID, branch ID, fork timestamp, inherited memory references,
    trace ancestry, and explicit divergence metadata before child work is
    accepted.

- id: CAP-3
  intent: Per-session work is queued and replayed in deterministic order.
  success: Queue operations accept a session ID, queue item ID, enqueue order,
    item type, payload reference, idempotency key, and trace context; dequeue
    and replay preserve ordering and avoid duplicate execution.

- id: CAP-4
  intent: Context-window pressure can be measured before model execution.
  success: Measurement records include session ID, turn ID, provider/model
    context-window limit or unknown marker, estimated prompt tokens, memory
    payload size, queued work contribution, threshold rule ID, and decision
    outcome.

- id: CAP-5
  intent: Context compaction is triggered deterministically when configured
    thresholds are reached.
  success: Compaction decisions declare trigger source, threshold rule,
    pre-compaction context measurement, retained task context, retained
    approval context, retained trace context, dropped or summarized references,
    and emitted `context.compacted` evidence.

- id: CAP-6
  intent: Compaction outputs preserve the state needed to continue safely.
  success: A compaction summary is accepted only when it keeps active task
    state, approval or resume tokens, queue position, trace identifiers,
    branch ancestry, memory provenance, and enough redacted diagnostic evidence
    to audit what changed.

## Constraints

- The capability must be technology-neutral and must not require a specific
  database, queue, vector store, cache, tracing backend, model provider, or
  compaction algorithm.
- Session state must be durable before queued work, branch work, resume work,
  or compaction-dependent model execution proceeds.
- Missing or corrupt session state must fail closed with a recoverable
  diagnostic before tool execution, provider execution, or irreversible side
  effects.
- Branching must preserve parent session ID, child session ID, branch ID, and
  trace ancestry.
- Queue ordering and idempotency must prevent duplicated work during resume,
  replay, retry, and branch execution.
- Context-window measurement must occur before model execution when context
  pressure can affect provider selection, prompt assembly, budget, or
  compaction.
- Compaction must reject outputs that drop active task state, approval context,
  resume tokens, queue position, required memory provenance, or trace context.
- Events and traces must not include secret values, private keys, raw
  credentials, unsafe production data, or raw business data beyond approved
  trace metadata.
- Replacement implementations must preserve session IDs, branch ancestry,
  resume semantics, queue ordering, context measurement fields, compaction
  retention rules, emitted events, trace tags, failure categories, and fixture
  outcomes.

## Non-goals

- This SPEC does not implement a session store, memory database, queue,
  compaction model, summarizer, token counter, event bus, or tracing backend.
- This SPEC does not choose a concrete retention algorithm, memory ranking
  strategy, prompt assembly strategy, database schema, or queue runtime.
- This SPEC does not define business-domain memory semantics for a specific
  Agent.
- This SPEC does not authorize unsafe replay, duplicate side effects, or
  compaction that hides required approval or trace evidence.
- This SPEC does not replace turn orchestration, provider/model capability,
  budget/hooks, event streaming, tracing, or evaluator capabilities.

## Success signal

A reviewer can inspect the session, memory, and context compaction contract and
determine how sessions are loaded, saved, branched, resumed, queued, measured
for context pressure, compacted, rejected when unsafe, and compared across
replacement implementations without relying on chat history or a concrete
runtime framework.

## Assumptions

- Memory content can initially be represented by references and provenance
  metadata before concrete memory storage exists.
- Context-window limits can come from the provider/model capability layer, with
  an explicit unknown marker when no limit is available.
- The first implementation can be contract-first documentation and fixtures,
  followed later by machine-readable worker contract templates.

## Open Questions

- Which context-pressure thresholds should be global defaults versus
  workspace-specific policy?
- Should compaction summaries be append-only audit records, mutable session
  state, or both?
