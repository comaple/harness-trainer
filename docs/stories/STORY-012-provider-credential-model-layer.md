# STORY-012: Provider, Credential, and Model Capability Layer

## Epic

EPIC-002

## Functional Requirements

- FR-016
- FR-019
- FR-021

## User Story

As a harness operator, I want model providers, credentials, and model
capabilities isolated behind stable contracts so that providers can be swapped
without changing the turn orchestrator.

## Implementation Plan

1. Specify provider streaming and completion contracts.
2. Specify credential lookup contracts and secret handling boundaries.
3. Specify model capability lookup for tools, vision, streaming, and context
   window support.
4. Define usage reporting to the budget layer.
5. Define provider error normalization.

## Acceptance Criteria

- The turn orchestrator depends on provider contracts, not concrete providers.
- Missing credentials fail before provider calls are made.
- Model capability checks can reject unsupported run requests before execution.

