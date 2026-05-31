# STORY-018: Harness Training Evaluator

## Epic

EPIC-002

## Functional Requirements

- FR-022
- FR-013
- FR-014

## User Story

As a harness trainer, I want a deterministic evaluator for harness design and
implementation artifacts so that agents can iteratively improve the harness
without relying on subjective review alone.

## Implementation Plan

1. Define evaluator dimensions:
   - capability coverage
   - contract completeness
   - replacement safety
   - failure semantics
   - state boundaries
   - policy and approval safety
   - observability
   - traceability to PRD/Epic/Story
2. Define replacement safety checks:
   - contract compatibility
   - state-boundary compatibility
   - failure-mode equivalence
   - event compatibility
   - trace compatibility
   - regression fixture result
3. Implement a dependency-free evaluator script.
4. Add fixture documents for passing and failing harness designs.
5. Add fixture documents for accepted and rejected replacement candidates.
6. Add CI checks for evaluator execution.
7. Define a `harness_score` output and a replacement safety report for
   experiment tracking.

## Acceptance Criteria

- The evaluator runs locally without external dependencies.
- The evaluator produces a numeric score and missing coverage report.
- The evaluator fails CI when required harness capability coverage regresses.
- The evaluator reports replacement safety as a first-class result.
- The evaluator can reject a replacement candidate when contract, state,
  failure, event, trace, or fixture evidence is incompatible.
- The evaluator reads expectations from the capability catalog and worker
  contract artifacts before scoring implementation artifacts.
- The evaluator references
  `docs/specs/spec-replaceable-harness-capabilities/SPEC.md` as the governing
  specification.
