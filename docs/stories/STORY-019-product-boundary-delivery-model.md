# STORY-019: Product Boundary and Delivery Model

## Epic

EPIC-003

## Functional Requirements

- FR-023
- FR-027

## User Story

As a project maintainer, I want the product boundary to state that
`harness-trainer` delivers enterprise business Agent Harnesses, not business
Agents or a generic Agent production platform, so that downstream planning stays
focused.

## Implementation Plan

1. Update README with product positioning, users, inputs, outputs, and
   non-goals.
2. Update PRD product section with the same boundary.
3. Update architecture with the delivery pipeline.
4. Keep Agent production platform and model training explicitly out of scope.

## Acceptance Criteria

- README states what the product delivers.
- README states what the product does not deliver.
- PRD distinguishes Agent Harness delivery from business Agent ownership.
- Architecture includes the delivery pipeline.

