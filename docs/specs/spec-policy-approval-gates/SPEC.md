---
id: SPEC-policy-approval-gates
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #52. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Policy and Approval Gates

## Why

`harness-trainer` needs policy and approval gates so every tool call and side
effect is evaluated before execution. Unsafe or human-sensitive actions must be
allowed, denied, paused for approval, or resumed with durable state, UI-safe
diagnostics, audit metadata, lifecycle events, and trace evidence.

## Capabilities

- id: CAP-1
  intent: The runtime can evaluate proposed tool calls before execution.
  success: Policy evaluation accepts turn ID, session ID, tool name, redacted
    argument summary, requested effect, actor context, optional approval
    context, and risk tags; raw secrets and unredacted business data are
    rejected before policy logging or tool execution.

- id: CAP-2
  intent: Policy decisions use a stable allow, deny, or needs-approval outcome
    model.
  success: Each decision returns `allow`, `deny`, or `needs_approval`, a rule
    ID, a redacted decision reason, and an approval request ID only when
    approval is required.

- id: CAP-3
  intent: Policy failures stop unsafe work before side effects.
  success: Missing policy context remains recoverable before tool execution;
    unavailable policy engine, timeout, malformed tool call metadata, missing
    policy, unredacted secret input, and expired approval fail closed before
    tool execution.

- id: CAP-4
  intent: Human approval requests are durable and resumable.
  success: Approval requests persist original turn ID, session ID, tool call
    reference, redacted proposed action, rule ID, decision reason, requested
    approver or role, request timestamp, expiration, status, and resume token
    before returning `needs_approval`.

- id: CAP-5
  intent: Approval resolution preserves the original tool contract.
  success: Approval grant or rejection records actor, reason, timestamp,
    approval request ID, resume token, and terminal approval status; resume
    reuses the original tool call contract and policy decision context without
    mutating the original tool request.

- id: CAP-6
  intent: Policy and approval decisions are observable and comparable across
    replacements.
  success: Decisions emit `policy.allowed`, `policy.denied`,
    `approval.requested`, `approval.granted`, or `approval.rejected` with
    UI-safe metadata, and trace tags include tool name, policy decision, rule
    ID, fail-closed marker, and approval request ID when applicable.

## Constraints

- The capability must be technology-neutral and must not require a specific
  policy engine, approval workflow tool, secrets manager, queue, database,
  event bus, or tracing backend.
- Tool execution and irreversible side effects must not occur before required
  policy and approval gates pass.
- Policy evaluation input must contain only redacted argument summaries and
  approved metadata; raw secrets, private keys, raw credentials, and unsafe
  production data are invalid.
- Timeout must map to `POLICY_ENGINE_UNAVAILABLE` and produce a denial or
  fail-closed outcome before tool execution.
- `needs_approval` is non-terminal for the turn and must pause execution until
  approval is granted, rejected, expired, or cancelled.
- Approval request state must be durable before the runtime reports
  `needs_approval` to the turn orchestrator or UI.
- Expired, rejected, malformed, or missing approvals must fail closed before
  resumed tool execution.
- Replacement implementations must preserve decision categories, fail-closed
  behavior, approval resume semantics, audit metadata, emitted events, trace
  tags, state writes, and idempotency behavior.
- The contract must align with `HC-005`, `FR-018`, `STORY-014`, the worker
  contract model, and the turn orchestration approval-waiting state.

## Non-goals

- This SPEC does not implement a policy engine, approval UI, identity provider,
  workflow tool, database, queue, event bus, or tracing backend.
- This SPEC does not define enterprise policy rules for a specific business
  Agent.
- This SPEC does not grant approval for unsafe tool calls or side effects.
- This SPEC does not choose who may approve production actions in a specific
  organization.
- This SPEC does not replace turn orchestration, provider/credential, budget,
  session memory, event streaming, or evaluator capabilities.

## Success signal

A reviewer can inspect the policy and approval gates contract and determine how
a proposed tool call is evaluated, allowed, denied, paused for approval,
resolved, resumed, expired, or failed closed. The reviewer can see durable
approval state, immutable tool-call context, actor/reason audit fields,
UI-safe events, trace tags, and replacement comparison criteria without relying
on a concrete policy or approval implementation.

## Assumptions

- Approval resolution can initially be represented as a contract and persisted
  decision record before an approval UI exists.
- Policy rules may be business-agent specific, but the gate contract remains
  shared across business Agent Harnesses.
- The turn orchestrator owns the approval-waiting state cursor, while `HC-005`
  owns approval request and response records.

## Open Questions

- Should approval expiration be configured per policy rule, per tool, or per
  business Agent Harness blueprint?
- Should rejected approvals always terminate the turn, or can some cases resume
  with an alternate tool path selected by the orchestrator?
