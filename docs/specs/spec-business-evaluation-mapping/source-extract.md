# Source Extract: Business Evaluation Mapping

This file preserves load-bearing source claims used by
`SPEC-business-evaluation-mapping`.

## Issue

Source: GitHub issue #34

- Create the BMad SPEC for `STORY-024: Business Evaluation Mapping` and
  `FR-028` under `EPIC-003`.
- SPEC must preserve load-bearing claims from PRD, EPIC-003, STORY-024,
  README, AGENTS, architecture/evaluator notes, and upstream intake/blueprint
  SPECs.
- SPEC must define how business success criteria and acceptance criteria map to
  deterministic evaluator checks, regression fixtures, and run evidence.
- SPEC must identify failure classes including incorrect tool use, missing
  approval, policy violation, unsupported data access, budget overrun, and poor
  task outcome.
- SPEC must define result evidence for keep, discard, and crash decisions.

## README

Source: `README.md`

- `harness-trainer` is an engineering delivery system for enterprise business
  Agents, not the business Agent itself.
- It takes a business goal, business PRD, and business environment, then drives
  the work needed to produce a governed, observable, evaluable Agent Harness.
- The core deliverable is an Agent Harness and its training loop: turn
  orchestration, tool policy, approval flow, budgets, resumable sessions,
  context compaction, skills, event streams, tracing, local evaluation, and the
  keep/discard loop for improving the harness.
- The operating model uses deterministic evaluators and traceability gates,
  reviews keep/discard/crash evidence, and ships an auditable Agent Harness
  delivery package.
- Outputs include an evaluation plan and deterministic harness evaluator, CI/CD
  and governance gates, run logs, events, traces, scores, and keep/discard
  records.

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
- A code-agent work package should include the expected evaluator or CI
  command and acceptance evidence required for review.

## PRD

Source: `docs/prd.md`

- `FR-028`: The product must map business success criteria and acceptance
  criteria into deterministic evaluator checks, regression fixtures, and run
  evidence so that harness training optimizes business-relevant outcomes.
- `FR-026`: The product must transform business context and environment
  inventory into a Business Agent Harness blueprint covering Agent purpose,
  tool contracts, knowledge access, policy, approval, budget, session, events,
  tracing, and evaluation.
- `FR-027`: The product must produce a delivery package for each target
  business Agent Harness, including PRD traceability, architecture, worker
  contracts, integration plan, evaluator plan, CI evidence, and run evidence.
- `FR-029`: Code-agent work packages must include issue reference, PRD
  requirement IDs, story ID, spec context, worker contract expectations,
  evaluator command, allowed files, and acceptance evidence.

## EPIC-003

Source: `docs/epics/EPIC-003-enterprise-business-agent-delivery.md`

- Goal: define product boundary and delivery workflow for using
  `harness-trainer` as the construction system for enterprise business Agent
  Harnesses.
- `FR-028` is a functional requirement under EPIC-003.
- `STORY-024` defines business evaluation mapping.
- Acceptance requires business evaluation criteria to map back to business
  goals and acceptance criteria.
- Delivery outputs include blueprint, contracts, integration plan, evaluator
  plan, CI evidence, and run evidence.
- Code-agent-assisted implementation must be bounded by issue, story, spec,
  contract, evaluator, allowed edit surface, and review evidence.

## STORY-024

Source: `docs/stories/STORY-024-business-evaluation-mapping.md`

- User story: as a harness trainer, I want business success criteria to map
  into evaluator checks so that harness training improves outcomes that matter
  to the target business Agent.
- Implementation plan: define mapping from business success criteria to
  evaluator checks.
- Implementation plan: define regression fixtures for key workflows.
- Implementation plan: define failure classes such as incorrect tool use,
  missing approval, policy violation, unsupported data access, budget overrun,
  and poor task outcome.
- Implementation plan: add result fields for keep, discard, and crash
  decisions.
- Acceptance: business success criteria have evaluator coverage.
- Acceptance: acceptance criteria map to deterministic checks where possible.
- Acceptance: evaluator output can support keep/discard/crash decisions.

## Architecture

Source: `docs/architecture.md`

- The delivery pipeline is: Business Goal -> Business PRD -> Business
  Environment Inventory -> Business Agent Harness Blueprint -> Worker Contracts
  -> Harness Runtime / Implementation Plan -> Business Evaluator -> CI
  Evidence + Run Evidence -> Keep / Discard / Crash Decision.
- The pipeline is intentionally not an Agent marketplace or generic Agent
  production platform.
- Replacement safety evaluation is evidence-based and can support keeping the
  current implementation, accepting a replacement, or rejecting a replacement
  because contract, state, failure, event, trace, or regression evidence changed
  unexpectedly.
- Implementation candidates must conform to worker contracts and must not
  change neighboring capabilities unless the catalog declares a new replacement
  boundary and evaluator evidence is updated.

## Blueprint Template

Source: `docs/blueprint/business-agent-harness-template.md`

- Blueprint evaluation expectations include evaluator ID, business metric or
  acceptance criteria, harness behavior under test, fixture or scenario, pass
  signal, keep/discard evidence, and status.
- Implementation story slices include business goal, harness capability, worker
  contract, policy rule, evaluator expectation, and validation command.
- Code-agent work package boundaries include issue/story/spec reference,
  allowed edit surface, required contract, required evaluator, validation
  command, and review evidence.

## Upstream Context SPEC

Source: `docs/specs/spec-business-context-intake/SPEC.md`

- Business context intake captures business goals, PRD reference or summary,
  workflows, roles, constraints, risks, success metrics, and acceptance
  criteria before blueprint work begins.
- Success metrics and acceptance criteria are recorded in a form that can feed
  deterministic evaluator checks, regression fixtures, and run evidence.
- Intake must preserve business ownership; programmers and code agents may not
  redefine goals, acceptance criteria, or risks without traceable confirmation.

## Upstream Environment SPEC

Source: `docs/specs/spec-business-environment-inventory/SPEC.md`

- Environment inventory records tools, APIs, databases, data sources, knowledge
  bases, permissions, approvals, secrets, logging, monitoring, and audit
  systems.
- Each environment item records test strategy, fixture or sandbox expectation,
  observability evidence, and failure or fallback behavior.
- Inventory must not expose secret values in repository files, issues, pull
  requests, logs, or CI output.

## Upstream Blueprint SPEC

Source: `docs/specs/spec-business-agent-harness-blueprint/SPEC.md`

- The blueprint maps business success metrics and acceptance criteria to
  evaluator expectations, fixtures, run evidence, and keep/discard review
  criteria.
- Blueprint work must consume business context intake and business environment
  inventory for the same target business Agent.
- Blueprint must preserve traceability from business requirement to harness
  capability, worker contract, evaluator expectation, and implementation story.
- Blueprint artifacts must be usable by downstream specs, stories, contracts,
  evaluators, delivery packages, and code-agent work packages without relying
  on chat history.

## Preservation Notes

- Wrapper-only content omitted: issue ceremony, exact PR wording, and process
  instructions that do not change downstream design decisions.
- No source claim requires choosing a runtime, SDK, model provider, UI,
  database client, or production access method in this SPEC.
- This SPEC preserves the distinction between business evaluation mapping and
  generic replacement-safety evaluation.
