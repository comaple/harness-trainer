# Harness Capability Catalog

Traceability: FR-013, STORY-009

## Purpose

This catalog defines the replaceable capability map for the harness-training
system. It is governed by
`docs/specs/spec-replaceable-harness-capabilities/SPEC.md` and supports
`EPIC-002`.

The catalog is technology-neutral. It defines what each harness capability must
promise at its boundary before an implementation is selected.

## Catalog Entry Rules

Every capability entry must include:

- capability ID
- capability name
- product area
- owning FR IDs
- owning Story IDs
- intent
- public contract surface
- state ownership
- emitted events
- failure behavior
- replacement boundary
- evaluator evidence
- trace evidence

## Turn Runtime

### HC-001: Turn Intake and Orchestration

- Capability ID: `HC-001`
- Capability name: Turn Intake and Orchestration
- Product area: turn runtime
- Owning FR IDs: `FR-015`
- Owning Story IDs: `STORY-011`
- Intent: Accept a business-agent turn, persist the request, advance the turn
  through deterministic steps, and coordinate model calls, tool calls, steering,
  and teardown.
- Public contract surface: `submit_turn`, `load_turn`, `step_turn`,
  `complete_turn`, and `fail_turn` operations with stable turn identifiers and
  typed turn state transitions.
- State ownership: Owns durable turn state, step cursor, terminal status,
  interruption reason, and resume metadata.
- Emitted events: `turn.accepted`, `turn.step_started`,
  `turn.step_completed`, `turn.completed`, and `turn.failed`.
- Failure behavior: Invalid turn requests fail closed before persistence;
  resumable runtime failures preserve the last successful step and expose a
  retryable status.
- Replacement boundary: A replacement is valid only if it preserves turn IDs,
  state transition semantics, terminal statuses, resume behavior, and emitted
  event names.
- Evaluator evidence: Fixture turns covering accepted, failed, interrupted,
  resumed, and completed flows.
- Trace evidence: One trace span per turn and child spans for each step.

## Provider and Credentials

### HC-002: Provider Credential Resolution

- Capability ID: `HC-002`
- Capability name: Provider Credential Resolution
- Product area: provider and credentials
- Owning FR IDs: `FR-016`
- Owning Story IDs: `STORY-012`
- Intent: Resolve the credentials and provider configuration needed for a model
  or tool call without leaking secrets into logs, prompts, or traces.
- Public contract surface: `resolve_provider_credentials` and
  `resolve_tool_credentials` operations that accept a provider or tool key and
  return a redacted credential handle plus capability metadata.
- State ownership: Does not own secret values; owns only redacted credential
  references, lookup status, and expiration metadata.
- Emitted events: `credential.lookup_started`, `credential.resolved`,
  `credential.denied`, and `credential.expired`.
- Failure behavior: Missing, expired, or unauthorized credentials fail closed
  and return redacted diagnostics.
- Replacement boundary: A replacement must preserve redaction guarantees,
  authorization checks, expiration semantics, and failure categories.
- Evaluator evidence: Passing and failing credential lookup fixtures with
  assertions that no secret value appears in outputs.
- Trace evidence: Credential lookup spans with redacted provider/tool tags.

### HC-003: Model Capability Lookup

- Capability ID: `HC-003`
- Capability name: Model Capability Lookup
- Product area: provider and credentials
- Owning FR IDs: `FR-016`
- Owning Story IDs: `STORY-012`
- Intent: Report provider and model capabilities needed by the turn runtime,
  including streaming support, context-window limits, tool-call support, and
  usage accounting expectations.
- Public contract surface: `lookup_model_capabilities` operation keyed by model
  selector and provider context.
- State ownership: Owns cached model capability records, freshness metadata,
  and lookup provenance.
- Emitted events: `model_capability.lookup_started`,
  `model_capability.resolved`, and `model_capability.unsupported`.
- Failure behavior: Unknown models fail closed before execution; stale records
  must be marked and may be rejected by policy.
- Replacement boundary: A replacement must preserve capability field names,
  freshness semantics, unsupported-model behavior, and usage-accounting fields.
- Evaluator evidence: Fixtures for streaming-supported, non-streaming,
  unsupported, and stale-capability cases.
- Trace evidence: Lookup spans tagged with provider, model key, freshness, and
  capability result.

## Skills and Prompt Assembly

### HC-004: Skill and Prompt Assembly

- Capability ID: `HC-004`
- Capability name: Skill and Prompt Assembly
- Product area: skills and prompt assembly
- Owning FR IDs: `FR-017`
- Owning Story IDs: `STORY-013`
- Intent: Discover applicable skills, load their instructions, and assemble the
  working prompt from mode, identity, workspace context, skills, and overrides.
- Public contract surface: `discover_skills`, `load_skill_context`, and
  `assemble_prompt_context` operations.
- State ownership: Owns resolved skill list, prompt assembly inputs, prompt
  provenance, and applied override metadata.
- Emitted events: `skill.discovered`, `skill.loaded`,
  `prompt.assembled`, and `prompt.override_applied`.
- Failure behavior: Missing required skills or invalid override instructions
  fail closed; optional skill failures are recorded without blocking unless the
  story requires them.
- Replacement boundary: A replacement must preserve skill selection rules,
  prompt ordering rules, override precedence, and provenance output.
- Evaluator evidence: Fixtures for no-skill, single-skill, multi-skill, missing
  required skill, and prompt-override cases.
- Trace evidence: Prompt assembly spans listing skill IDs, source paths, and
  applied override identifiers.

## Policy and Approvals

### HC-005: Policy and Approval Gates

- Capability ID: `HC-005`
- Capability name: Policy and Approval Gates
- Product area: policy and approvals
- Owning FR IDs: `FR-018`
- Owning Story IDs: `STORY-014`
- Intent: Evaluate proposed tool calls and side effects before execution,
  returning allow, deny, or needs-approval outcomes with a fail-closed default.
- Public contract surface: `evaluate_tool_policy`,
  `request_human_approval`, and `resume_after_approval` operations.
- State ownership: Owns policy decision records, approval requests, approval
  responses, and resume tokens.
- Emitted events: `policy.allowed`, `policy.denied`,
  `approval.requested`, `approval.granted`, and `approval.rejected`.
- Failure behavior: Missing policy, malformed tool call metadata, or expired
  approvals fail closed before tool execution.
- Replacement boundary: A replacement must preserve decision categories,
  fail-closed behavior, approval resume semantics, and audit metadata.
- Evaluator evidence: Fixtures for allowed, denied, approval-required,
  approval-granted, approval-rejected, and expired-approval paths.
- Trace evidence: Policy spans tagged with tool name, decision, rule ID, and
  approval request ID when applicable.

## Budget and Hooks

### HC-006: Budget, Hooks, and Side Effects

- Capability ID: `HC-006`
- Capability name: Budget, Hooks, and Side Effects
- Product area: budget and hooks
- Owning FR IDs: `FR-019`
- Owning Story IDs: `STORY-015`
- Intent: Check spend and usage budgets, run before-call and after-call hooks,
  record spend, and execute permitted custom side effects.
- Public contract surface: `check_budget`, `record_usage`,
  `run_before_call_hooks`, `run_after_call_hooks`, and
  `run_redaction_hooks` operations.
- State ownership: Owns budget counters, usage records, hook outcomes, alert
  records, and redaction reports.
- Emitted events: `budget.checked`, `budget.exceeded`,
  `usage.recorded`, `hook.started`, `hook.completed`, and `hook.failed`.
- Failure behavior: Budget exhaustion and hook policy violations fail closed;
  non-critical hook failures are recorded and surfaced as degraded execution.
- Replacement boundary: A replacement must preserve budget accounting units,
  hook ordering, redaction-before-log behavior, and side-effect eligibility.
- Evaluator evidence: Fixtures for in-budget, over-budget, hook-success,
  hook-failure, redaction, and side-effect-denied cases.
- Trace evidence: Budget and hook spans with usage units, hook IDs, redaction
  status, and side-effect decision tags.

## Session and Context

### HC-007: Session, Memory, and Context Compaction

- Capability ID: `HC-007`
- Capability name: Session, Memory, and Context Compaction
- Product area: session and context
- Owning FR IDs: `FR-020`
- Owning Story IDs: `STORY-016`
- Intent: Persist sessions as resumable and branchable state, manage
  per-session queues, monitor context-window pressure, and compact context
  without losing required traceability.
- Public contract surface: `load_session`, `save_session`, `branch_session`,
  `enqueue_session_item`, `measure_context_pressure`, and `compact_context`
  operations.
- State ownership: Owns session metadata, branch ancestry, queued work,
  context-window measurements, and compaction summaries.
- Emitted events: `session.loaded`, `session.saved`,
  `session.branched`, `context.pressure_measured`, and `context.compacted`.
- Failure behavior: Missing or corrupt session state fails closed with a
  recoverable diagnostic; compaction must reject outputs that drop required
  task, approval, or trace context.
- Replacement boundary: A replacement must preserve session IDs, branch
  ancestry, resume semantics, queue ordering, and compaction retention rules.
- Evaluator evidence: Fixtures for resume, branch, queue ordering, compaction
  pass, and compaction rejection cases.
- Trace evidence: Session spans tagged with session ID, branch ID, queue
  position, context size, and compaction summary ID.

## Events and Tracing

### HC-008: Events, Streaming, and Tracing

- Capability ID: `HC-008`
- Capability name: Events, Streaming, and Tracing
- Product area: events and tracing
- Owning FR IDs: `FR-021`
- Owning Story IDs: `STORY-017`
- Intent: Emit assistant token streams, UI events, automation events, and trace
  context that spans the full turn.
- Public contract surface: `emit_event`, `stream_assistant_token`,
  `start_trace`, `attach_trace_context`, and `finish_trace` operations.
- State ownership: Owns event IDs, stream offsets, trace IDs, span IDs, and
  event-to-trace linkage.
- Emitted events: `trace.started`, `trace.finished`,
  `assistant.token_streamed`, `ui.event_emitted`, and
  `automation.event_emitted`.
- Failure behavior: Event emission failures must not silently drop audit events;
  unrecoverable trace failures mark the turn as observability-degraded.
- Replacement boundary: A replacement must preserve event names, ordering,
  stream offsets, trace propagation fields, and replay compatibility.
- Evaluator evidence: Fixtures for ordered token streaming, replayable events,
  missing trace rejection, and degraded observability reporting.
- Trace evidence: Root trace for each turn and linked spans for model calls,
  tool calls, approvals, hooks, and emitted events.

## Evaluation

### HC-009: Harness Training Evaluator

- Capability ID: `HC-009`
- Capability name: Harness Training Evaluator
- Product area: evaluation
- Owning FR IDs: `FR-022`
- Owning Story IDs: `STORY-018`
- Intent: Score harness designs and implementation artifacts against the
  capability catalog, worker contracts, failure semantics, observability, and
  replacement safety.
- Public contract surface: `evaluate_harness_artifacts`,
  `score_capability_coverage`, and `compare_replacement_candidate`
  operations.
- State ownership: Owns evaluator fixture set, scoring dimensions, score
  reports, missing-coverage reports, and replacement-safety reports.
- Emitted events: `evaluation.started`, `evaluation.completed`,
  `evaluation.failed`, and `replacement_candidate.rejected`.
- Failure behavior: Missing required catalog or contract evidence fails the
  evaluation; invalid replacement evidence is reported as rejected, not
  accepted with warnings.
- Replacement boundary: A replacement must preserve score dimensions, required
  evidence checks, rejection semantics, and report structure.
- Evaluator evidence: Passing and failing fixture documents plus accepted and
  rejected replacement-candidate fixtures.
- Trace evidence: Evaluation run ID, artifact list, score dimensions, missing
  coverage list, and replacement-safety result.

## Catalog Governance

### HC-010: Capability Catalog Governance

- Capability ID: `HC-010`
- Capability name: Capability Catalog Governance
- Product area: evaluation
- Owning FR IDs: `FR-013`, `FR-014`, `FR-022`
- Owning Story IDs: `STORY-009`, `STORY-010`, `STORY-018`
- Intent: Keep capability definitions, worker contracts, and evaluator checks
  aligned as implementation proceeds.
- Public contract surface: `validate_capability_catalog`,
  `validate_contract_references`, and `validate_evaluator_evidence`
  operations.
- State ownership: Owns catalog validation rules, required field set, and
  traceability checks between catalog, contracts, and evaluator fixtures.
- Emitted events: `catalog.validation_started`,
  `catalog.validation_completed`, and `catalog.validation_failed`.
- Failure behavior: Missing required fields, broken FR/story references, or
  absent evaluator evidence fail validation before implementation is accepted.
- Replacement boundary: A replacement must preserve required field validation,
  cross-reference checks, and failure behavior.
- Evaluator evidence: Fixtures with complete entries, missing required fields,
  invalid FR references, invalid story references, and absent evidence.
- Trace evidence: Validation report listing catalog entry IDs, referenced FRs,
  referenced stories, and failed checks.

## Runtime FR Coverage

| FR | Capability IDs | Story IDs |
| --- | --- | --- |
| `FR-013` | `HC-010` | `STORY-009` |
| `FR-014` | `HC-010` | `STORY-010` |
| `FR-015` | `HC-001` | `STORY-011` |
| `FR-016` | `HC-002`, `HC-003` | `STORY-012` |
| `FR-017` | `HC-004` | `STORY-013` |
| `FR-018` | `HC-005` | `STORY-014` |
| `FR-019` | `HC-006` | `STORY-015` |
| `FR-020` | `HC-007` | `STORY-016` |
| `FR-021` | `HC-008` | `STORY-017` |
| `FR-022` | `HC-009`, `HC-010` | `STORY-018` |

## Reviewer Validation Checklist

- [ ] Every runtime FR from `FR-013` through `FR-022` appears in the coverage
  table.
- [ ] Every capability entry has all required catalog fields.
- [ ] Every capability entry names a public contract surface.
- [ ] Every capability entry defines state ownership and failure behavior.
- [ ] Every capability entry defines emitted events and trace evidence.
- [ ] Every capability entry defines replacement boundary and evaluator
  evidence.
- [ ] The catalog does not require a specific implementation framework.
- [ ] Future worker contracts reference the capability IDs defined here.
