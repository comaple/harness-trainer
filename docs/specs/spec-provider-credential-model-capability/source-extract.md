# Source Extract: Provider Credential and Model Capability

## Issue

Source: GitHub issue #48

- Create the BMad SPEC for `STORY-012 / FR-016` provider, credential, and model
  capability layer.
- Scope includes technology-neutral provider routing boundaries, credential
  lookup contracts, secret-handling boundaries, redacted handles, fail-closed
  behavior, model capability lookup, emitted events, trace evidence, stale or
  unknown model handling, and integration with turn orchestration and worker
  contracts.
- Acceptance requires credential lookup to avoid exposing secret values,
  missing/expired/unauthorized credentials to fail before provider calls, model
  capability lookup to reject unsupported features before model execution, and
  mapping to `HC-002`, `HC-003`, `FR-016`, `STORY-012`, and `EPIC-002`.

## PRD

Source: `docs/prd.md`

### FR-016: Provider, Credential, and Model Capability Layer

The harness runtime plan must include provider routing, credential resolution,
model capability lookup, streaming support, context window awareness, and usage
recording.

## Epic

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

- `EPIC-002` decomposes the target agent harness into replaceable, testable
  capabilities.
- `FR-016` is part of EPIC-002.
- `STORY-012` plans provider, credential, and model capability layer.
- Acceptance requires each capability to identify its public contract, state
  boundary, failure behavior, and observability evidence.
- Replacement-sensitive capabilities must identify evaluator evidence and
  replacement safety criteria before implementation begins.
- The decomposition must not require adopting any specific external harness
  framework.

## Story

Source: `docs/stories/STORY-012-provider-credential-model-layer.md`

- As a harness operator, model providers, credentials, and model capabilities
  must be isolated behind stable contracts so providers can be swapped without
  changing the turn orchestrator.
- Implementation plan:
  - Specify provider streaming and completion contracts.
  - Specify credential lookup contracts and secret handling boundaries.
  - Specify model capability lookup for tools, vision, streaming, and context
    window support.
  - Define usage reporting to the budget layer.
  - Define provider error normalization.
- Acceptance:
  - The turn orchestrator depends on provider contracts, not concrete
    providers.
  - Missing credentials fail before provider calls are made.
  - Model capability checks can reject unsupported run requests before
    execution.

## Capability Catalog

Source: `docs/harness/capability-catalog.md`

### HC-002: Provider Credential Resolution

- Intent: Resolve credentials and provider configuration needed for a model or
  tool call without leaking secrets into logs, prompts, or traces.
- Public contract surface: `resolve_provider_credentials` and
  `resolve_tool_credentials` accept a provider or tool key and return a
  redacted credential handle plus capability metadata.
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

- Intent: Report provider and model capabilities needed by the turn runtime,
  including streaming support, context-window limits, tool-call support, and
  usage accounting expectations.
- Public contract surface: `lookup_model_capabilities` keyed by model selector
  and provider context.
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

## Worker Contract

Source: `docs/harness/worker-contract.md`

### Model Capability Lookup

- Function ID: `model.lookup_capabilities`.
- Capability ID: `HC-003`.
- Trigger name: `lookup_model_capabilities`.
- Trigger style: synchronous call.
- Required input: `provider_key`, `model_key`, and `turn_id`.
- Optional input: `freshness_requirement` and `requested_features`.
- Validation: provider and model keys must be non-empty, and unknown providers
  are invalid.
- Success output includes provider key, model key, streaming support,
  tool-call support, context-window token limit or unknown marker,
  usage-accounting unit, and freshness.
- Non-terminal outcome `unsupported` means the caller must select another model
  or fail before execution.
- Recoverable error `MODEL_CAPABILITY_STALE` means capability data exists but
  does not meet freshness requirements.
- Fail-closed error `MODEL_UNSUPPORTED` forbids model execution for the current
  turn step and requires `model_capability.unsupported`.
- Fail-closed error `PROVIDER_UNKNOWN` forbids credential lookup and model
  execution and requires trace evidence without credentials.
- Timeout result is `MODEL_CAPABILITY_STALE` when cached data exists, otherwise
  `PROVIDER_UNKNOWN`.
- Idempotency key is `provider_key + model_key + freshness_requirement`.
- State reads include the model capability registry and cached capability
  records.
- State writes include cached capability records after successful refresh with
  provenance.
- Events include `model_capability.lookup_started`,
  `model_capability.resolved`, and `model_capability.unsupported`.
- Trace tags include `provider.key`, `model.key`, and `model.freshness`, with
  provider/model identifiers only and no credentials.
- Compatible change: Add optional capability fields callers can ignore.
- Breaking change: Remove required fields or change unsupported-model behavior.
- Fixtures cover streaming-supported model, non-streaming model,
  tool-call-supported model, unsupported model, unknown provider, stale
  capability data, and replacement comparison.

## Neighboring Spec

Source: `docs/specs/spec-turn-intake-orchestration/SPEC.md`

- Tool/function execution must not occur before policy, credential, budget, and
  approval gates required by neighboring capabilities have passed.
- Failure behavior must distinguish provider/tool failure from policy,
  approval, budget, timeout, interruption, and teardown failure.
- Events and traces must not include secret values, credentials, private keys,
  unsafe production data, or raw business data beyond approved trace metadata.
- Turn orchestration does not implement provider, credential, or model
  capability behavior; those neighboring capabilities own their own contracts.

## Wrapper-Only Content

- GitHub issue URLs, user avatar metadata, API node IDs, and timestamps are
  process metadata and are not part of the product contract.
