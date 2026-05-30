# STORY-009: Harness Capability Catalog

## Epic

EPIC-002

## Functional Requirements

- FR-013
- FR-014

## User Story

As a harness architect, I want a catalog of harness capabilities so that runtime
work can be planned as replaceable parts instead of as one monolithic framework.

## Implementation Plan

1. Create a capability catalog under `docs/harness/capability-catalog.md`.
2. Group capabilities into product areas:
   - turn runtime
   - provider and credentials
   - skills and prompt assembly
   - policy and approvals
   - budget and hooks
   - session and context
   - events and tracing
   - evaluation
3. For each capability, record:
   - contract surface
   - persisted state
   - emitted events
   - failure behavior
   - replacement boundary
4. Cross-reference each capability to its FR and Story.

## Acceptance Criteria

- The catalog covers all runtime FRs from `FR-013` through `FR-022`.
- Every catalog row has a replacement boundary.
- Every catalog row has at least one testable evidence item.

