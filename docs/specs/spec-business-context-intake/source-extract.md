# Source Extract: Business Context Intake

## Issue

- `#22`: Create the BMad spec for `STORY-020: Business Context Intake` and
  `FR-024` under `EPIC-003`.
- Scope: Distill the business context intake product contract into a SPEC
  kernel and companions so downstream development can implement structured
  intake without drifting from the enterprise Agent Harness delivery model.
- Acceptance: SPEC captures business goals, PRD, workflows, roles, risks,
  constraints, success metrics, and acceptance criteria as first-class intake
  inputs.
- Acceptance: SPEC defines assumptions that require business owner
  confirmation.
- Acceptance: SPEC preserves links to PRD, EPIC-003, and STORY-020.

## PRD

- `FR-024`: The product must accept and structure business goals, business PRDs,
  workflows, roles, risks, constraints, success metrics, and acceptance criteria
  as first-class inputs to harness delivery.
- `FR-028`: Business success criteria and acceptance criteria must map into
  deterministic evaluator checks, regression fixtures, and run evidence.
- `BR-003`: The product must support enterprise-grade delivery of business Agent
  Harnesses from business goals, business PRDs, and business environment
  definitions.
- Post-delivery operating model: business owner or product owner supplies
  business goal, business PRD, workflows, risks, and success metrics.
- The product must not become a free-form code generation interface; code-agent
  work must be constrained by PRD entries, epics, stories, specs, contracts, CI
  gates, deterministic evaluators, and delivery evidence.

## EPIC-003

- Goal: Define the product boundary and delivery workflow for using
  `harness-trainer` as the construction system for enterprise business Agent
  Harnesses.
- Acceptance: Business goals and business PRDs are first-class inputs.
- Acceptance: Business evaluation criteria map back to business goals and
  acceptance criteria.
- Acceptance: Code-agent-assisted implementation work is bounded by issue,
  story, spec, contract, evaluator, allowed edit surface, and review evidence.

## STORY-020

- User Story: As a business owner, I want business goals, business PRDs,
  workflows, roles, risks, and acceptance criteria to be captured as structured
  inputs so that the Agent Harness is built around real business intent.
- Implementation plan: Define a business context intake template.
- Implementation plan: Include goals, users, workflows, roles, constraints,
  risks, and success metrics.
- Implementation plan: Map each accepted business requirement to harness
  capability areas.
- Implementation plan: Mark assumptions that require business owner
  confirmation.
- Acceptance: Intake captures business goals and success criteria.
- Acceptance: Intake captures business workflows and roles.
- Acceptance: Intake captures acceptance criteria and risks.
- Acceptance: Intake output can be referenced by the harness blueprint.

## Project Alignment

- README: `harness-trainer` is used by an enterprise Agent delivery team, not
  only by programmers.
- README: The delivery team captures business goal, business PRD, and
  environment inventory, then uses `harness-trainer` to produce blueprint,
  contracts, stories, specs, and evaluator expectations.
- AGENTS.md: Every implementation must remain anchored to business intent,
  approved requirements, bounded stories, explicit contracts, and objective
  evaluation evidence.
