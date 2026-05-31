---
id: SPEC-business-context-intake
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #22. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Business Context Intake

## Why

`harness-trainer` needs business context intake because enterprise Agent
Harness delivery starts from business intent, not from free-form code-agent
tasks. Delivery teams need a structured way to capture goals, PRDs, workflows,
roles, risks, constraints, success metrics, and acceptance criteria before a
Harness Blueprint, worker contracts, evaluator, or code-agent execution package
can be produced.

## Capabilities

- id: CAP-1
  intent: Business owners can submit business intent in a structured intake
    artifact before harness design begins.
  success: The intake captures business goals, business PRD reference or
    summary, workflows, roles, constraints, risks, success metrics, and
    acceptance criteria as named fields.

- id: CAP-2
  intent: Harness architects can identify whether the business context is ready
    for blueprint and contract work.
  success: The intake marks required fields, missing information, ambiguous
    claims, and assumptions that require business owner confirmation.

- id: CAP-3
  intent: Delivery teams can map accepted business requirements to harness
    capability areas.
  success: Each accepted business requirement links to at least one relevant
    harness area such as tools, knowledge, policy, approval, budget, session,
    events, tracing, or evaluation.

- id: CAP-4
  intent: Evaluator designers can derive business-relevant checks from intake
    evidence.
  success: Success metrics and acceptance criteria are recorded in a form that
    can feed deterministic evaluator checks, regression fixtures, and run
    evidence.

- id: CAP-5
  intent: Code-agent-assisted delivery can start from approved context rather
    than ad hoc prompts.
  success: Downstream stories, specs, and code-agent execution packages can
    cite the intake artifact as their source for business intent and review
    evidence.

## Constraints

- Intake must precede Business Agent Harness Blueprint work for the same target
  Agent.
- Intake must preserve business ownership; programmers and code agents may not
  redefine goals, acceptance criteria, or risks without traceable confirmation.
- Intake must separate confirmed business facts from assumptions and open
  questions.
- Intake must not require choosing a specific harness runtime, model provider,
  or implementation stack.
- Intake artifacts must be usable by downstream specs, stories, evaluators, and
  delivery packages without relying on chat history.

## Non-goals

- This SPEC does not implement the Business Agent Harness runtime.
- This SPEC does not capture technical environment inventory; that belongs to
  `FR-025` and `STORY-021`.
- This SPEC does not produce the final Harness Blueprint; that belongs to
  `FR-026` and `STORY-022`.
- This SPEC does not make code agents product owners or business approvers.

## Success signal

A harness delivery lead can take a completed intake artifact and determine
whether the target business Agent has enough confirmed goals, workflows, roles,
risks, constraints, success metrics, and acceptance criteria to begin blueprint,
contract, evaluator, and bounded code-agent execution work.

## Assumptions

- The business owner or product owner can approve the final intake artifact.
- A business PRD may be a linked external document, a repository document, or a
  structured summary when the source document is not available.
- Initial intake can be document-based before a UI or API exists.

## Open Questions

- Should intake artifacts use Markdown templates first, or should the first
  implementation define a machine-readable schema?
- Which fields should block downstream blueprint generation versus remain
  warnings for reviewer judgment?
