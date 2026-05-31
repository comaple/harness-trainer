# STORY-010: Worker Contract Model

## Epic

EPIC-002

## Functional Requirements

- FR-014
- FR-013

## User Story

As a harness developer, I want a standard worker contract model so that each
harness capability can be implemented, tested, and replaced independently.

## Implementation Plan

1. Define a contract schema in `docs/harness/worker-contract.md`.
2. Include required contract fields:
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
3. Define comparison semantics for two implementations of the same capability:
   - identical accepted input shape
   - compatible output shape
   - equivalent failure behavior
   - equivalent state boundary
   - equivalent event and trace evidence
   - compatible timeout and idempotency behavior
4. Add an example contract for a policy check capability.
5. Add an example contract for a model capability lookup.
6. Update the evaluator plan to score contract completeness and replacement
   safety.

## Acceptance Criteria

- The contract model is technology-neutral.
- The contract model supports both synchronous calls and event-triggered
  handlers.
- The contract model defines fail-closed behavior where applicable.
- The contract model distinguishes recoverable errors from fail-closed errors.
- The contract model defines how replacement candidates are compared without
  changing neighboring capabilities.
- The contract model references capability IDs from
  `docs/harness/capability-catalog.md`.
- The contract model references
  `docs/specs/spec-replaceable-harness-capabilities/SPEC.md` as the governing
  specification.
