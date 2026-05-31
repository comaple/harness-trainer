# Source Extract: Policy and Approval Gates

## Issue

Source: GitHub issue #52

- Create the BMad SPEC for `STORY-014 / FR-018` policy and approval gates.
- Scope includes policy checks before tool execution, allow/deny/
  needs-approval outcomes, fail-closed defaults, policy timeout behavior,
  malformed tool metadata handling, unavailable policy engine behavior, human
  approval request/resolution inputs, persisted decision state, resume
  semantics, lifecycle events, trace tags, and audit metadata.
- Acceptance requires policy timeout to produce denial or fail-closed before
  tool execution, approval decisions to resume without changing the original
  tool contract, each approval decision to have reason, actor, and traceable
  event, and mapping to `HC-005`, `FR-018`, `STORY-014`, and `EPIC-002`.

## PRD

Source: `docs/prd.md`

### FR-018: Policy and Approval Gates

The harness runtime plan must include policy checks before tool execution,
allow/deny/needs-approval outcomes, fail-closed behavior, human approval
resolution, and resumed execution after approval.

## Epic

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

- `EPIC-002` decomposes the target agent harness into replaceable, testable
  capabilities.
- `STORY-014` plans policy and approval gates.
- Acceptance requires each capability to identify its public contract, state
  boundary, failure behavior, and observability evidence.
- Replacement-sensitive capabilities must identify evaluator evidence and
  replacement safety criteria before implementation begins.
- The decomposition must not require adopting any specific external harness
  framework.

## Story

Source: `docs/stories/STORY-014-policy-approval-gates.md`

- As a maintainer, every tool call must pass through policy and approval gates
  so unsafe or human-sensitive actions are denied, paused, or resumed with an
  audit trail.
- Functional requirements: `FR-018`, `FR-014`, and `FR-021`.
- Implementation plan:
  - Specify the policy check contract and timeout.
  - Specify `allow`, `deny`, and `needs_approval` outcomes.
  - Specify fail-closed behavior when policy is unavailable.
  - Specify approval resolution inputs and persisted decision state.
  - Specify lifecycle events and trace tags for policy and approval decisions.
- Acceptance:
  - Policy timeout produces a denial outcome.
  - Approval decisions can be resumed without changing the original tool
    contract.
  - Every approval decision has a reason, actor, and traceable event.

## Capability Catalog

Source: `docs/harness/capability-catalog.md`

### HC-005: Policy and Approval Gates

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

## Worker Contract

Source: `docs/harness/worker-contract.md`

### Policy Check Capability

- Function ID: `policy.evaluate_tool_call`.
- Capability ID: `HC-005`.
- Trigger name: `evaluate_tool_policy`.
- Trigger style: synchronous call.
- Required input: `turn_id`, `session_id`, `tool_name`,
  `tool_args_summary`, `requested_effect`, and `actor_context`.
- Optional input: `approval_context` and `risk_tags`.
- Validation: `tool_name` and `requested_effect` are required; raw secrets and
  unredacted business data are invalid.
- Success output includes `decision`, `rule_id`, `decision_reason`, and
  `approval_request_id` only when `decision` is `needs_approval`.
- Non-terminal outcome `needs_approval` pauses execution until approval is
  resolved.
- Recoverable error `POLICY_CONTEXT_INCOMPLETE` means required policy context is
  missing but no unsafe action has run; caller must rebuild context and retry
  before tool execution.
- Fail-closed error `POLICY_ENGINE_UNAVAILABLE` forbids tool execution and must
  emit `policy.denied` or `policy.failed_closed` with
  `policy.fail_closed=true`.
- Fail-closed error `UNREDACTED_SECRET_IN_POLICY_INPUT` forbids tool execution
  and policy logging of raw input, and must emit redaction failure evidence
  without secret values.
- Timeout result: `POLICY_ENGINE_UNAVAILABLE`.
- Retry safety: Safe to retry with the same idempotency key before tool
  execution.
- Idempotency key: `turn_id + tool_call_id + policy_contract_version`.
- Duplicate handling: Return the existing decision record for the same key.
- State reads include policy rules and approval request state.
- State writes include policy decision record before permitted tool execution
  and durable approval request before returning `needs_approval`.
- Events include `policy.allowed`, `policy.denied`, and `approval.requested`.
- Trace tags include `tool.name`, `policy.rule_id`, and `policy.decision`, with
  redaction rules that exclude raw arguments.
- Contract version: `policy.evaluate_tool_call.v1`.
- Compatible change: Add optional non-secret risk tags.
- Breaking change: Rename decision values or change fail-closed behavior.
- Fixtures cover allowed, denied, approval-required, missing policy context,
  unavailable policy engine, unredacted secret input, and replacement
  comparison with identical decisions, events, trace tags, and state writes for
  the same redacted inputs.

## Neighboring Spec

Source: `docs/specs/spec-turn-intake-orchestration/SPEC.md`

- Tool/function execution must not occur before policy, credential, budget, and
  approval gates required by neighboring capabilities have passed.
- Approval waiting must preserve enough state to resume or reject the turn
  without replaying prior side effects.
- Failure behavior must distinguish policy denial and approval rejection from
  provider/tool failure, budget failure, timeout, interruption, and teardown
  failure.
- Events and traces must not include secret values, credentials, private keys,
  unsafe production data, or raw business data beyond approved trace metadata.

## Wrapper-Only Content

- GitHub issue URLs, user avatar metadata, API node IDs, and timestamps are
  process metadata and are not part of the product contract.
