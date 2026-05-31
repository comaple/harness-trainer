# Source Extract: Business Agent Harness Blueprint

This file preserves load-bearing source claims used by
`SPEC-business-agent-harness-blueprint`.

## Issue

Source: GitHub issue #30

- Create the BMad SPEC for `STORY-022: Business Agent Harness Blueprint` and
  `FR-026` under `EPIC-003`.
- SPEC must preserve load-bearing claims from PRD, EPIC-003, STORY-022, README,
  AGENTS, architecture notes, and upstream context and inventory SPECs.
- SPEC must define blueprint scope for Agent purpose, user tasks, tools,
  knowledge access, policy, approval, budget, session, events, tracing, and
  evaluation.
- SPEC must explain how business goals map to harness capabilities and how
  environment items map to worker contracts.
- SPEC must identify how risks and missing dependencies are surfaced before
  implementation stories.

## README

Source: `README.md`

- `harness-trainer` is an engineering delivery system for enterprise business
  Agents, not the business Agent itself.
- It takes a business goal, business PRD, and business environment, then drives
  work needed to produce a governed, observable, evaluable Agent Harness.
- Harness architects turn business intent into an Agent Harness blueprint,
  worker contracts, policies, approval flows, budgets, sessions, tracing, and
  evaluators.
- The operating model captures business goal, business PRD, and environment
  inventory, then uses `harness-trainer` to produce blueprint, contracts,
  stories, specs, and evaluator expectations.
- Outputs include Business Agent Harness blueprint, worker contracts,
  environment integration plan, evaluation plan, governance gates, run logs,
  events, traces, scores, and keep/discard records.
- The goal is to ingest business goal, business PRD, and business environment,
  generate the Agent Harness blueprint and worker contracts, build or update
  implementation, run evaluators, and keep changes based on evidence.

## AGENTS

Source: `AGENTS.md`

- The project is for enterprise Agent Harness delivery, not a generic Agent
  production platform, prompt manager, or language-model training project.
- The delivery model runs from business goal, business PRD, and environment
  inventory to harness blueprint, worker contracts, issue, story, spec,
  implementation execution, CI evidence, evaluator evidence, human review, and
  keep/discard/retry/handoff decision.
- Code agents may implement bounded work packages but do not replace business
  owner, product owner, architect, reviewer, PRD, story, contract, evaluator,
  or delivery evidence.

## PRD

Source: `docs/prd.md`

- `FR-026`: The product must transform business context and environment
  inventory into a Business Agent Harness blueprint covering Agent purpose,
  tool contracts, knowledge access, policy, approval, budget, session, events,
  tracing, and evaluation.
- `FR-027`: The product must produce a delivery package for each target
  business Agent Harness, including PRD traceability, architecture, worker
  contracts, integration plan, evaluator plan, CI evidence, and run evidence.

## EPIC-003

Source: `docs/epics/EPIC-003-enterprise-business-agent-delivery.md`

- Goal: define product boundary and delivery workflow for using
  `harness-trainer` as the construction system for enterprise business Agent
  Harnesses.
- `FR-026` is a functional requirement under EPIC-003.
- `STORY-022` defines business Agent Harness blueprint.
- Acceptance requires business goals and business PRDs to be first-class
  inputs, business environment inventory to be a first-class input, delivery
  outputs to include blueprint, contracts, integration plan, evaluator plan, CI
  evidence, and run evidence, and code-agent-assisted implementation to be
  bounded by issue, story, spec, contract, evaluator, allowed edit surface, and
  review evidence.

## STORY-022

Source: `docs/stories/STORY-022-business-agent-harness-blueprint.md`

- User story: as a harness architect, I want a Business Agent Harness blueprint
  that turns business context and environment inventory into harness
  capabilities and worker contracts.
- Implementation plan: define blueprint sections for Agent purpose, user tasks,
  tools, knowledge, policy, approval, budget, session, events, tracing, and
  evaluator.
- Implementation plan: map business requirements to harness capability catalog
  entries.
- Implementation plan: map environment inventory items to worker contracts.
- Implementation plan: identify open risks and missing environment
  dependencies.
- Acceptance: blueprint links business goals to harness capabilities.
- Acceptance: blueprint links environment items to worker contracts.
- Acceptance: blueprint identifies policy, approval, and evaluation needs.
- Acceptance: blueprint is sufficient to create implementation stories.

## Architecture

Source: `docs/architecture.md`

- The delivery pipeline is: Business Goal -> Business PRD -> Business
  Environment Inventory -> Business Agent Harness Blueprint -> Worker Contracts
  -> Harness Runtime / Implementation Plan -> Business Evaluator -> CI Evidence
  + Run Evidence -> Keep / Discard / Crash Decision.
- The pipeline is intentionally not an Agent marketplace or generic Agent
  production platform.

## Upstream Context SPEC

Source: `docs/specs/spec-business-context-intake/SPEC.md`

- Business context intake captures business goals, PRD reference or summary,
  workflows, roles, constraints, risks, success metrics, and acceptance
  criteria before blueprint work begins.
- Intake marks required fields, missing information, ambiguous claims, and
  assumptions requiring business owner confirmation.
- Accepted business requirements map to harness areas such as tools, knowledge,
  policy, approval, budget, session, events, tracing, or evaluation.
- Success metrics and acceptance criteria feed deterministic evaluator checks,
  regression fixtures, and run evidence.
- Intake does not produce the final Harness Blueprint; that belongs to
  `FR-026` and `STORY-022`.

## Upstream Environment SPEC

Source: `docs/specs/spec-business-environment-inventory/SPEC.md`

- Environment inventory records tools, APIs, databases, data sources, knowledge
  bases, permissions, approvals, secrets, logging, monitoring, and audit
  systems.
- Each environment item records owner, access method, access boundary,
  credential or secret handling need, and expected harness capability area.
- Each item records permission, approval, audit, privacy, operational, or
  security constraints that can shape policy rules, review gates, or worker
  contracts.
- Each item records test strategy, fixture or sandbox expectation,
  observability evidence, and failure or fallback behavior.
- Inventory items can be mapped to tool contracts, knowledge access, policy,
  approval, budget, session, events, tracing, and evaluation sections of
  `FR-026`.

## Preservation Notes

- Wrapper-only content omitted: issue ceremony, exact PR wording, and process
  instructions that do not change downstream design decisions.
- No source claim requires choosing a runtime, SDK, model provider, UI,
  database client, or production access method in this SPEC.
