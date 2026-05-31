# STORY-026: Code Agent Execution Package

## Epic

EPIC-003

## Functional Requirements

- FR-029
- FR-005

## User Story

As a harness delivery lead, I want a bounded execution package for programmers
and code agents so that implementation work stays tied to approved business
intent, stories, specs, contracts, evaluator expectations, and review evidence.

## Implementation Plan

1. Define the required fields for a code agent execution package:
   - issue reference
   - `FR-XXX` requirement ID
   - `STORY-XXX` story ID
   - spec or worker contract context
   - evaluator and CI commands
   - allowed edit surface
   - acceptance evidence required for review
2. Define how the package is created from business context, environment
   inventory, blueprint, and worker contracts.
3. Define how code agents report implementation evidence, test evidence, and
   evaluator output.
4. Define review outcomes: keep, revise, discard, retry, or handoff.

## Acceptance Criteria

- Execution packages identify the exact issue, FR, Story, spec or contract,
  and evaluator expectation for a code agent task.
- Execution packages constrain allowed edits and required evidence before
  review.
- Code-agent-assisted work remains auditable from business intent to delivery
  evidence.
