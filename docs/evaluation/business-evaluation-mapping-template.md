# Business Evaluation Mapping Template

Use this template for one target business Agent. The mapping consumes business
context intake, business environment inventory, the Business Agent Harness
Blueprint, relevant worker contracts, and `SPEC-business-evaluation-mapping`.
Keep confirmed business criteria separate from assumptions, open gaps, manual
review needs, and implementation decisions.

## Evaluation Mapping Metadata

| Field | Value |
| --- | --- |
| Target business Agent | |
| Evaluation mapping owner | |
| Business owner | |
| Harness architect | |
| Evaluator owner | |
| Business context intake reference | |
| Business environment inventory reference | |
| Business Agent Harness Blueprint reference | |
| Spec reference | `docs/specs/spec-business-evaluation-mapping/SPEC.md` |
| Last updated | |
| Status | draft / under review / confirmed / blocked |

## Source Inputs

| Source ID | Source artifact | Required for mapping? | Criteria provided | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001 | Business PRD | yes | business success criterion / acceptance criterion | draft | |
| SRC-002 | Business context intake | yes | success metrics / acceptance criteria | draft | |
| SRC-003 | Business environment inventory | yes | fixture, sandbox, access, and observability constraints | draft | |
| SRC-004 | Business Agent Harness Blueprint | yes | evaluator expectations and implementation slices | draft | |
| SRC-005 | Worker contract | if applicable | contract behavior, errors, events, traces | draft | |
| SRC-006 | Story or code-agent work package | if applicable | validation command and acceptance evidence | draft | |

## Business Criteria Coverage

| Criterion ID | Criterion type | Business success criterion or acceptance criterion | Source reference | Harness behavior under test | Evaluation mode | Coverage status | Owner decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CRIT-001 | business success criterion / acceptance criterion | | | | deterministic check / review evidence / open gap | draft | |

## Evaluator Checks

| Evaluator check ID | Criterion ID | Deterministic check | Input fixture or scenario | Expected output or event | Pass signal | Failure signal | Validation command | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CHECK-001 | CRIT-001 | | FIXTURE-001 | | | | | draft |

## Regression Fixtures and Scenarios

| Fixture ID | Scenario | Business workflow | Environment dependency | Fixture, mock, sandbox, or manual evidence | Data boundary | Setup command | Reset expectation | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FIXTURE-001 | | | | fixture / mock / sandbox / review evidence | no production secrets | | | draft |

## Failure Classification

| Failure class | Applies to criterion or check | Detection signal | Required evidence | Decision impact | Notes |
| --- | --- | --- | --- | --- | --- |
| incorrect tool use | | | run evidence, event, trace, or reviewer note | discard / manual review | |
| missing approval | | | approval request and decision evidence | discard / crash | |
| policy violation | | | policy rule, event, and trace evidence | discard / crash | |
| unsupported data access | | | access boundary and audit evidence | discard / crash | |
| budget overrun | | | budget event, spend record, or token evidence | discard / manual review | |
| poor task outcome | | | business outcome evidence and acceptance criterion | discard / manual review | |
| crash | | | error, timeout, infrastructure, or evaluator failure evidence | crash | |

## Run Evidence

| Run ID | Evaluator check ID | Validation command | Fixture or scenario | Observed output | Event evidence | Trace evidence | Score or pass signal | Failure class | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RUN-001 | CHECK-001 | | FIXTURE-001 | | | | pass / fail / crash | | draft |

## Keep, Discard, and Crash Decision Evidence

| Decision ID | Change or run reference | Decision | Business criterion impact | Evidence summary | Reviewer | Follow-up action | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DECISION-001 | RUN-001 | keep / discard / crash | | | | | draft |

## Open Gaps and Manual Review

| Gap ID | Criterion or check | Gap type | Why deterministic check is unavailable | Manual review evidence | Owner | Blocks implementation review? | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GAP-001 | CRIT-001 | missing fixture / manual-only criterion / unclear source | | review evidence | | yes / no | open |

## Code-Agent Work Package Links

| Work package | Issue/story/spec reference | Required evaluator check | Fixture or scenario | Validation command | Required review evidence | Allowed edit surface | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WORK-001 | | CHECK-001 | FIXTURE-001 | | | | draft |

## Mapping Readiness

| Check | Status | Evidence |
| --- | --- | --- |
| Every business success criterion has evaluator coverage or an explicit open gap. | draft | |
| Every acceptance criterion maps to deterministic check, review evidence, or open gap. | draft | |
| Regression fixtures or scenarios are defined for key workflows. | draft | |
| Environment-dependent checks avoid production secrets and unsafe production access. | draft | |
| Failure classes include incorrect tool use, missing approval, policy violation, unsupported data access, budget overrun, poor task outcome, and crash. | draft | |
| Run evidence records validation command, fixture or scenario, pass signal, failure class, event evidence, and trace evidence. | draft | |
| Keep, discard, and crash decisions are evidence-based. | draft | |
| Code-agent work packages cite issue/story/spec, evaluator check, validation command, allowed edit surface, and review evidence. | draft | |
| Mapping can be consumed by downstream stories without relying on chat history. | draft | |
