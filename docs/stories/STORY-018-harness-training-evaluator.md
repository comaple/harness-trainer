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
   - failure semantics
   - state boundaries
   - policy and approval safety
   - observability
   - traceability to PRD/Epic/Story
2. Implement a dependency-free evaluator script.
3. Add fixture documents for passing and failing harness designs.
4. Add CI checks for evaluator execution.
5. Define a `harness_score` output for experiment tracking.

## Acceptance Criteria

- The evaluator runs locally without external dependencies.
- The evaluator produces a numeric score and missing coverage report.
- The evaluator fails CI when required harness capability coverage regresses.

