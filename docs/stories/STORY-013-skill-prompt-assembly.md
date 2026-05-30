# STORY-013: Skill and Prompt Assembly

## Epic

EPIC-002

## Functional Requirements

- FR-017
- FR-014

## User Story

As a harness designer, I want skills and prompt assembly to be explicit
capabilities so that tool instructions and system prompts can evolve without
rewriting the turn runtime.

## Implementation Plan

1. Specify skill discovery and skill body retrieval.
2. Specify the per-function skill metadata required before tool calls.
3. Specify default prompt assembly from mode, identity, workspace, and skills.
4. Specify prompt override behavior.
5. Define validation checks for missing or malformed skill metadata.

## Acceptance Criteria

- Skills document request shape, errors, and usage notes.
- Prompt assembly is deterministic from declared inputs.
- Prompt override behavior preserves tool discovery when required.

