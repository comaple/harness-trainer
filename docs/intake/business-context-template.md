# Business Context Intake Template

Use this template to capture the business context for one target business Agent
before creating a Harness Blueprint, worker contracts, evaluator checks, or
code-agent execution packages.

## Intake Metadata

| Field | Value |
| --- | --- |
| Target business Agent name | TBD |
| Business owner | TBD |
| Product owner / analyst | TBD |
| Harness delivery lead | TBD |
| Intake status | draft / ready-for-review / approved |
| Source business PRD | link or repository path |
| Last updated | YYYY-MM-DD |

## Business Goals

List each confirmed business goal. Use one row per goal.

| Goal ID | Goal | Business outcome | Owner | Status |
| --- | --- | --- | --- | --- |
| BG-001 | TBD | TBD | TBD | confirmed / assumption / open question |

## Business PRD

Summarize or link the business PRD that owns the target Agent's business
purpose. If the PRD is external, record the approved source and reviewer.

| Field | Value |
| --- | --- |
| PRD source | TBD |
| PRD owner | TBD |
| Approved scope summary | TBD |
| Explicit non-goals | TBD |
| Business owner confirmation | pending / confirmed |

## Stakeholders and Roles

Capture the users, operators, approvers, reviewers, and support roles involved
in the target business Agent workflow.

| Role ID | Role | Responsibility | Decision rights | Notes |
| --- | --- | --- | --- | --- |
| ROLE-001 | TBD | TBD | TBD | TBD |

## Business Workflows

Describe each workflow that the target business Agent must support.

| Workflow ID | Trigger | Actor | Desired outcome | Critical steps | Failure impact |
| --- | --- | --- | --- | --- | --- |
| WF-001 | TBD | TBD | TBD | TBD | TBD |

## Constraints

Record business, legal, operational, compliance, schedule, and budget
constraints that bend design decisions.

| Constraint ID | Constraint | Applies to | Confirmation status |
| --- | --- | --- | --- |
| CON-001 | TBD | TBD | confirmed / assumption / open question |

## Risks

Record risks that the harness must manage through policy, approval,
observability, evaluator checks, or operational handoff.

| Risk ID | Risk | Impact | Mitigation expectation | Owner |
| --- | --- | --- | --- | --- |
| RISK-001 | TBD | TBD | TBD | TBD |

## Success Metrics

Record business success metrics in a form that can later map to evaluator
checks, regression fixtures, or run evidence.

| Metric ID | Metric | Target | Measurement source | Evaluation note |
| --- | --- | --- | --- | --- |
| MET-001 | TBD | TBD | TBD | TBD |

## Acceptance Criteria

Record acceptance criteria that business owners or reviewers can use to decide
whether the target Agent Harness is ready for delivery.

| AC ID | Acceptance criterion | Evidence required | Owner |
| --- | --- | --- | --- |
| AC-001 | TBD | TBD | TBD |

## Assumptions Requiring Business Owner Confirmation

Use this section for claims that cannot be treated as confirmed business facts
until the business owner or product owner approves them.

| Assumption ID | Assumption | Risk if wrong | Confirmation owner | Status |
| --- | --- | --- | --- | --- |
| ASM-001 | TBD | TBD | TBD | pending / confirmed / rejected |

## Open Questions

Use this section for gaps that block or warn downstream blueprint work.

| Question ID | Question | Blocks blueprint? | Owner | Due |
| --- | --- | --- | --- | --- |
| OQ-001 | TBD | yes / no | TBD | TBD |

## Harness Capability Mapping

Map accepted business requirements to harness capability areas. Use the area
names exactly so downstream specs, stories, and evaluators can reference them.

Allowed harness areas:

- `tools`
- `knowledge`
- `policy`
- `approval`
- `budget`
- `session`
- `events`
- `tracing`
- `evaluation`

| Requirement ID | Business source | Harness areas | Mapping rationale |
| --- | --- | --- | --- |
| BRQ-001 | BG-001 / WF-001 / AC-001 | `policy`, `approval`, `evaluation` | TBD |

## Blueprint Readiness

Use this checklist before creating or updating a Business Agent Harness
Blueprint.

- [ ] Business goals are confirmed or explicitly marked as assumptions.
- [ ] Business PRD source is recorded.
- [ ] Workflows and roles are captured.
- [ ] Constraints, risks, success metrics, and acceptance criteria are recorded.
- [ ] Assumptions needing business owner confirmation are separated from facts.
- [ ] Open questions identify whether they block blueprint work.
- [ ] Accepted business requirements map to harness capability areas.
- [ ] Intake reviewer has approved downstream blueprint use.
