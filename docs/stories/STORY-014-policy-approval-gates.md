# STORY-014: Policy and Approval Gates

## Epic

EPIC-002

## Functional Requirements

- FR-018
- FR-014
- FR-021

## User Story

As a maintainer, I want every tool call to pass through policy and approval
gates so that unsafe or human-sensitive actions are denied, paused, or resumed
with an audit trail.

## Implementation Plan

1. Specify the policy check contract and timeout.
2. Specify `allow`, `deny`, and `needs_approval` outcomes.
3. Specify fail-closed behavior when policy is unavailable.
4. Specify approval resolution inputs and persisted decision state.
5. Specify lifecycle events and trace tags for policy and approval decisions.

## Acceptance Criteria

- Policy timeout produces a denial outcome.
- Approval decisions can be resumed without changing the original tool contract.
- Every approval decision has a reason, actor, and traceable event.

