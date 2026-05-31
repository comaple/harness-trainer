---
id: SPEC-skill-prompt-assembly
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #50. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Skill and Prompt Assembly

## Why

`harness-trainer` needs skill and prompt assembly as an explicit harness
capability so tool instructions, function metadata, system identity, workspace
context, and prompt overrides can evolve without rewriting turn orchestration.
Prompt construction must be deterministic, provenance-rich, and safe to compare
across replacement implementations.

## Capabilities

- id: CAP-1
  intent: The runtime can discover the skills applicable to a turn or tool
    call.
  success: Skill discovery returns skill IDs, source paths, required/optional
    status, selection reason, owning capability or function shape, and
    validation status from declared inputs.

- id: CAP-2
  intent: The runtime can load skill instructions and tool-use metadata before
    prompt assembly or tool execution.
  success: Skill loading returns instruction body references, request shape,
    error shape, usage notes, source provenance, and malformed/missing metadata
    diagnostics without hiding validation failures.

- id: CAP-3
  intent: Prompt assembly is deterministic from declared prompt inputs.
  success: The assembled prompt context is ordered from mode, identity,
    workspace context, discovered skills, loaded skill metadata, function-shape
    documentation, and approved overrides using stable ordering and precedence
    rules.

- id: CAP-4
  intent: Prompt override behavior is explicit and auditable.
  success: Overrides declare target section, precedence, scope, reason,
    allowed replacement or append behavior, and provenance; invalid override
    instructions fail closed, and required tool discovery is preserved when the
    story requires it.

- id: CAP-5
  intent: Missing required skills or malformed required metadata stop unsafe
    prompt or tool execution.
  success: Required-skill failures and malformed required metadata emit
    UI-safe diagnostics, preserve trace evidence, and fail closed before prompt
    assembly is treated as usable or before dependent tool calls execute.

- id: CAP-6
  intent: Replacement implementations can be compared without inspecting prompt
    builder internals.
  success: Replacement comparison fixtures prove identical skill selection,
    prompt ordering, override precedence, provenance output, emitted events,
    trace tags, and failure categories for the same declared inputs.

## Constraints

- The capability must be technology-neutral and must not require a specific
  prompt framework, model provider, tool runtime, skill storage backend, or
  templating engine.
- Prompt assembly must be deterministic from declared inputs; hidden ambient
  state must not change the assembled prompt.
- The turn orchestrator must depend on skill and prompt assembly contracts, not
  concrete prompt-builder implementations.
- Skill metadata required before tool calls must include request shape, error
  shape, and usage notes.
- Required skills and required metadata failures must fail closed; optional
  skill failures may be recorded without blocking only when the story declares
  them optional.
- Prompt overrides must not silently remove required tool discovery,
  function-shape documentation, safety constraints, or provenance.
- Prompt assembly state may own resolved skill list, prompt inputs, prompt
  provenance, and applied override metadata; it must not own secrets,
  credentials, or raw unsafe production data.
- Events and traces must not include secrets, private keys, raw credentials, or
  raw business data beyond approved prompt assembly metadata.
- The contract must align with `HC-004`, `FR-017`, `STORY-013`, and the worker
  contract model.

## Non-goals

- This SPEC does not implement a prompt renderer, skill registry, tool runtime,
  model provider, policy engine, event bus, or tracing backend.
- This SPEC does not choose a prompt template language, file format, framework,
  storage backend, or runtime SDK.
- This SPEC does not define business-domain prompts for a specific Agent.
- This SPEC does not authorize prompt overrides that bypass required tools,
  policy constraints, approvals, credential boundaries, or traceability.
- This SPEC does not replace turn orchestration, provider/model capability,
  policy approval, budget, session memory, event streaming, or evaluator
  capabilities.

## Success signal

A reviewer can inspect the skill and prompt assembly contract and determine how
skills are discovered, loaded, validated, ordered into prompt context, modified
by approved overrides, observed through events/traces, and compared across
replacement implementations without relying on a concrete prompt framework.

## Assumptions

- Skill bodies can initially be referenced by path or artifact ID rather than
  copied into every prompt assembly record.
- Prompt assembly can emit provenance for each assembled section before a
  concrete prompt renderer exists.
- Function-shape documentation can be represented as metadata until runtime
  tool schemas are implemented.

## Open Questions

- Should prompt assembly produce a machine-readable section graph in addition
  to human-readable prompt text?
- Should optional skill failure policy live in each business Agent Harness
  blueprint or in a shared harness-level policy file?
