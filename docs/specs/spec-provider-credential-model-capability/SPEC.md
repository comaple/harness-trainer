---
id: SPEC-provider-credential-model-capability
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #48. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Provider Credential and Model Capability

## Why

`harness-trainer` needs a provider, credential, and model capability layer so
business Agent Harnesses can route model work, resolve credentials, reject
unsupported requests, and record usage without binding turn orchestration to a
specific provider. Provider replacement must preserve credential safety,
capability semantics, error categories, and trace evidence.

## Capabilities

- id: CAP-1
  intent: The turn runtime can route provider work through a stable provider
    contract instead of concrete provider code.
  success: A provider request declares provider key, model key or selector,
    turn ID, requested features, streaming mode, context requirements, and
    usage-recording expectations before any provider call is made.

- id: CAP-2
  intent: The runtime can resolve model and tool credentials without exposing
    secret values.
  success: Credential lookup accepts provider or tool keys and returns only a
    redacted credential handle, capability metadata, lookup status, expiration
    metadata, and redacted diagnostics; no secret value appears in prompts,
    logs, events, traces, outputs, or persisted harness state.

- id: CAP-3
  intent: Missing, expired, or unauthorized credentials stop execution before
    provider or tool side effects.
  success: Credential failures emit `credential.denied` or
    `credential.expired`, preserve redacted trace evidence, and fail closed
    before model execution, tool execution, streaming startup, or usage
    recording.

- id: CAP-4
  intent: The runtime can determine whether a selected model can satisfy a
    turn step before execution.
  success: Model capability lookup resolves provider key, model key,
    streaming support, tool-call support, vision support, structured-output
    support, context-window tokens, usage-accounting unit, freshness, and
    provenance.

- id: CAP-5
  intent: Unsupported or stale model capability decisions are explicit and
    safe to evaluate.
  success: Unknown providers and unsupported models fail closed before
    credential lookup or model execution; stale capability data is marked with
    freshness metadata and is accepted, refreshed, or rejected according to the
    caller's freshness requirement.

- id: CAP-6
  intent: Provider outcomes can be compared and replaced without changing turn
    orchestration.
  success: Provider completion, streaming, capability lookup, credential
    lookup, and provider error normalization emit compatible events, trace
    tags, failure categories, and usage fields across provider replacements.

## Constraints

- The layer must be technology-neutral and must not require a specific model
  provider, SDK, secrets manager, database, queue, or tracing backend.
- The turn orchestrator must depend on provider, credential, and model
  capability contracts, not concrete provider implementations.
- Credential resolution must not own or persist secret values; it may own only
  redacted handles, lookup status, expiration metadata, and authorization
  evidence.
- Credential lookup must precede provider calls, model streaming, tool calls,
  and side effects that need those credentials.
- Model capability lookup must precede model execution when requested features,
  streaming, tool calls, vision, structured output, context window, or usage
  accounting affect the run.
- Unknown providers, missing credentials, expired credentials, unauthorized
  credentials, unsupported models, and unsupported requested features must fail
  closed with UI-safe diagnostics.
- Stale capability records must be visibly marked and must not silently satisfy
  a stricter freshness requirement.
- Events and traces must not include secret values, private keys, raw
  credential material, or unsafe production data.
- The contract must align with `HC-002`, `HC-003`, `FR-016`, `STORY-012`, and
  the worker contract model.

## Non-goals

- This SPEC does not implement a provider adapter, secrets manager, model
  registry, budget system, policy engine, event bus, or tracing backend.
- This SPEC does not choose any concrete model provider, credential storage
  product, SDK, database, queue, or cache.
- This SPEC does not define business-domain behavior for a specific Agent.
- This SPEC does not grant access to production credentials or authorize
  unsafe tool calls.
- This SPEC does not replace the turn orchestration, budget, policy, session,
  memory, event streaming, or evaluator capabilities.

## Success signal

A reviewer can inspect the provider, credential, and model capability contract
and determine how a run resolves redacted credentials, checks model
capabilities, rejects unsupported requests before execution, normalizes
provider errors, emits safe lifecycle evidence, and preserves replacement
compatibility without relying on a concrete provider implementation.

## Assumptions

- Provider completion and streaming contracts can be specified first, with
  concrete adapters introduced by later implementation stories.
- Usage reporting can be contract-shaped here and consumed by the budget layer
  once the budget story is implemented.
- A redacted credential handle is sufficient for downstream contracts; secret
  retrieval remains outside this repository's persisted artifacts.

## Open Questions

- Should provider completion and streaming contracts become separate machine
  readable templates, or remain part of a single provider contract template?
- Which stale capability cases should be recoverable by refresh, and which
  should fail closed until an operator updates the registry?
