# Code Agent Execution Package Template

Use this template for one bounded implementation task. Fill the intake and
boundary sections before a programmer or code agent edits files. Fill the
evidence and review sections before the change is kept, revised, discarded,
retried, or handed off.

Do not store secret values, tokens, passwords, private keys, or unsafe
production data in this package.

## Package Metadata

| Field | Value |
| --- | --- |
| Package ID | WORK-001 |
| Target business Agent Harness | |
| Package owner | |
| Implementer | programmer / code agent / pair |
| Reviewer | |
| Issue reference | #000 |
| Epic ID | EPIC-XXX |
| FR ID | FR-XXX |
| Story ID | STORY-XXX |
| Source spec reference | |
| Worker contract reference | |
| Blueprint slice reference | |
| Evaluation mapping reference | |
| Enterprise delivery package reference | |
| Last updated | |
| Status | draft / ready for implementation / implemented / under review / accepted / blocked |

## Source Context

| Source ID | Source artifact | Required for task? | Provides | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001 | Business PRD or requirement | yes | business intent, non-goals, acceptance criteria | draft | |
| SRC-002 | Story | yes | implementation plan and acceptance criteria | draft | |
| SRC-003 | Spec | yes | canonical downstream contract | draft | |
| SRC-004 | Worker contract | if applicable | input boundary, output boundary, error behavior, policy boundary | draft | |
| SRC-005 | Blueprint slice | if applicable | allowed implementation slice and harness capability | draft | |
| SRC-006 | Evaluation mapping | yes | evaluator check, fixture, failure class, run evidence | draft | |
| SRC-007 | Enterprise delivery package | if applicable | final handoff evidence link | draft | |

## Work Scope

| Field | Value |
| --- | --- |
| Implementation objective | |
| In-scope behavior | |
| Out-of-scope behavior | |
| Acceptance evidence required before review | |
| Owner approval required for scope change? | yes |

## Allowed Edit Surface

| Surface ID | Allowed file, directory, or artifact | Change type | Rationale | Guardrail |
| --- | --- | --- | --- | --- |
| SURFACE-001 | | create / update / delete | | |

## Disallowed Changes

| Disallowed item | Why blocked | Approval required to change |
| --- | --- | --- |
| Business goals or PRD scope | Owned by business/product owner | business owner and product owner |
| Acceptance criteria | Owned by PRD/story/spec | product owner and reviewer |
| Environment access boundary | Owned by platform/security owner | platform/security owner |
| Policy or approval decision | Owned by harness architect/reviewer | harness architect and reviewer |
| Budget limit | Owned by delivery/platform owner | delivery lead |
| Evaluator criteria or pass signal | Owned by evaluator owner/reviewer | evaluator owner and reviewer |
| Delivery readiness decision | Owned by delivery reviewer | delivery reviewer |

## Required Commands and Gates

| Command ID | Command or workflow | Purpose | Required before review? | Expected pass signal | Evidence location |
| --- | --- | --- | --- | --- | --- |
| CMD-001 | `python3 scripts/ci_check.py` | local repository quality gate | yes | CI gate passed | |
| CMD-002 | | evaluator or test command | yes / no | pass / score / review evidence | |

## Evaluator Expectations

| Evaluator check | Fixture or scenario | Business criterion | Expected output or event | Failure class | Validation command | Status |
| --- | --- | --- | --- | --- | --- | --- |
| CHECK-001 | FIXTURE-001 | CRIT-001 | | incorrect tool use / missing approval / policy violation / unsupported data access / budget overrun / poor task outcome / crash | | draft |

## Implementation Evidence

| Evidence item | Value |
| --- | --- |
| Changed artifacts | |
| Implementation summary | |
| Linked commit or PR | |
| Assumptions made | none / listed below |
| Deviations from package | none / listed below |
| Open risks | none / listed below |

## Test and CI Evidence

| Evidence ID | Command or workflow | Result | Output summary | Evidence link or log reference | Status |
| --- | --- | --- | --- | --- | --- |
| TEST-001 | `python3 scripts/ci_check.py` | pass / fail / skipped | | | draft |

## Evaluator Output and Run Evidence

| Run ID | Evaluator check | Validation command | Observed output | Event evidence | Trace evidence | Score or pass signal | Failure class | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RUN-001 | CHECK-001 | | | | | pass / fail / crash | | draft |

## Assumptions, Deviations, and Open Risks

| Item ID | Type | Description | Impact | Owner | Blocks review? | Status |
| --- | --- | --- | --- | --- | --- | --- |
| OPEN-001 | assumption / deviation / open risk / missing evidence | | | | yes / no | open |

## Review Decision

| Field | Value |
| --- | --- |
| Reviewer | |
| Decision | keep / revise / discard / retry / handoff |
| Decision rationale | |
| Evidence used | |
| Required follow-up | none / listed |
| Enterprise delivery package update required? | yes / no |
| Final status | accepted / needs revision / discarded / retry planned / handed off |

## Package Readiness

| Check | Status | Evidence |
| --- | --- | --- |
| Package identifies issue, epic, FR, Story, owner, implementer, and reviewer. | draft | |
| Package references the source spec or worker contract required for implementation. | draft | |
| Package identifies evaluator expectation, fixture or scenario, validation command, and expected pass signal. | draft | |
| Allowed edit surface is explicit. | draft | |
| Disallowed changes protect business goals, PRD scope, access boundaries, policy, approval, budget, evaluator criteria, and delivery readiness. | draft | |
| Required CI and evaluator commands are listed before implementation starts. | draft | |
| Implementation evidence records changed artifacts, summary, linked commit or PR, assumptions, deviations, and open risks. | draft | |
| Test evidence and evaluator output are recorded before review. | draft | |
| Review decision records keep, revise, discard, retry, or handoff with rationale and evidence. | draft | |
| Package can be audited from business intent to delivery evidence without relying on chat history. | draft | |
