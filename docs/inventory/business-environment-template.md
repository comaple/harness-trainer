# Business Environment Inventory Template

Use this template for one target business Agent. Keep confirmed facts separate
from assumptions, open questions, and access requests. Do not record secret
values.

## Inventory Metadata

| Field | Value |
| --- | --- |
| Target business Agent | |
| Business context intake reference | |
| Inventory owner | |
| Platform owner | |
| Business owner | |
| Last updated | |
| Status | draft / under review / confirmed / blocked |

## Environment Summary

| Summary ID | Environment area | Confirmed facts | Assumptions | Open questions |
| --- | --- | --- | --- | --- |
| ENV-SUM-001 | | | | |

## Tools and APIs

| Item ID | Tool or API | Business use | Owner | Access method | Access boundary | Risk | Test strategy | Worker contract | Policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-TOOL-001 | | | | | | | | | | draft |

## Databases and Data Sources

| Item ID | Database or data source | Data class | Owner | Access method | Access boundary | Read/write scope | Risk | Test strategy | Worker contract | Policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-DATA-001 | | | | | | | | | | | draft |

## Knowledge Bases and Documents

| Item ID | Knowledge source | Content type | Owner | Access method | Access boundary | Refresh cadence | Risk | Test strategy | Worker contract | Policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-KNOW-001 | | | | | | | | | | | draft |

## Permission Systems

| Item ID | Permission system | Business use | Owner | Access method | Access boundary | Role model | Risk | Test strategy | Worker contract | Policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-PERM-001 | | | | | | | | | | | draft |

## Approval Processes

| Item ID | Approval process | Trigger condition | Approver owner | Access method | Access boundary | Evidence required | Risk | Test strategy | Worker contract | Policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-APPROVAL-001 | | | | | | | | | | | draft |

## Secrets and Credentials

Do not store a secret value, token, password, private key, or credential
material in this file, an issue, a pull request, a log, or CI output.

| Item ID | Secret purpose | Owner | Storage location class | Access method | Access boundary | Rotation expectation | Risk | Test strategy | Worker contract | Policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-SECRET-001 | | | vault / CI secret / managed identity / other | | | | | | | | draft |

## Logging, Monitoring, Metrics, and Audit Systems

| Item ID | System | Evidence type | Owner | Access method | Access boundary | Retention | Risk | Test strategy | Worker contract | Policy rule | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-OBS-001 | | logs / metrics / traces / audit | | | | | | | | | draft |

## Assumptions

| Assumption ID | Assumption | Affected environment item | Risk if wrong | Confirmation owner | Status |
| --- | --- | --- | --- | --- | --- |
| ENV-ASM-001 | | | | | unconfirmed |

## Open Questions

| Question ID | Question | Affected environment item | Blocks blueprint? | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| ENV-Q-001 | | | yes / no | | open |

## Access Requests

| Request ID | Environment item | Requested access | Request owner | Approver | Access boundary | Risk | Test strategy | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ENV-REQ-001 | | | | | | | | open |

## Harness Mapping

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

| Environment item | Harness area | Worker contract | Policy rule | Event or trace evidence | Evaluator expectation | Blueprint section |
| --- | --- | --- | --- | --- | --- | --- |
| ENV-TOOL-001 | `tools` | | | | | |

## Blueprint Readiness

| Check | Status | Evidence |
| --- | --- | --- |
| Every environment item has an owner. | draft | |
| Every environment item has an access method. | draft | |
| Every environment item has an access boundary. | draft | |
| Every environment item has a risk entry. | draft | |
| Every environment item has a test strategy. | draft | |
| Secrets record handling requirements without storing a secret value. | draft | |
| Assumptions identify a confirmation owner. | draft | |
| Open questions identify whether they block blueprint work. | draft | |
| Access requests identify requested scope and approver. | draft | |
| Harness mapping links items to worker contracts, policy rules, or harness areas. | draft | |
| Blueprint can consume confirmed environment items without relying on chat history. | draft | |
