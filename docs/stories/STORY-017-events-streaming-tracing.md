# STORY-017: Events, Streaming, and Tracing

## Epic

EPIC-002

## Functional Requirements

- FR-021
- FR-015

## User Story

As a reviewer, I want token streams, UI events, and traces to share run,
session, message, and function identifiers so that a full turn can be debugged
across capabilities.

## Implementation Plan

1. Specify event names for turn lifecycle, message updates, tool calls,
   approvals, budget decisions, compaction, and completion.
2. Specify event payload requirements.
3. Specify trace identifiers and required span attributes.
4. Specify streaming behavior for assistant output.
5. Define event replay expectations for debugging.

## Acceptance Criteria

- Every runtime capability emits or forwards trace context.
- UI-visible events can be correlated to trace spans.
- Failed turns emit enough information to diagnose the failing capability.

