# Source Extract: Code Agent Execution Package

## User Request

- Continue the EPIC-003 delivery workflow after completing the Enterprise
  Delivery Package.
- Create the BMad SPEC for `STORY-026: Code Agent Execution Package` and
  `FR-029` before downstream implementation.
- Preserve the project boundary: programmers and code agents are execution
  roles, not owners of business goals, PRD scope, architecture, evaluator
  criteria, or delivery decisions.

## Issue #42

Source: GitHub issue `#42`

- Title: `FR-029: Create code agent execution package spec`
- Scope: distill the canonical contract for bounded programmer/code-agent
  execution packages.
- Required fields: issue, FR, story, spec or worker contract context,
  evaluator/CI commands, allowed edit surface, acceptance evidence,
  implementation evidence, test evidence, evaluator output, and review
  outcome.
- Acceptance: execution packages identify the exact issue, FR, Story, spec or
  contract, and evaluator expectation for a code agent task.
- Acceptance: execution packages constrain allowed edits and required evidence
  before review.
- Acceptance: code-agent-assisted work remains auditable from business intent
  to delivery evidence.

## README Product Boundary

Source: `README.md`

- `harness-trainer` is an engineering delivery system for enterprise business
  Agents.
- It is not the business Agent itself.
- It is the construction crew for building a governed, observable, evaluable
  Agent Harness for a business Agent.
- Programmers and code agents are execution roles inside the delivery loop; they
  do not own product direction by themselves.
- Code agents execute bounded stories and specs under repository gates,
  contracts, and evaluator checks.
- The delivery team gives bounded implementation tasks to programmers or code
  agents, validates changes through CI, traceability gates, and deterministic
  evaluators, reviews keep/discard/crash evidence, and ships an auditable Agent
  Harness delivery package.
- The repository defines what code must satisfy, why it exists, how it is
  evaluated, and when it is safe to keep.

## AGENTS Product Alignment

Source: `AGENTS.md`

- The project is for enterprise Agent Harness delivery.
- It is not a generic Agent production platform, free-form code generation
  interface, prompt manager, or language-model training project.
- The delivery team may include business owners, Agent product owners,
  analysts, harness architects, platform engineers, programmers, reviewers, and
  code agents.
- Programmers and code agents are execution roles and do not replace business
  owner, product owner, architect, reviewer, PRD, story, contract, evaluator, or
  delivery evidence.
- Implementation must remain anchored to business intent, approved
  requirements, bounded stories, explicit contracts, and objective evaluation
  evidence.
- A code agent should receive a bounded work package before editing code.
- Required work package contents include issue reference, `FR-XXX`,
  `STORY-XXX`, relevant spec or worker contract, expected evaluator or CI
  command, allowed edit surface, and acceptance evidence required for review.
- The code agent implements the bounded package, runs required checks, and
  reports evidence.
- The delivery lead or reviewer decides whether the change is kept, revised,
  discarded, or handed off.

## PRD

Source: `docs/prd.md`

- `FR-029`: The product must be able to package bounded implementation work for
  programmers or code agents.
- Required package contents include issue reference, PRD requirement IDs, story
  ID, spec context, worker contract expectations, evaluator command, allowed
  files, and acceptance evidence required before review.

## EPIC-003

Source: `docs/epics/EPIC-003-enterprise-business-agent-delivery.md`

- `FR-029` is a functional requirement under EPIC-003.
- `STORY-026` defines the code agent execution package.
- EPIC acceptance requires code-agent-assisted implementation work to be
  bounded by issue, story, spec, contract, evaluator, allowed edit surface, and
  review evidence.

## STORY-026

Source: `docs/stories/STORY-026-code-agent-execution-package.md`

- User story: as a harness delivery lead, I want a bounded execution package
  for programmers and code agents so that implementation work stays tied to
  approved business intent, stories, specs, contracts, evaluator expectations,
  and review evidence.
- Implementation plan: define required fields for issue reference, `FR-XXX`,
  `STORY-XXX`, spec or worker contract context, evaluator and CI commands,
  allowed edit surface, and acceptance evidence.
- Implementation plan: define how the package is created from business context,
  environment inventory, blueprint, and worker contracts.
- Implementation plan: define how code agents report implementation evidence,
  test evidence, and evaluator output.
- Implementation plan: define review outcomes: keep, revise, discard, retry,
  or handoff.
- Acceptance: execution packages identify the exact issue, FR, Story, spec or
  contract, and evaluator expectation for a code agent task.
- Acceptance: execution packages constrain allowed edits and required evidence
  before review.
- Acceptance: code-agent-assisted work remains auditable from business intent
  to delivery evidence.

## Blueprint Template

Source: `docs/blueprint/business-agent-harness-template.md`

- Business Agent Harness Blueprint includes Code-Agent Work Package Boundaries.
- Work package boundaries include issue/story/spec reference, allowed edit
  surface, required contract, required evaluator, validation command, review
  evidence, and status.
- Blueprint readiness requires implementation story slices to be bounded by
  issue/story/spec, contract, evaluator, allowed edit surface, and validation
  command.
- Code-agent work packages cannot redefine business goals, environment access
  boundaries, policy decisions, or acceptance criteria.

## Evaluation Mapping Template

Source: `docs/evaluation/business-evaluation-mapping-template.md`

- Business evaluation mapping includes Code-Agent Work Package Links.
- Work package links include required evaluator check, fixture or scenario,
  validation command, required review evidence, allowed edit surface, and
  status.
- Mapping readiness requires code-agent work packages to cite issue/story/spec,
  evaluator check, validation command, allowed edit surface, and review
  evidence.

## Enterprise Delivery Package SPEC and Template

Sources:

- `docs/specs/spec-enterprise-delivery-package/SPEC.md`
- `docs/delivery/enterprise-delivery-package-template.md`

Load-bearing claims:

- The Enterprise Delivery Package references bounded work packages by issue,
  story, spec, worker contract, allowed edit surface, validation command, and
  review evidence when implementation work exists.
- Code-agent execution package work is referenced as a package component but is
  defined by `FR-029` and `STORY-026`.
- Delivery packages must preserve traceability from business goal and PRD
  requirement to implementation evidence, evaluator evidence, and run evidence.
- Delivery packages must not expose secret values or production credentials.

## Preservation Notes

- All load-bearing claims above are represented in `SPEC.md` capabilities,
  constraints, non-goals, success signal, assumptions, or open questions.
- Wrapper-only process details, timestamps, and API metadata were not carried
  forward because they do not change downstream implementation decisions.
