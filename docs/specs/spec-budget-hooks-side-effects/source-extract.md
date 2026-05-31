# Source Extract: Budget Hooks and Side Effects

## Issue

Source: GitHub issue #54

- Create the BMad SPEC for `STORY-015 / FR-019` budget, hooks, and side
  effects.
- Scope includes budget check, spend recording, alerting, forecasting, rollover
  behavior, before-call hooks, after-call hooks, redaction hooks, logging hooks,
  hook fanout, ordering, timeout, failure semantics, block/warn decisions before
  spend, permitted custom side-effect execution, side-effect denial,
  redaction-before-log behavior, lifecycle events, trace tags, and replacement
  criteria.
- Acceptance requires budget checks to block or warn before spend occurs,
  redaction hooks to run before logging hooks, hook failures to define whether
  execution is blocked, degraded, or allowed, and mapping to `HC-006`,
  `FR-019`, `STORY-015`, and `EPIC-002`.

## PRD

Source: `docs/prd.md`

### FR-019: Budget, Hooks, and Side Effects

The harness runtime plan must include budget checking, spend recording,
alerting, before-call hooks, after-call hooks, redaction hooks, logging hooks,
and custom side effects.

## Epic

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

- `EPIC-002` decomposes the target agent harness into replaceable, testable
  capabilities.
- `STORY-015` plans budget, hooks, and side effects.
- Acceptance requires each capability to identify its public contract, state
  boundary, failure behavior, and observability evidence.
- Replacement-sensitive capabilities must identify evaluator evidence and
  replacement safety criteria before implementation begins.
- The decomposition must not require adopting any specific external harness
  framework.

## Story

Source: `docs/stories/STORY-015-budget-hooks-side-effects.md`

- As a workspace owner, budget and hook behavior must be specified separately
  from the turn loop so spend limits, redaction, logging, and side effects can
  be added or replaced safely.
- Functional requirements: `FR-019`, `FR-016`, and `FR-021`.
- Implementation plan:
  - Specify budget check, record, alert, forecast, and rollover behavior.
  - Specify before-call and after-call hook contracts.
  - Specify hook fanout behavior and timeout semantics.
  - Specify redaction and logging hook examples.
  - Define how hook failures affect tool execution.
- Acceptance:
  - Budget checks can block or warn before spend occurs.
  - Usage recording happens after provider calls.
  - Hook failure semantics are explicit and testable.

## Capability Catalog

Source: `docs/harness/capability-catalog.md`

### HC-006: Budget, Hooks, and Side Effects

- Intent: Check spend and usage budgets, run before-call and after-call hooks,
  record spend, and execute permitted custom side effects.
- Public contract surface: `check_budget`, `record_usage`,
  `run_before_call_hooks`, `run_after_call_hooks`, and `run_redaction_hooks`
  operations.
- State ownership: Owns budget counters, usage records, hook outcomes, alert
  records, and redaction reports.
- Emitted events: `budget.checked`, `budget.exceeded`, `usage.recorded`,
  `hook.started`, `hook.completed`, and `hook.failed`.
- Failure behavior: Budget exhaustion and hook policy violations fail closed;
  non-critical hook failures are recorded and surfaced as degraded execution.
- Replacement boundary: A replacement must preserve budget accounting units,
  hook ordering, redaction-before-log behavior, and side-effect eligibility.
- Evaluator evidence: Fixtures for in-budget, over-budget, hook-success,
  hook-failure, redaction, and side-effect-denied cases.
- Trace evidence: Budget and hook spans with usage units, hook IDs, redaction
  status, and side-effect decision tags.

## Worker Contract

Source: `docs/harness/worker-contract.md`

- Worker contracts require function ID, capability ID, trigger name, input
  shape, output shape, recoverable errors, fail-closed errors, timeout,
  idempotency, state reads, state writes, emitted events, trace tags, version
  expectations, and fixture expectations.
- Input shape describes accepted fields, required fields, optional fields, and
  validation rules.
- Output shape includes enough status for neighboring capabilities to continue
  without implementation internals.
- Recoverable errors define code, meaning, caller action, and preserved state.
- Fail-closed errors stop before side effects, tool execution, credential
  exposure, or irreversible state mutation, and require event or trace evidence.
- Timeout behavior must state retry safety and whether partial state may exist.
- Idempotency prevents duplicated state writes, events, or side effects.
- State reads/writes must remain scoped to the capability boundary.
- Trace tags must not include secrets or raw business data unless explicitly
  approved by a future security requirement.
- Replacement comparison requires compatible input/output shapes, equivalent
  failure behavior, emitted event compatibility, state boundary compatibility,
  trace compatibility, and fixture compatibility.

## Neighboring Specs

Source: `docs/specs/spec-turn-intake-orchestration/SPEC.md`

- State transitions must be durable before side effects that depend on them.
- Tool/function execution must not occur before policy, credential, budget, and
  approval gates required by neighboring capabilities have passed.
- Failure behavior must distinguish budget failure from policy denial, approval
  rejection, provider/tool failure, timeout, interruption, and teardown failure.
- Events and traces must not include secret values, credentials, private keys,
  unsafe production data, or raw business data beyond approved trace metadata.

Source: `docs/specs/spec-provider-credential-model-capability/SPEC.md`

- Provider completion and streaming contracts can be specified first, with
  concrete adapters introduced by later implementation stories.
- Usage reporting can be contract-shaped here and consumed by the budget layer
  once the budget story is implemented.

## Wrapper-Only Content

- GitHub issue URLs, user avatar metadata, API node IDs, and timestamps are
  process metadata and are not part of the product contract.
