# Business Agent Harness Blueprint Template

Use this template for one target business Agent. The blueprint consumes the
business context intake and business environment inventory for the same target
Agent. Keep confirmed facts separate from assumptions, open questions, risks,
and missing dependencies.

## Blueprint Metadata

| Field | Value |
| --- | --- |
| Target business Agent | |
| Blueprint owner | |
| Business owner | |
| Harness architect | |
| Business context intake reference | |
| Business environment inventory reference | |
| Last updated | |
| Status | draft / under review / confirmed / blocked |

## Source Inputs

| Source ID | Source artifact | Required for blueprint? | Status | Notes |
| --- | --- | --- | --- | --- |
| SRC-001 | Business context intake | yes | draft | |
| SRC-002 | Business environment inventory | yes | draft | |

## Agent Purpose

| Field | Value |
| --- | --- |
| Agent purpose | |
| Primary users | |
| Business goal references | |
| Success metric references | |
| Acceptance criteria references | |
| Out-of-scope responsibilities | |

## User Tasks

| Task ID | User task | Business goal | Workflow reference | Acceptance criteria | In scope? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| TASK-001 | | | | | yes / no | |

## Business Goal to Harness Capability Mapping

Allowed harness capability areas:

- `tools`
- `knowledge`
- `policy`
- `approval`
- `budget`
- `session`
- `events`
- `tracing`
- `evaluation`

| Business goal or requirement | Harness capability | Blueprint decision | Evidence source | Status |
| --- | --- | --- | --- | --- |
| | `tools` | | | draft |

## Tools and Worker Contract Candidates

| Environment item | Tool or API role | Worker contract candidate | Function ID candidate | Input boundary | Output boundary | Failure behavior | Test strategy | Policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-TOOL-001 | | | | | | | | | draft |

## Knowledge Access

| Knowledge source | Harness capability | Access boundary | Refresh expectation | Retrieval rule | Trace evidence | Evaluator expectation | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | `knowledge` | | | | | | draft |

## Policy Rules

| Policy rule | Trigger | Applies to | Business rationale | Owner | Enforcement point | Review evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| POLICY-001 | | | | | | | draft |

## Approval Flow

| Approval ID | Trigger | Approver | Request payload | Decision evidence | Timeout or fallback | Related policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APPROVAL-001 | | | | | | | draft |

## Budget Constraints

| Budget item | Scope | Limit | Owner | Enforcement point | Event or trace evidence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| BUDGET-001 | | | | | | draft |

## Session and Memory Rules

| Rule ID | Session or memory rule | Applies to | Persistence boundary | Compaction expectation | Privacy constraint | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SESSION-001 | | | | | | draft |

## Events and Tracing

| Event or trace ID | Event | Producer | Consumer | Required fields | Retention or audit need | Evaluator expectation | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EVENT-001 | | | | | | | draft |

## Evaluation Expectations

| Evaluator ID | Business metric or acceptance criteria | Harness behavior under test | Fixture or scenario | Pass signal | Keep/discard evidence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| EVAL-001 | | | | | | draft |

## Risks and Missing Dependencies

| Risk ID | Risk or missing dependency | Affected capability | Blocks implementation story? | Owner | Mitigation or decision needed | Status |
| --- | --- | --- | --- | --- | --- | --- |
| RISK-001 | | | yes / no | | | open |

## Implementation Story Slices

| Slice ID | Implementation story candidate | Business goal | Harness capability | Worker contract | Policy rule | Evaluator expectation | Validation command | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SLICE-001 | | | `tools` | | | | | draft |

## Code-Agent Work Package Boundaries

| Work package | Issue/story/spec reference | Allowed edit surface | Required contract | Required evaluator | Validation command | Review evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WORK-001 | | | | | | | draft |

## Blueprint Readiness

| Check | Status | Evidence |
| --- | --- | --- |
| Agent purpose is confirmed. | draft | |
| User task scope is confirmed. | draft | |
| Business goals map to harness capability areas. | draft | |
| Environment items map to worker contract candidates or policy rules. | draft | |
| Policy, approval, budget, session, events, tracing, and evaluator needs are identified. | draft | |
| Risks and missing dependencies identify whether they block implementation story creation. | draft | |
| Implementation story slices are bounded by issue/story/spec, contract, evaluator, allowed edit surface, and validation command. | draft | |
| Code-agent work packages cannot redefine business goals, environment access boundaries, policy decisions, or acceptance criteria. | draft | |
| Blueprint can be consumed by downstream stories without relying on chat history. | draft | |
