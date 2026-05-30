# STORY-011: Turn Intake and Orchestration

## Epic

EPIC-002

## Functional Requirements

- FR-015
- FR-021
- FR-020

## User Story

As an agent operator, I want each user turn to be accepted, persisted, executed,
and completed through a durable state machine so that interrupted runs can be
debugged or resumed.

## Implementation Plan

1. Specify the turn request schema.
2. Specify the turn state record and terminal states.
3. Define state transitions for provisioning, assistant streaming, function
   execution, approval waiting, steering, teardown, stopped, and failed.
4. Define emitted lifecycle events for each state.
5. Define how state transition errors become visible to the UI and trace.

## Acceptance Criteria

- The state machine has explicit terminal states.
- Each state declares entry conditions, output events, and failure behavior.
- Teardown behavior is specified for both success and failure.

