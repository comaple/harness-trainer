# Source Extract: Session Memory and Context Compaction

## Issue

Source: GitHub issue #56

- Create the BMad SPEC for `STORY-016 / FR-020` session, memory, and context
  compaction.
- Scope includes persistent session state, session branching, per-session
  queues, memory read/write boundaries, session resume, context-window
  measurement, threshold-driven compaction triggers, compaction summaries,
  preservation of task/approval/trace/queue/replay context, lifecycle events,
  trace tags, failure semantics, and replacement criteria.
- Acceptance requires resumable persisted sessions, parent/child traceability
  for branches, deterministic compaction with evidence, no loss of active task,
  approval, or trace context, and mapping to `HC-007`, `FR-020`, `STORY-016`,
  and `EPIC-002`.

## PRD

Source: `docs/prd.md`

### FR-020: Session, Memory, and Context Compaction

The harness runtime plan must include branching session storage, resumable
state, per-session queues, context window monitoring, and context compaction.

## Epic

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

- `EPIC-002` decomposes the target agent harness into replaceable, testable
  capabilities.
- `STORY-016` plans session, memory, and context compaction.
- Acceptance requires each capability to identify its public contract, state
  boundary, failure behavior, and observability evidence.
- Replacement-sensitive capabilities must identify evaluator evidence and
  replacement safety criteria before implementation begins.
- The decomposition must not require adopting any specific external harness
  framework.

## Story

Source: `docs/stories/STORY-016-session-memory-context-compaction.md`

- As an agent operator, session state, memory, and context compaction must be
  durable and branchable so long-running agents can fork, resume, and stay
  within context limits.
- Functional requirements: `FR-020`, `FR-015`, and `FR-021`.
- Implementation plan:
  - Specify session tree records and parent links.
  - Specify per-session inbox or queue behavior.
  - Specify resume and fork behavior.
  - Specify compaction triggers based on context window thresholds.
  - Specify compaction output events and trace tags.
- Acceptance:
  - Sessions can be resumed from persisted state.
  - Forked sessions preserve parent lineage.
  - Compaction is triggered deterministically and emits evidence.

## Capability Catalog

Source: `docs/harness/capability-catalog.md`

### HC-007: Session, Memory, and Context Compaction

- Intent: Persist sessions as resumable and branchable state, manage
  per-session queues, monitor context-window pressure, and compact context
  without losing required traceability.
- Public contract surface: `load_session`, `save_session`, `branch_session`,
  `enqueue_session_item`, `measure_context_pressure`, and `compact_context`
  operations.
- State ownership: Owns session metadata, branch ancestry, queued work,
  context-window measurements, and compaction summaries.
- Emitted events: `session.loaded`, `session.saved`, `session.branched`,
  `context.pressure_measured`, and `context.compacted`.
- Failure behavior: Missing or corrupt session state fails closed with a
  recoverable diagnostic; compaction must reject outputs that drop required
  task, approval, or trace context.
- Replacement boundary: A replacement must preserve session IDs, branch
  ancestry, resume semantics, queue ordering, and compaction retention rules.
- Evaluator evidence: Fixtures for resume, branch, queue ordering, compaction
  pass, and compaction rejection cases.
- Trace evidence: Session spans tagged with session ID, branch ID, queue
  position, context size, and compaction summary ID.

## Worker Contract

Source: `docs/harness/worker-contract.md`

- Worker contracts require output status sufficient for neighboring
  capabilities to continue without inspecting implementation internals.
- Recoverable errors define code, meaning, caller action, and preserved state.
- Fail-closed errors stop before side effects, tool execution, credential
  exposure, or irreversible state mutation, and require event or trace
  evidence.
- Timeout behavior must state retry safety and whether partial state may exist.
- Idempotency prevents duplicated state writes, events, or side effects.
- State reads/writes must remain scoped to the capability boundary.
- Trace tags must not include secrets or raw business data unless explicitly
  approved by a future security requirement.
- Replacement comparison requires equivalent state boundary, compatible
  timeout and idempotency, equivalent events and trace tags, and fixture
  compatibility.
- Evaluator scoring expects contract completeness, catalog linkage, error
  clarity, state boundary clarity, event and trace evidence, replacement
  safety, and fixture coverage.

## Neighboring Specs

Source: `docs/specs/spec-turn-intake-orchestration/SPEC.md`

- Turn state records include turn ID, session ID, retry/resume metadata, event
  offsets, and trace IDs.
- Interrupted or approval-waiting turns resume using persisted state,
  idempotency keys, approval references, event offsets, and trace context.
- Approval waiting must preserve enough state to resume or reject the turn
  without replaying prior side effects.
- The turn orchestration SPEC does not implement session or memory
  capabilities.

Source: `docs/specs/spec-provider-credential-model-capability/SPEC.md`

- Model capability lookup resolves context-window tokens and an unknown marker.
- Model capability lookup must precede model execution when context window
  limits affect the run.

Source: `docs/specs/spec-budget-hooks-side-effects/SPEC.md`

- Budget and hooks consume turn ID and session ID.
- Custom side effects and logs require redacted, traceable evidence and must
  not duplicate side effects.

## Wrapper-Only Content

- GitHub issue URLs, user avatar metadata, API node IDs, and timestamps are
  process metadata and are not part of the product contract.
