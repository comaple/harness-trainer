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
2. Define each catalog entry with these required fields:
   - capability ID
   - capability name
   - product area
   - owning FR IDs
   - owning Story IDs
   - intent
   - public contract surface
   - state ownership
   - emitted events
   - failure behavior
   - replacement boundary
   - evaluator evidence
   - trace evidence
3. Group capabilities into product areas:
   - turn runtime
   - provider and credentials
   - skills and prompt assembly
   - policy and approvals
   - budget and hooks
   - session and context
   - events and tracing
   - evaluation
4. Include at least one catalog row for each runtime FR from `FR-013` through
   `FR-022`.
5. Cross-reference each capability to its FR and Story.
6. Add a short validation checklist at the end of the catalog that reviewers can
   use before implementation begins.

## Acceptance Criteria

- The catalog covers all runtime FRs from `FR-013` through `FR-022`.
- Every catalog row has a public contract surface, state ownership statement,
  emitted event expectation, failure behavior, replacement boundary, evaluator
  evidence, and trace evidence.
- Every catalog row has at least one testable evidence item that can be used by
  the harness training evaluator.
- The catalog remains technology-neutral and does not select a runtime
  framework.
- The catalog references
  `docs/specs/spec-replaceable-harness-capabilities/SPEC.md` as the governing
  specification.
