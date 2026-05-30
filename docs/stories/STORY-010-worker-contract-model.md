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
2. Include fields for function ID, trigger name, input shape, output shape,
   errors, timeout, idempotency, state reads/writes, emitted events, and trace
   tags.
3. Add an example contract for a policy check capability.
4. Add an example contract for a model capability lookup.
5. Update the evaluator plan to score contract completeness.

## Acceptance Criteria

- The contract model is technology-neutral.
- The contract model supports both synchronous calls and event-triggered
  handlers.
- The contract model defines fail-closed behavior where applicable.

