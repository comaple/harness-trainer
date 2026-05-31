---
id: SPEC-product-boundary-delivery-model
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #62. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Product Boundary and Delivery Model

## Why

`harness-trainer` needs an explicit product boundary so downstream planning,
code-agent work, and enterprise delivery artifacts stay focused on building
business Agent Harnesses. The product is the construction system for a governed,
observable, evaluable Agent Harness around a target business Agent; it is not
the business Agent itself, a generic Agent production platform, a language model
trainer, a prompt manager, or a free-form code generation interface.

## Capabilities

- id: CAP-1
  intent: Maintainers can state what product `harness-trainer` delivers.
  success: Product-facing artifacts define the deliverable as an enterprise
    business Agent Harness delivery system that turns business goals, business
    PRDs, and business environment inventory into blueprint, contracts,
    implementation plan, evaluators, CI evidence, run evidence, and handoff
    package.

- id: CAP-2
  intent: Delivery teams can distinguish the business Agent from the Agent
    Harness.
  success: The business Agent remains the business-owned product or workflow
    capability; the Agent Harness is the engineered operating layer containing
    turn orchestration, tool policy, approval flow, budget control, sessions,
    context management, skills, event streams, tracing, and evaluation.

- id: CAP-3
  intent: Users and execution roles are explicit.
  success: Boundary artifacts identify business owners, Agent product owners,
    analysts, harness architects, platform engineers, programmers, reviewers,
    and code agents; programmers and code agents are execution roles, not the
    owners of business goals, product direction, contracts, review decisions,
    or delivery evidence.

- id: CAP-4
  intent: Inputs and outputs of the delivery system are stable.
  success: Inputs include business goals, business PRD, workflows, roles,
    risks, acceptance criteria, success metrics, tools, APIs, databases,
    knowledge sources, permissions, secrets boundaries, approval processes,
    audit systems, model constraints, budget, policy, session/memory rules, and
    evaluator requirements; outputs include harness blueprint, worker
    contracts, environment integration plan, runtime or implementation plan,
    evaluation plan, deterministic evaluator, CI/CD gates, run evidence,
    keep/discard records, enterprise delivery package, and bounded code-agent
    execution package.

- id: CAP-5
  intent: The delivery pipeline remains auditable from business intent to
    handoff.
  success: The pipeline preserves the order business goal, business PRD,
    business environment inventory, Business Agent Harness Blueprint, worker
    contracts, runtime or implementation plan, business evaluator, CI evidence,
    run evidence, keep/discard/crash decision, and enterprise handoff.

- id: CAP-6
  intent: Out-of-scope product directions are rejected before planning drifts.
  success: Boundary artifacts explicitly exclude generic Agent marketplace,
    generic Agent production platform, direct language-model training, prompt
    management as the whole product, business PRD ownership replacement,
    unrestricted workflow automation, and unbounded code-agent code generation.

## Constraints

- Product documentation, specs, stories, code-agent packages, and delivery
  artifacts must preserve the boundary that `harness-trainer` delivers Agent
  Harnesses for business Agents, not the business Agents themselves.
- Business owners or approved product owners remain accountable for business
  goals, workflows, acceptance criteria, risks, and success metrics.
- Code-agent-assisted implementation must remain bounded by issue, FR ID,
  story ID, spec or worker contract, evaluator or CI command, allowed edit
  surface, and review evidence.
- The delivery model must keep business goal, business PRD, and business
  environment inventory as first-class upstream inputs before blueprint,
  contracts, implementation, and evaluation work.
- Architecture and README language must continue to distinguish business
  Agent, Agent Harness, Harness Training, and Agent production platform.
- Delivery outputs must include evidence, not only generated plans or code.
- Any change that repositions the repository as model training, prompt
  management, generic code generation, generic workflow automation, or an
  Agent marketplace violates this boundary.

## Non-goals

- This SPEC does not implement a business Agent runtime.
- This SPEC does not implement the full Agent Harness runtime.
- This SPEC does not create a generic Agent production platform, marketplace,
  prompt manager, language-model trainer, or free-form code generation tool.
- This SPEC does not transfer business goal ownership to programmers, code
  agents, or the repository.
- This SPEC does not replace the detailed SPECs for intake, environment
  inventory, blueprint, delivery package, business evaluation mapping, or
  code-agent execution package.

## Success signal

A reviewer can inspect the product boundary contract and determine who uses
`harness-trainer`, what inputs it accepts, what outputs it delivers, where the
business Agent remains outside the repository, how the Agent Harness delivery
pipeline proceeds, and which product directions must be rejected before
implementation work begins.

## Assumptions

- Existing README, PRD, AGENTS, and architecture boundary text is authoritative
  and should be preserved rather than rewritten in this issue.
- This SPEC fills the missing downstream machine contract for `FR-023` while
  later EPIC-003 SPECs continue to define detailed delivery artifacts.
- A target business Agent is always business-owned even when the Agent Harness
  is implemented by platform engineers or code agents.

## Open Questions

- Should future CI explicitly reject wording that repositions the repository as
  an Agent production platform or model trainer?
- Should the product boundary appear as a reusable checklist in every
  enterprise delivery package?
