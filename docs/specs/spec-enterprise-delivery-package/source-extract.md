# Source Extract: Enterprise Delivery Package

This file preserves load-bearing source claims used by
`SPEC-enterprise-delivery-package`.

## Issue

Source: GitHub issue #38

- Create the BMad SPEC for `STORY-023: Enterprise Delivery Package` and
  `FR-027` under `EPIC-003`.
- SPEC must preserve load-bearing claims from PRD, EPIC-003, STORY-023,
  README, AGENTS, architecture notes, and upstream EPIC-003 SPECs/templates.
- SPEC must define delivery package contents: PRD traceability, architecture,
  worker contracts, implementation plan, environment integration plan,
  evaluator plan, CI evidence, run evidence, and operational handoff evidence.
- SPEC must define package completion criteria and how package evidence is
  updated after harness training iterations.
- SPEC keeps code-agent execution package work separate unless referenced as a
  downstream package component.

## README

Source: `README.md`

- `harness-trainer` is an engineering delivery system for enterprise business
  Agents, not the business Agent itself.
- It takes a business goal, business PRD, and business environment, then drives
  the work needed to produce a governed, observable, evaluable Agent Harness.
- The delivered product is used by an enterprise Agent delivery team that may
  include business owners, product owners, analysts, harness architects,
  platform engineers, programmers, and code agents.
- The operating model captures business goal, business PRD, and environment
  inventory; produces blueprint, contracts, stories, specs, and evaluator
  expectations; validates changes through CI, traceability gates, and
  deterministic evaluators; reviews keep/discard/crash evidence; and ships an
  auditable Agent Harness delivery package.
- Outputs include Business Agent Harness blueprint, worker contracts,
  environment integration plan, Agent runtime plan or implementation,
  evaluation plan, deterministic harness evaluator, CI/CD and governance gates,
  run logs, events, traces, scores, and keep/discard records.

## AGENTS

Source: `AGENTS.md`

- The project improves the operating system around an agent: turn loop, tool
  policy, approval handling, budget control, session durability, context
  management, observability, and evaluation loop.
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

- `FR-027`: The product must produce a delivery package for each target
  business Agent Harness, including PRD traceability, architecture, worker
  contracts, implementation plan, environment integration plan, evaluator plan,
  CI evidence, and run evidence.
- `FR-023`: The product must explicitly define itself as an enterprise business
  Agent Harness delivery system, not as a business Agent, generic Agent
  production platform, language model trainer, or prompt manager.
- `FR-024`: Business context intake captures goals, business PRDs, workflows,
  roles, risks, constraints, success metrics, and acceptance criteria.
- `FR-025`: Business environment inventory captures tools, APIs, databases,
  data sources, knowledge bases, permissions, approvals, secrets, logging,
  monitoring, and audit systems.
- `FR-026`: Business Agent Harness Blueprint covers Agent purpose, tool
  contracts, knowledge access, policy, approval, budget, session, events,
  tracing, and evaluation.
- `FR-028`: Business success criteria and acceptance criteria map to
  deterministic evaluator checks, regression fixtures, and run evidence.
- `FR-029`: Code-agent work packages include issue reference, requirement IDs,
  story ID, spec context, worker contract expectations, evaluator command,
  allowed files, and acceptance evidence.
- Enterprise delivery must account for auditability, access control,
  environment integration risk, operational handoff, and repeatable evaluation.
- Every business Agent delivery package maps business goals and business
  acceptance criteria to delivery evidence.

## EPIC-003

Source: `docs/epics/EPIC-003-enterprise-business-agent-delivery.md`

- Goal: define product boundary and delivery workflow for using
  `harness-trainer` as the construction system for enterprise business Agent
  Harnesses.
- `FR-027` is a functional requirement under EPIC-003.
- `STORY-023` defines enterprise delivery package.
- Delivery outputs include blueprint, contracts, integration plan, evaluator
  plan, CI evidence, and run evidence.
- Code-agent-assisted implementation work is bounded by issue, story, spec,
  contract, evaluator, allowed edit surface, and review evidence.

## STORY-023

Source: `docs/stories/STORY-023-enterprise-delivery-package.md`

- User story: as an enterprise reviewer, I want a complete delivery package for
  each business Agent Harness so that I can audit intent, implementation,
  environment access, test evidence, and operational handoff.
- Implementation plan: define delivery package contents.
- Implementation plan: include PRD traceability, architecture, worker
  contracts, implementation plan, environment integration plan, evaluator plan,
  CI evidence, and run evidence.
- Implementation plan: define package completion criteria.
- Implementation plan: define how package evidence is updated after harness
  training iterations.
- Acceptance: delivery package lists required artifacts.
- Acceptance: delivery package includes CI and evaluator evidence.
- Acceptance: delivery package can be audited from business goal to run
  evidence.

## Architecture

Source: `docs/architecture.md`

- The documentation kernel is the source of truth for product intent and agile
  decomposition.
- The local quality gate is `scripts/ci_check.py`; GitHub workflow is
  `.github/workflows/ci.yml`.
- The gate validates repository hygiene, required files, Markdown links, agile
  traceability, code traceability, and commit-message traceability.
- Future runtime boundaries include turn orchestration, policy, approval,
  budget, session persistence, event streams, and evaluation.
- Capability catalog, worker contract, and replacement safety evaluator form
  the replaceability spine.
- Replacement safety is evaluated against declared evidence, not developer
  intent.
- Business Agent Delivery Pipeline: Business Goal -> Business PRD -> Business
  Environment Inventory -> Business Agent Harness Blueprint -> Worker
  Contracts -> Harness Runtime / Implementation Plan -> Business Evaluator ->
  CI Evidence + Run Evidence -> Keep / Discard / Crash Decision.
- The pipeline is not an Agent marketplace or generic Agent production
  platform.

## Upstream Intake SPEC

Source: `docs/specs/spec-business-context-intake/SPEC.md`

- Business context intake captures business goals, PRD reference or summary,
  workflows, roles, constraints, risks, success metrics, and acceptance
  criteria before blueprint work begins.
- Intake artifacts must be usable by downstream specs, stories, evaluators, and
  delivery packages without relying on chat history.

## Upstream Environment SPEC

Source: `docs/specs/spec-business-environment-inventory/SPEC.md`

- Environment inventory records tools, APIs, databases, data sources, knowledge
  bases, permissions, approvals, secrets, logging, monitoring, and audit
  systems.
- Inventory artifacts must be usable by downstream specs, stories, contracts,
  evaluators, and delivery packages without relying on chat history.
- Inventory does not implement environment integrations, grant access, or
  replace enterprise security, compliance, or data-governance approvals.

## Upstream Blueprint SPEC

Source: `docs/specs/spec-business-agent-harness-blueprint/SPEC.md`

- The blueprint links business goals, user tasks, environment dependencies,
  harness capabilities, worker contracts, policy, approval, budget, session,
  events, tracing, and evaluation into one auditable delivery plan.
- Blueprint artifacts must be usable by downstream specs, stories, contracts,
  evaluators, delivery packages, and code-agent work packages without relying
  on chat history.
- The blueprint does not create the enterprise delivery package; that belongs
  to `FR-027` and `STORY-023`.

## Upstream Evaluation Mapping SPEC and Template

Sources:

- `docs/specs/spec-business-evaluation-mapping/SPEC.md`
- `docs/evaluation/business-evaluation-mapping-template.md`

Load-bearing claims:

- Business evaluation mapping turns business success criteria and acceptance
  criteria into deterministic evaluator checks, regression fixtures, run
  evidence, failure classification, and keep/discard/crash decisions.
- Evaluation mapping must be usable by downstream stories and code-agent work
  packages without relying on chat history.
- The evaluation mapping template captures source inputs, business criteria
  coverage, evaluator checks, regression fixtures and scenarios, failure
  classification, run evidence, decision evidence, open gaps, code-agent work
  package links, and mapping readiness.
- The evaluation mapping SPEC does not create the final enterprise delivery
  package; that belongs to `FR-027` and `STORY-023`.

## Preservation Notes

- Wrapper-only content omitted: issue ceremony, exact PR wording, and process
  instructions that do not change downstream design decisions.
- No source claim requires choosing a runtime, SDK, model provider, UI,
  database client, production access method, or secret storage mechanism in
  this SPEC.
- This SPEC preserves `FR-029` code-agent execution package as a separate
  downstream artifact that the delivery package may reference.
