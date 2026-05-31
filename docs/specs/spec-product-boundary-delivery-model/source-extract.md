# Source Extract: Product Boundary and Delivery Model

## Issue

Source: GitHub issue #62

- Create the BMad SPEC for `STORY-019 / FR-023` product boundary and delivery
  model.
- Scope includes defining `harness-trainer` as an enterprise business Agent
  Harness delivery system, distinguishing business Agent, Agent Harness,
  Harness Training, and Agent production platform, defining users, inputs,
  outputs, delivery pipeline, and non-goals, and preserving README, PRD,
  AGENTS, architecture, EPIC-003, and STORY-019 boundary language.
- Acceptance requires README and PRD boundary claims to be preserved, the SPEC
  to state what the product delivers and does not deliver, distinction between
  Agent Harness delivery and business Agent ownership, and mapping to
  `FR-023`, `STORY-019`, and `EPIC-003`.

## README

Source: `README.md`

- `harness-trainer` is an engineering delivery system for enterprise business
  Agents.
- It is not the business Agent itself; it is the construction crew for building
  a governed, observable, evaluable Agent Harness for that business Agent.
- Inputs include business goal, business PRD, and business environment.
- Core deliverable is an Agent Harness and its training loop: turn
  orchestration, tool policy, approval flow, budgets, resumable sessions,
  context compaction, skills, event streams, tracing, local evaluation, and the
  keep/discard loop.
- The delivered product is used by an enterprise Agent delivery team, not only
  programmers.
- Users include business owners, Agent product owners or analysts, harness
  architects, platform engineers, programmers, and code agents.
- Code agents are bounded execution roles; the repository defines what code
  must satisfy, why it exists, how it is evaluated, and when it is safe to keep.
- Outputs include Business Agent Harness blueprint, worker contracts,
  environment integration plan, Agent runtime plan or implementation,
  evaluation plan, deterministic harness evaluator, CI/CD and governance gates,
  run logs/events/traces/scores/keep-discard records, enterprise delivery
  package, and code-agent execution package.
- Non-goals include generic Agent marketplace, direct language model training,
  replacing business PRD ownership, allowing programmers or code agents to
  redefine business goals without traceable approval, general workflow
  automation, and treating prompt management as the whole product.

## AGENTS

Source: `AGENTS.md`

- The goal is not to train a language model; it is to improve the operating
  system around an agent: turn loop, tool policy, approval handling, budget
  control, session durability, context management, observability, and
  evaluation loop.
- The object under optimization is the harness, not the benchmark task executed
  by the harness.
- The project is not a generic Agent production platform, free-form code
  generation interface, prompt manager, or language-model training project.
- The delivered product is used by an Agent Harness delivery team that may
  include business owners, product owners, analysts, architects, platform
  engineers, programmers, reviewers, and code agents.
- Programmers and code agents are execution roles and do not replace business
  owner, product owner, architect, reviewer, PRD, story, contract, evaluator,
  or delivery evidence.
- Delivery model: business goal / business PRD / environment inventory,
  harness blueprint, worker contracts, issue/story/spec, programmer or
  code-agent execution, CI and evaluator evidence, human review, keep/discard,
  retry, or handoff decision.

## PRD

Source: `docs/prd.md`

- `harness-trainer` is not the business Agent itself; it is the construction
  crew that drives work needed to produce a governed, observable, evaluable
  Agent Harness.
- Primary users include the Agent Harness delivery team: business owners,
  product owners, analysts, harness architects, platform engineers,
  programmers, reviewers, and code agents.
- `FR-023`: The product must explicitly define itself as an enterprise
  business Agent Harness delivery system, not as a business Agent, generic
  Agent production platform, language model trainer, or prompt manager.
- Business Agent owner supplies or approves the business PRD and environment.
- Every business Agent delivery package maps business goals and business
  requirements into delivery and evaluation evidence.

## Epic

Source: `docs/epics/EPIC-003-enterprise-business-agent-delivery.md`

- Goal: Define the product boundary and delivery workflow for using
  `harness-trainer` as the construction system for enterprise business Agent
  Harnesses.
- Acceptance requires README and PRD to clearly distinguish business Agent,
  Agent Harness, Harness Training, and Agent production platform.
- Business goals, business PRDs, and business environment inventory are
  first-class inputs.
- Delivery outputs include blueprint, contracts, integration plan, evaluator
  plan, CI evidence, and run evidence.
- Code-agent-assisted implementation work is bounded by issue, story, spec,
  contract, evaluator, allowed edit surface, and review evidence.

## Story

Source: `docs/stories/STORY-019-product-boundary-delivery-model.md`

- As a project maintainer, the product boundary must state that
  `harness-trainer` delivers enterprise business Agent Harnesses, not business
  Agents or a generic Agent production platform.
- Implementation plan:
  - Update README with product positioning, users, inputs, outputs, and
    non-goals.
  - Update PRD product section with the same boundary.
  - Update architecture with the delivery pipeline.
  - Keep Agent production platform and model training explicitly out of scope.
- Acceptance:
  - README states what the product delivers.
  - README states what the product does not deliver.
  - PRD distinguishes Agent Harness delivery from business Agent ownership.
  - Architecture includes the delivery pipeline.

## Architecture

Source: `docs/architecture.md`

- Product boundary is enterprise business Agent Harness delivery.
- A business team brings business goals, business PRD, and business
  environment.
- The system produces an Agent Harness blueprint, worker contracts,
  environment integration plan, evaluator plan, implementation evidence, and
  training loop for that business Agent Harness.
- Business Agent Delivery Pipeline:
  - Business Goal
  - Business PRD
  - Business Environment Inventory
  - Business Agent Harness Blueprint
  - Worker Contracts
  - Harness Runtime / Implementation Plan
  - Business Evaluator
  - CI Evidence + Run Evidence
  - Keep / Discard / Crash Decision
- The pipeline is not an Agent marketplace or generic Agent production
  platform; it delivers the harness that lets a specific business Agent run
  safely and improve over time.

## Neighboring Specs

Source: `docs/specs/spec-business-context-intake/source-extract.md`

- Business context intake must not drift from the enterprise Agent Harness
  delivery model.
- The product must not become a free-form code generation interface.
- Code-agent work must be constrained by PRD entries, epics, stories, specs,
  contracts, CI gates, deterministic evaluators, and delivery evidence.

Source: `docs/specs/spec-enterprise-delivery-package/source-extract.md`

- `FR-023` requires the product to define itself as an enterprise business
  Agent Harness delivery system, not as a business Agent, generic Agent
  production platform, language model trainer, or prompt manager.
- Enterprise delivery package evidence depends on the product boundary and
  delivery workflow.

## Wrapper-Only Content

- GitHub issue URLs, user avatar metadata, API node IDs, timestamps, and local
  command invocation details are process metadata and are not part of the
  product contract.
