# Worker Contract Model

Traceability: FR-014, STORY-010

## Purpose

This document defines the technology-neutral worker contract model for
replaceable harness capabilities. It is governed by
`docs/specs/spec-replaceable-harness-capabilities/SPEC.md` and references
capability IDs from `docs/harness/capability-catalog.md`.

A worker contract defines one callable or event-triggered unit at a capability
boundary. A capability may expose multiple worker contracts, but each contract
must be independently testable and comparable against a replacement
implementation.

## Contract Types

Worker contracts support two trigger styles:

- Synchronous call: the runtime invokes the worker and waits for a typed result.
- Event-triggered handler: the runtime or event bus delivers a named event and
  the worker produces state changes, emitted events, or a terminal result.

Both styles use the same required fields so replacements can be compared
without depending on a specific framework, queue, process model, or language.

## Required Contract Fields

Every worker contract must include these fields:

- function ID
- capability ID
- trigger name
- input shape
- output shape
- recoverable errors
- fail-closed errors
- timeout
- idempotency
- state reads
- state writes
- emitted events
- trace tags
- version expectations
- fixture expectations

## Field Semantics

### Function ID

The stable identifier for this worker contract. It must be unique inside the
repository and should use capability-oriented names, for example
`policy.evaluate_tool_call`.

### Capability ID

The capability that owns this worker contract. The value must reference a
capability ID from `docs/harness/capability-catalog.md`, such as `HC-005`.

### Trigger Name

The operation or event that invokes the worker. For synchronous calls, use the
operation name. For event-triggered handlers, use the event name.

### Input Shape

The accepted input fields, required fields, optional fields, and validation
rules. The shape should describe data contracts, not implementation classes.

### Output Shape

The successful result fields and the allowed non-terminal outcomes. Outputs must
include enough status information for neighboring capabilities to continue
without inspecting implementation internals.

### Recoverable Errors

Errors where the caller may retry, resume, ask for approval, or continue in a
degraded state. Each recoverable error must define:

- error code
- meaning
- caller action
- preserved state, if any

### Fail-Closed Errors

Errors where execution must stop before side effects, tool execution, credential
exposure, or irreversible state mutation. Each fail-closed error must define:

- error code
- meaning
- forbidden next action
- required event or trace evidence

### Timeout

The maximum allowed duration and the timeout result. Timeout behavior must state
whether the worker is safe to retry and whether partial state may exist.

### Idempotency

The idempotency key or rule used to prevent duplicated state writes, events, or
side effects. Non-idempotent workers must explicitly say why and name the guard
that prevents duplicate execution.

### State Reads

The durable state, cache, queue, or external record the worker may read. Reads
must be scoped to the capability boundary.

### State Writes

The durable state, cache, queue, or external record the worker may write. Writes
must name the owning capability and any ordering or atomicity expectation.

### Emitted Events

The events the worker may emit, including success, failure, degraded, and audit
events. Event names should match the capability catalog where applicable.

### Trace Tags

The trace fields required for observability and replacement comparison. Trace
tags must not include secrets or raw business data unless explicitly approved
by a future security requirement.

### Version Expectations

The contract version, compatibility rule, and allowed evolution path. Breaking
changes must require a new contract version and updated fixtures.

### Fixture Expectations

The fixture documents, test cases, or examples required to prove the contract.
At minimum, each contract needs one passing fixture and one failing fixture.

## Contract Template

```text
Function ID:
Capability ID:
Trigger name:
Trigger style: synchronous call | event-triggered handler

Input shape:
- Required:
- Optional:
- Validation:

Output shape:
- Success:
- Non-terminal outcomes:

Recoverable errors:
- Code:
  Meaning:
  Caller action:
  Preserved state:

Fail-closed errors:
- Code:
  Meaning:
  Forbidden next action:
  Required evidence:

Timeout:
- Limit:
- Timeout result:
- Retry safety:

Idempotency:
- Key or rule:
- Duplicate handling:

State reads:
- Name:
  Owner:
  Purpose:

State writes:
- Name:
  Owner:
  Ordering or atomicity:

Emitted events:
- Name:
  When emitted:

Trace tags:
- Name:
  Purpose:
  Redaction rule:

Version expectations:
- Contract version:
- Compatible change:
- Breaking change:

Fixture expectations:
- Passing fixtures:
- Failing fixtures:
- Replacement comparison fixtures:
```

## Replacement Comparison Semantics

A replacement implementation is compatible only when all required comparison
checks pass.

### Accepted Input Shape

The replacement must accept every required input field and validation rule from
the current contract. It may accept additional optional fields only when those
fields do not change behavior for existing callers.

### Compatible Output Shape

The replacement must return every success and non-terminal output field required
by the current contract. Additional output fields are compatible only when
callers can ignore them safely.

### Equivalent Failure Behavior

Recoverable errors must remain recoverable with the same caller action.
Fail-closed errors must still stop the same unsafe next actions. A replacement
must not downgrade a fail-closed error into a warning, degraded status, or
recoverable error.

### Equivalent State Boundary

The replacement must read and write only the state named in the contract unless
a new contract version expands the state boundary. It must preserve state owner,
ordering, atomicity, and idempotency rules.

### Equivalent Event and Trace Evidence

The replacement must emit the same required events and trace tags for equivalent
paths. It may emit additional diagnostic events only if required events remain
stable and ordering-sensitive consumers are not affected.

### Compatible Timeout and Idempotency

The replacement must preserve timeout result semantics, retry safety, duplicate
handling, and idempotency keys. A faster implementation is compatible; an
implementation that times out differently is not compatible unless callers are
updated through a new contract version.

### Fixture Result

The replacement must pass the current passing fixtures, current failing
fixtures, and replacement comparison fixtures. If fixture results differ, the
replacement is rejected until the contract version or fixtures are intentionally
updated.

## Evaluator Scoring Expectations

The harness training evaluator should score worker contracts with these
dimensions:

- Contract completeness: all required fields are present and non-empty.
- Catalog linkage: capability IDs exist in
  `docs/harness/capability-catalog.md`.
- Error clarity: recoverable and fail-closed errors are distinct.
- State boundary clarity: reads and writes name owners and purposes.
- Event and trace evidence: emitted events and trace tags are specified.
- Replacement safety: comparison semantics are satisfied by fixture evidence.
- Fixture coverage: passing, failing, and replacement comparison fixtures are
  named.

## Example: Policy Check Capability

### Contract

- Function ID: `policy.evaluate_tool_call`
- Capability ID: `HC-005`
- Trigger name: `evaluate_tool_policy`
- Trigger style: synchronous call

### Input Shape

- Required:
  - `turn_id`: stable turn identifier.
  - `session_id`: stable session identifier.
  - `tool_name`: requested tool name.
  - `tool_args_summary`: redacted summary of proposed arguments.
  - `requested_effect`: declared side effect class.
  - `actor_context`: role or agent identity used for policy evaluation.
- Optional:
  - `approval_context`: existing approval request or resume token.
  - `risk_tags`: caller-provided risk hints.
- Validation:
  - `tool_name` and `requested_effect` are required.
  - Raw secrets and unredacted business data are invalid.

### Output Shape

- Success:
  - `decision`: one of `allow`, `deny`, or `needs_approval`.
  - `rule_id`: policy rule that produced the decision.
  - `decision_reason`: redacted explanation for audit.
  - `approval_request_id`: present only when `decision` is `needs_approval`.
- Non-terminal outcomes:
  - `needs_approval` pauses execution until approval is resolved.

### Recoverable Errors

- Code: `POLICY_CONTEXT_INCOMPLETE`
  - Meaning: Required policy context is missing but no unsafe action has run.
  - Caller action: Rebuild context and retry before tool execution.
  - Preserved state: Original turn state and proposed tool call metadata.

### Fail-Closed Errors

- Code: `POLICY_ENGINE_UNAVAILABLE`
  - Meaning: The policy decision cannot be produced.
  - Forbidden next action: Tool execution.
  - Required evidence: Emit `policy.denied` or `policy.failed_closed` and trace
    tag `policy.fail_closed=true`.
- Code: `UNREDACTED_SECRET_IN_POLICY_INPUT`
  - Meaning: Policy input includes data that must not enter policy logs.
  - Forbidden next action: Tool execution and policy logging of raw input.
  - Required evidence: Emit redaction failure evidence without secret values.

### Timeout

- Limit: The project-specific timeout must be declared by implementation
  stories before runtime use.
- Timeout result: `POLICY_ENGINE_UNAVAILABLE`.
- Retry safety: Safe to retry with the same idempotency key before tool
  execution.

### Idempotency

- Key or rule: `turn_id + tool_call_id + policy_contract_version`.
- Duplicate handling: Return the existing decision record when the same key is
  evaluated again.

### State Reads

- Name: policy rules
  - Owner: `HC-005`
  - Purpose: Determine allow, deny, or needs-approval outcome.
- Name: approval request state
  - Owner: `HC-005`
  - Purpose: Determine whether an approval context can resume execution.

### State Writes

- Name: policy decision record
  - Owner: `HC-005`
  - Ordering or atomicity: Must be written before any permitted tool execution.
- Name: approval request
  - Owner: `HC-005`
  - Ordering or atomicity: Must be durable before returning `needs_approval`.

### Emitted Events

- Name: `policy.allowed`
  - When emitted: Decision is `allow`.
- Name: `policy.denied`
  - When emitted: Decision is `deny` or policy fails closed.
- Name: `approval.requested`
  - When emitted: Decision is `needs_approval`.

### Trace Tags

- Name: `tool.name`
  - Purpose: Identify the requested tool.
  - Redaction rule: Tool name only; no raw arguments.
- Name: `policy.rule_id`
  - Purpose: Identify the rule that produced the decision.
  - Redaction rule: Rule ID only.
- Name: `policy.decision`
  - Purpose: Compare replacement behavior.
  - Redaction rule: Enum value only.

### Version Expectations

- Contract version: `policy.evaluate_tool_call.v1`
- Compatible change: Add optional non-secret risk tags.
- Breaking change: Rename decision values or change fail-closed behavior.

### Fixture Expectations

- Passing fixtures:
  - allowed tool call
  - denied tool call
  - approval-required tool call
- Failing fixtures:
  - missing policy context
  - unavailable policy engine
  - unredacted secret input
- Replacement comparison fixtures:
  - existing implementation and replacement produce identical decisions,
    events, trace tags, and state writes for the same redacted inputs.

## Example: Model Capability Lookup

### Contract

- Function ID: `model.lookup_capabilities`
- Capability ID: `HC-003`
- Trigger name: `lookup_model_capabilities`
- Trigger style: synchronous call

### Input Shape

- Required:
  - `provider_key`: provider identifier.
  - `model_key`: model identifier or selector.
  - `turn_id`: stable turn identifier.
- Optional:
  - `freshness_requirement`: maximum accepted age for cached capability data.
  - `requested_features`: feature list such as streaming or tool calls.
- Validation:
  - Provider and model keys must be non-empty.
  - Unknown providers are invalid.

### Output Shape

- Success:
  - `provider_key`: provider identifier.
  - `model_key`: resolved model identifier.
  - `supports_streaming`: boolean.
  - `supports_tool_calls`: boolean.
  - `context_window_tokens`: numeric limit or unknown marker.
  - `usage_accounting_unit`: unit used for budget recording.
  - `freshness`: current, stale, or unknown.
- Non-terminal outcomes:
  - `unsupported` means the caller must select another model or fail before
    execution.

### Recoverable Errors

- Code: `MODEL_CAPABILITY_STALE`
  - Meaning: Capability data exists but does not meet freshness requirements.
  - Caller action: Refresh capability data or retry with relaxed freshness.
  - Preserved state: Cached capability record with stale marker.

### Fail-Closed Errors

- Code: `MODEL_UNSUPPORTED`
  - Meaning: The selected model cannot satisfy required features.
  - Forbidden next action: Model execution for the current turn step.
  - Required evidence: Emit `model_capability.unsupported` with redacted tags.
- Code: `PROVIDER_UNKNOWN`
  - Meaning: Provider key has no registered capability source.
  - Forbidden next action: Credential lookup and model execution.
  - Required evidence: Trace provider lookup failure without credentials.

### Timeout

- Limit: The project-specific timeout must be declared by implementation
  stories before runtime use.
- Timeout result: `MODEL_CAPABILITY_STALE` when cached data exists, otherwise
  `PROVIDER_UNKNOWN`.
- Retry safety: Safe to retry; no side effect occurs beyond cache refresh.

### Idempotency

- Key or rule: `provider_key + model_key + freshness_requirement`.
- Duplicate handling: Return the same cached or refreshed capability record for
  equivalent lookup keys.

### State Reads

- Name: model capability registry
  - Owner: `HC-003`
  - Purpose: Resolve model behavior before execution.
- Name: cached capability records
  - Owner: `HC-003`
  - Purpose: Avoid unnecessary provider lookups and preserve provenance.

### State Writes

- Name: cached capability record
  - Owner: `HC-003`
  - Ordering or atomicity: Write after successful refresh with provenance.

### Emitted Events

- Name: `model_capability.lookup_started`
  - When emitted: Lookup begins.
- Name: `model_capability.resolved`
  - When emitted: Capability data is usable.
- Name: `model_capability.unsupported`
  - When emitted: Required features are unavailable.

### Trace Tags

- Name: `provider.key`
  - Purpose: Identify provider routing.
  - Redaction rule: Provider key only; no credentials.
- Name: `model.key`
  - Purpose: Identify model selection.
  - Redaction rule: Model key only.
- Name: `model.freshness`
  - Purpose: Compare cache and refresh behavior.
  - Redaction rule: Enum value only.

### Version Expectations

- Contract version: `model.lookup_capabilities.v1`
- Compatible change: Add optional capability fields that callers can ignore.
- Breaking change: Remove required fields or change unsupported-model behavior.

### Fixture Expectations

- Passing fixtures:
  - streaming-supported model
  - non-streaming model
  - tool-call-supported model
- Failing fixtures:
  - unsupported model
  - unknown provider
  - stale capability data
- Replacement comparison fixtures:
  - existing implementation and replacement produce compatible capability
    fields, unsupported-model behavior, emitted events, and trace tags.

## Reviewer Validation Checklist

- [ ] Every worker contract includes all required fields.
- [ ] Every capability ID exists in
  `docs/harness/capability-catalog.md`.
- [ ] Every contract distinguishes recoverable errors from fail-closed errors.
- [ ] Every fail-closed error names the forbidden next action.
- [ ] Every contract states timeout and idempotency behavior.
- [ ] Every contract names state reads, state writes, emitted events, and trace
  tags.
- [ ] Replacement comparison semantics are explicit enough to evaluate a second
  implementation without modifying neighboring capabilities.
- [ ] Passing, failing, and replacement comparison fixtures are named before
  implementation begins.
