# EPIC-002: Agent Harness Capabilities

## Goal

Decompose the target agent harness into replaceable, testable capabilities based
on the harness reference article.

## Functional Requirements

- FR-013
- FR-014
- FR-015
- FR-016
- FR-017
- FR-018
- FR-019
- FR-020
- FR-021
- FR-022

## Stories

- STORY-009: Build the harness capability catalog.
- STORY-010: Define the worker contract model.
- STORY-011: Plan turn intake and orchestration.
- STORY-012: Plan provider, credential, and model capability layer.
- STORY-013: Plan skill and prompt assembly.
- STORY-014: Plan policy and approval gates.
- STORY-015: Plan budget, hooks, and side effects.
- STORY-016: Plan session, memory, and context compaction.
- STORY-017: Plan events, streaming, and tracing.
- STORY-018: Plan the harness training evaluator.

## Acceptance Criteria

- Every harness runtime FR is represented by at least one Story.
- Every Story includes a concrete implementation plan.
- Each capability identifies its public contract, state boundary, failure
  behavior, and observability evidence.
- The decomposition does not require adopting any specific external harness
  framework.

