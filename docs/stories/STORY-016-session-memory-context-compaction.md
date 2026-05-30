# STORY-016: Session, Memory, and Context Compaction

## Epic

EPIC-002

## Functional Requirements

- FR-020
- FR-015
- FR-021

## User Story

As an agent operator, I want session state, memory, and context compaction to be
durable and branchable so that long-running agents can fork, resume, and stay
within context limits.

## Implementation Plan

1. Specify session tree records and parent links.
2. Specify per-session inbox or queue behavior.
3. Specify resume and fork behavior.
4. Specify compaction triggers based on context window thresholds.
5. Specify compaction output events and trace tags.

## Acceptance Criteria

- Sessions can be resumed from persisted state.
- Forked sessions preserve parent lineage.
- Compaction is triggered deterministically and emits evidence.

