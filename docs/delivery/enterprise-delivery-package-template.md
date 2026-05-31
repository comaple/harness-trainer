# Enterprise Delivery Package Template

Use this template for one target business Agent Harness. Keep source artifacts
as the source of truth and record references plus review evidence here. Do not
store secret values, tokens, passwords, private keys, or credential material.

## Delivery Metadata

| Field | Value |
| --- | --- |
| Target business Agent | |
| Delivery package owner | |
| Business owner | |
| Product owner / analyst | |
| Harness architect | |
| Implementation lead | |
| Reviewer | |
| Business context intake reference | |
| Business environment inventory reference | |
| Business Agent Harness Blueprint reference | |
| Business evaluation mapping reference | |
| Spec reference | `docs/specs/spec-enterprise-delivery-package/SPEC.md` |
| Last updated | |
| Status | draft / under review / ready for handoff / blocked |

## Source Inputs

| Source ID | Source artifact | Required for handoff? | Provides | Status | Evidence reference |
| --- | --- | --- | --- | --- | --- |
| SRC-001 | Business PRD | yes | business goals, workflows, acceptance criteria, non-goals | draft | |
| SRC-002 | Business context intake | yes | stakeholders, success metrics, risks, assumptions | draft | |
| SRC-003 | Business environment inventory | yes | tools, APIs, databases, permissions, approvals, observability | draft | |
| SRC-004 | Business Agent Harness Blueprint | yes | harness architecture, policies, contracts, evaluation expectations | draft | |
| SRC-005 | Worker contracts | yes | tool, skill, policy, approval, budget, session, event, and tracing behavior | draft | |
| SRC-006 | Implementation stories and issues | yes | planned implementation slices and code-agent work packages | draft | |
| SRC-007 | Business evaluation mapping | yes | evaluator checks, fixtures, failure classes, run evidence | draft | |
| SRC-008 | CI and review records | yes | quality gate, code review, merge, and release evidence | draft | |

## PRD Traceability

| Business goal or acceptance criterion | PRD reference | FR ID | Story ID | Issue or PR | Harness capability | Contract or spec | Evaluator check | Run evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BG-001 / AC-001 | | FR-XXX | STORY-XXX | #000 | `tools` / `knowledge` / `policy` / `approval` / `budget` / `session` / `events` / `tracing` / `evaluation` | | CHECK-001 | RUN-001 | draft |

## Architecture Evidence

| Architecture decision | Source reference | Harness component | Business rationale | Risk or constraint addressed | Review evidence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| ARCH-001 | | turn orchestration / worker contract / policy / approval / budget / session / event / tracing / evaluator | | | | draft |

## Worker Contract Evidence

| Worker contract | Capability area | Input boundary | Output boundary | Error behavior | Timeout behavior | Persisted state | Events or traces | Policy boundary | Test evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONTRACT-001 | `tools` | | | | | | | | | draft |

## Implementation Plan Evidence

| Implementation item | Issue/story/spec | Allowed edit surface | Owner | Validation command | Review evidence | Delivery status |
| --- | --- | --- | --- | --- | --- | --- |
| IMPL-001 | #000 / STORY-XXX / SPEC | | | | | planned / implemented / reviewed / blocked |

## Environment Integration Plan

| Environment item | Inventory reference | Access method | Access boundary | Secret handling | Sandbox or mock strategy | Observability evidence | Approval evidence | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-001 | ENV-TOOL-001 / ENV-DATA-001 | | | no secret values stored here | fixture / mock / sandbox / manual evidence | | | | draft |

## Evaluator Plan Evidence

| Evaluator check | Business criterion | Fixture or scenario | Expected pass signal | Failure class | Validation command | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CHECK-001 | CRIT-001 | FIXTURE-001 | | incorrect tool use / missing approval / policy violation / unsupported data access / budget overrun / poor task outcome / crash | | | draft |

## CI Evidence

| CI record | Branch or commit | Command or workflow | Result | Evidence link or log reference | Reviewer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| CI-001 | | `python3 scripts/ci_check.py` | pass / fail / skipped | | | draft |

## Run Evidence

| Run ID | Evaluator check | Validation command | Observed output | Event evidence | Trace evidence | Score or pass signal | Failure class | Keep/discard/crash decision | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RUN-001 | CHECK-001 | | | | | pass / fail / crash | keep / discard / crash / manual review | draft |

## Operational Handoff

| Handoff item | Owner | Runtime or support boundary | Runbook or procedure | Monitoring or audit evidence | Rollback or recovery expectation | Status |
| --- | --- | --- | --- | --- | --- | --- |
| HANDOFF-001 | | | | | | draft |

## Open Risks and Decisions

| Item ID | Type | Description | Affected artifact | Blocks handoff? | Owner | Decision or mitigation | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RISK-001 | risk / assumption / open question / missing evidence | | | yes / no | | | open |

## Delivery Readiness

| Check | Status | Evidence |
| --- | --- | --- |
| Required source inputs are linked and reviewed. | draft | |
| PRD traceability connects business goals or acceptance criteria to FR, story, issue, contract, evaluator check, and run evidence. | draft | |
| Architecture decisions and worker contracts are reviewable. | draft | |
| Implementation plan evidence includes allowed edit surface, validation command, and review evidence. | draft | |
| Environment integration plan records access method, access boundary, secret handling, approval evidence, and observability evidence. | draft | |
| Evaluator plan covers business criteria or records explicit open gaps. | draft | |
| CI evidence includes command or workflow, commit or branch, result, and evidence reference. | draft | |
| Run evidence includes validation command, observed output, event evidence, trace evidence, score or pass signal, failure class, and keep/discard/crash decision. | draft | |
| Operational handoff identifies owner, support boundary, runbook, monitoring or audit evidence, and rollback or recovery expectation. | draft | |
| Assumptions, open questions, missing evidence, and handoff blockers are separated from confirmed facts. | draft | |
| Package can be audited from business goal to run evidence without relying on chat history. | draft | |
