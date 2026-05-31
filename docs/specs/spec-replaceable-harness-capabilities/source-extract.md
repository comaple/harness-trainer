# Source Extract

## GitHub Issue

- Issue: `#4`
- Title: `BR-002: Replaceable Harness Capabilities`
- URL: `https://github.com/comaple/harness-trainer/issues/4`
- State when read: `open`

Issue text:

> The product must help teams design and train harnesses as replaceable
> capabilities rather than as a monolithic agent framework.

Issue acceptance:

- Requirement is decomposed into Epic/Story work before implementation.
- Any implementation commit references this issue, `BR-002`, and the relevant
  Story ID.

## PRD Extract

Source: `docs/prd.md`

`BR-002: Replaceable Harness Capabilities`

> The product must help teams design and train harnesses as replaceable
> capabilities rather than as a monolithic agent framework.

Updated PRD clarification:

- A capability is replaceable only when its public contract, state ownership,
  failure semantics, events, and evaluator evidence are explicit enough that an
  alternative implementation can be compared without rewriting neighboring
  capabilities.
- `FR-013` requires the capability catalog to include contracts, state, events,
  failure behavior, replacement boundary, and evaluator evidence.
- `FR-014` requires the worker contract model to include function IDs, inputs,
  outputs, errors, timeouts, persisted state, emitted events, versioning
  expectations, and replaceability boundaries.
- `FR-022` requires the deterministic evaluator to score replacement safety.
- `NFR-004` requires replacement claims to be backed by contract
  compatibility, state-boundary clarity, failure-mode equivalence, and evaluator
  evidence.

## Epic Extract

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

`EPIC-002: Agent Harness Capabilities`

Goal:

> Decompose the target agent harness into replaceable, testable capabilities
> based on the harness reference article.

Covered functional requirements:

- `FR-013`: Harness Capability Catalog
- `FR-014`: Worker Contract Model
- `FR-015`: Turn Intake and Orchestration
- `FR-016`: Provider, Credential, and Model Capability Layer
- `FR-017`: Skill and Prompt Assembly
- `FR-018`: Policy and Approval Gates
- `FR-019`: Budget, Hooks, and Side Effects
- `FR-020`: Session, Memory, and Context Compaction
- `FR-021`: Events, Streaming, and Tracing
- `FR-022`: Harness Training Evaluator

Epic acceptance criteria:

- Every harness runtime FR is represented by at least one Story.
- Every Story includes a concrete implementation plan.
- Each capability identifies its public contract, state boundary, failure
  behavior, and observability evidence.
- The decomposition does not require adopting any specific external harness
  framework.

## Story Extract

Primary stories implementing the replaceability spine:

- `STORY-009`: Build the harness capability catalog.
- `STORY-010`: Define the worker contract model.
- `STORY-018`: Plan the harness training evaluator.

`STORY-009` requires each catalog row to record contract surface, persisted
state, emitted events, failure behavior, replacement boundary, FR linkage, Story
linkage, and testable evidence.

`STORY-010` requires the worker contract model to include function ID, trigger
name, input shape, output shape, errors, timeout, idempotency, state
reads/writes, emitted events, and trace tags.

## Preservation Notes

- The issue's core business requirement is preserved in `SPEC.md` Why and
  Success signal.
- The issue acceptance criteria are preserved in the constraints and
  assumptions.
- PRD details about public contract, state ownership, failure semantics, events,
  and evaluator evidence are preserved in `CAP-1` through `CAP-4`.
- Epic and Story decomposition claims are preserved as constraints,
  assumptions, and companion detail.

