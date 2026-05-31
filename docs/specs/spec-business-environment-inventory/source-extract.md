# Source Extract: Business Environment Inventory

This file preserves load-bearing source claims used by
`SPEC-business-environment-inventory`.

## Issue

Source: GitHub issue #26

- Create the BMad SPEC for `STORY-021: Business Environment Inventory` and
  `FR-025` under `EPIC-003`.
- SPEC must preserve load-bearing claims from PRD, EPIC-003, STORY-021, README,
  AGENTS, and architecture notes.
- SPEC must define inventory scope for tools, APIs, databases, data sources,
  knowledge bases, permissions, approvals, secrets, logging, monitoring, and
  audit systems.
- SPEC must explain how inventory output feeds `FR-026` Business Agent Harness
  Blueprint.

## README

Source: `README.md`

- `harness-trainer` is an engineering delivery system for enterprise business
  Agents, not the business Agent itself.
- It takes a business goal, business PRD, and business environment, then drives
  work needed to produce a governed, observable, evaluable Agent Harness.
- The delivery team captures business goal, business PRD, and environment
  inventory before producing blueprint, contracts, stories, specs, and
  evaluator expectations.
- Business environment inventory includes tools and APIs, databases and data
  sources, knowledge bases and documents, permission systems and secrets,
  approval processes, and logging, monitoring, and audit systems.
- Outputs include Business Agent Harness blueprint, worker contracts,
  environment integration plan, evaluation plan, CI/CD gates, and run evidence.

## AGENTS

Source: `AGENTS.md`

- The project is for enterprise Agent Harness delivery, not a generic Agent
  production platform, prompt manager, or language-model training project.
- The delivery model begins with business goal, business PRD, and environment
  inventory, then proceeds to harness blueprint, worker contracts, issue, story,
  spec, implementation execution, CI evidence, evaluator evidence, human
  review, and keep/discard/retry/handoff decision.
- Code agents may implement bounded work packages, but they do not replace the
  business owner, product owner, architect, reviewer, PRD, story, contract,
  evaluator, or delivery evidence.

## PRD

Source: `docs/prd.md`

- `FR-025`: The product must capture the business environment required by the
  target Agent, including tools, APIs, databases, data sources, knowledge bases,
  permission systems, approval processes, secrets, logging, monitoring, and
  audit systems.
- `FR-026`: The product must transform business context and environment
  inventory into a Business Agent Harness blueprint covering Agent purpose,
  tool contracts, knowledge access, policy, approval, budget, session, events,
  tracing, and evaluation.
- Assumption: the business Agent owner supplies or approves the business PRD
  and environment inventory.

## EPIC-003

Source: `docs/epics/EPIC-003-enterprise-business-agent-delivery.md`

- Goal: define the product boundary and delivery workflow for using
  `harness-trainer` as the construction system for enterprise business Agent
  Harnesses.
- `FR-025` is a functional requirement under EPIC-003.
- `STORY-021` defines business environment inventory.
- Acceptance requires business environment inventory to be a first-class input.
- Delivery outputs include blueprint, contracts, integration plan, evaluator
  plan, CI evidence, and run evidence.

## STORY-021

Source: `docs/stories/STORY-021-business-environment-inventory.md`

- User story: as a platform engineer, I want a structured business environment
  inventory so that tools, APIs, databases, knowledge sources, permissions,
  approvals, and observability systems are known before harness implementation.
- Implementation plan: define an environment inventory template.
- Implementation plan: include tools, APIs, databases, data sources, knowledge
  bases, permissions, approval systems, secrets, logs, metrics, and audit
  systems.
- Implementation plan: record ownership, access method, risk, and test strategy
  for each item.
- Implementation plan: link environment items to tool contracts and policy
  rules.
- Acceptance: inventory covers tools, data, knowledge, permissions, approvals,
  and observability.
- Acceptance: each environment item has an owner and access boundary.
- Acceptance: each environment item can map to a worker contract or policy rule.

## Architecture

Source: `docs/architecture.md`

- The delivery pipeline is: Business Goal -> Business PRD -> Business
  Environment Inventory -> Business Agent Harness Blueprint -> Worker Contracts
  -> Harness Runtime / Implementation Plan -> Business Evaluator -> CI Evidence
  + Run Evidence -> Keep / Discard / Crash Decision.
- The pipeline is intentionally not an Agent marketplace or generic Agent
  production platform.

## Prior SPEC

Source: `docs/specs/spec-business-context-intake/SPEC.md`

- Business context intake does not capture technical environment inventory;
  that belongs to `FR-025` and `STORY-021`.
- Intake must precede blueprint work and separate confirmed facts from
  assumptions and open questions.

## Preservation Notes

- Wrapper-only content omitted: issue ceremony, file names, and process
  instructions that do not change downstream design decisions.
- No source claim requires choosing a runtime, SDK, storage technology, or UI.
