# Product Requirements Document

## Product

`harness-trainer` is an engineering delivery system for enterprise business
Agents. It is not the business Agent itself; it is the construction crew that
turns a business goal, business PRD, and business environment into a governed,
observable, evaluable Agent Harness.

The product must preserve a traceable path from business intent to PRD, Epic,
Story, implementation, commit, evaluation, and delivery evidence.

## Source Material

- Agent harness reference:
  [How to Build Your Own Agent Harness](https://iii.dev/blog/how-to-build-your-own-agent-harness/)

This PRD interprets the reference article as a product direction: an agent
harness should be decomposed into replaceable responsibilities with stable
function contracts, shared state boundaries, policy gates, session durability,
and end-to-end observability.

## Requirement Taxonomy

Every PRD must separate these requirement classes:

- Business Requirements (`BR-XXX`): business outcomes, operating model, and
  governance goals.
- User Requirements (`UR-XXX`): needs of maintainers, contributors, reviewers,
  and agent operators.
- Functional Requirements (`FR-XXX`): behavior the system must provide.
- Non-Functional Requirements (`NFR-XXX`): quality attributes such as security,
  reliability, maintainability, usability, auditability, performance, and
  observability.
- Constraints: technical, process, compliance, dependency, and schedule limits.
- Assumptions and Dependencies: conditions the plan relies on.
- Out of Scope: explicit non-goals.
- Success Metrics: measurable evidence that the product is working.

Functional requirements drive epic and story decomposition. Non-functional
requirements must be reflected in acceptance criteria, architecture decisions,
or quality gates when relevant.

## Business Requirements

### BR-001: Governed Harness Development

The project must support a disciplined agile workflow where agent-harness
changes are planned, traceable, reviewed, and gated before integration.

### BR-002: Replaceable Harness Capabilities

The product must help teams design and train harnesses as replaceable
capabilities rather than as a monolithic agent framework.

### BR-003: Enterprise Business Agent Delivery

The product must support enterprise-grade delivery of business Agent Harnesses
from business goals, business PRDs, and business environment definitions.

## User Requirements

### UR-001: Maintainer Traceability

Maintainers must be able to inspect a change and identify the originating
requirement, epic, story, implementation plan, and commit.

### UR-002: Agent Operating Clarity

Agents working in the repository must have clear rules for branch naming,
editable surfaces, required checks, and evidence before implementation.

### UR-003: Harness Architect Planning

Harness architects must be able to decompose a target harness into contracts,
workers, state boundaries, and testable stories before implementation.

### UR-004: Reviewer Runtime Evidence

Reviewers must be able to determine whether a harness capability has an
explicit contract, failure mode, event output, and traceability chain.

### UR-005: Business Owner Alignment

Business owners must be able to see how business goals, workflows, acceptance
criteria, and risks map into Agent Harness capabilities and evaluator checks.

### UR-006: Enterprise Environment Integration

Platform engineers must be able to identify which tools, APIs, databases,
knowledge sources, permission systems, and observability systems the Agent
Harness must integrate with.

## Functional Requirements

### FR-001: Project Charter

The repository must define its purpose, non-goals, reference methodology, and
agent working rules in project-owned documentation.

### FR-002: Agile Requirement Traceability

Every product requirement must be declared in this PRD with a stable `FR-XXX`
identifier before implementation work begins.

### FR-003: Epic and Story Decomposition

Every functional requirement selected for implementation must be decomposed in
an epic document, and each epic must list the stories that implement it.

### FR-004: Story Implementation Planning

Every story must include a concrete implementation plan before code is changed
for that story.

### FR-005: Commit and CI Gate Traceability

Every code change must bind back to at least one `FR-XXX` requirement and one
`STORY-XXX` story. CI must reject changes when documentation, code, and commit
metadata are inconsistent.

### FR-006: System Architecture

The project must maintain an architecture document describing the major
components, boundaries, and quality gates for the harness-training system.

### FR-007: Main and Work Branch Workflow

The repository must use `main` as the integration branch and named work item
branches as development branches. Work is performed on an allowed
`<type>/<description>` branch, validated by gates, and then merged into `main`.

### FR-008: Work Branch Naming

Every development branch must use the `<type>/<description>` format. The type
must be one of the allowed issue categories, and the description must identify
the work being changed, for example `feat/branch-naming-rules`,
`docs/prd-rules`, or `ci/delete-merged-branches`.

Bare category names such as `feat` or `docs` are not allowed for implementation
work.

### FR-009: PRD Requirement Classes

The PRD must define and preserve the project requirement classes beyond
functional requirements, and CI must reject PRDs that omit required classes.

### FR-010: Delete Merged Feature Branches

After a pull request from an allowed `<type>/<description>` branch to `main` is
merged successfully, CI must automatically delete the merged remote work branch.
The workflow must not delete `main` or any branch that does not match the
work branch naming rule.

### FR-011: Issue Category Taxonomy

The project must define a controlled issue category taxonomy and use it for
branch naming, CI branch validation, and merged branch cleanup.

Allowed issue categories:

- `feat`: new product behavior or user-facing capability.
- `fix`: defect correction.
- `docs`: documentation-only changes.
- `test`: test coverage, test data, and test infrastructure.
- `refactor`: behavior-preserving code or structure changes.
- `ci`: CI/CD, automation, and release workflow changes.
- `chore`: maintenance that does not change product behavior.
- `perf`: performance improvements.
- `security`: security hardening and vulnerability remediation.

### FR-012: Commit Issue Binding

Every commit must bind to an issue. CI must reject commits whose messages do not
include either a GitHub issue reference such as `#123` or a stable issue token
such as `ISSUE-123`.

### FR-013: Harness Capability Catalog

The project must maintain a catalog of harness capabilities derived from the
agent harness reference model. The catalog must group capabilities by product
area and identify their contracts, state, events, and failure behavior.

### FR-014: Worker Contract Model

The project must define a reusable worker contract model for harness
capabilities, including function IDs, inputs, outputs, errors, timeouts,
persisted state, emitted events, and replaceability boundaries.

### FR-015: Turn Intake and Orchestration

The harness runtime plan must include turn request intake, persistence, durable
turn state, turn stepping, assistant streaming, tool execution, steering, and
teardown.

### FR-016: Provider, Credential, and Model Capability Layer

The harness runtime plan must include provider routing, credential resolution,
model capability lookup, streaming support, context window awareness, and usage
recording.

### FR-017: Skill and Prompt Assembly

The harness runtime plan must include skill discovery, skill loading,
function-shape documentation, mode/identity prompt assembly, working directory
context, and prompt override behavior.

### FR-018: Policy and Approval Gates

The harness runtime plan must include policy checks before tool execution,
allow/deny/needs-approval outcomes, fail-closed behavior, human approval
resolution, and resumed execution after approval.

### FR-019: Budget, Hooks, and Side Effects

The harness runtime plan must include budget checking, spend recording, alerting,
before-call hooks, after-call hooks, redaction hooks, logging hooks, and custom
side effects.

### FR-020: Session, Memory, and Context Compaction

The harness runtime plan must include branching session storage, resumable
state, per-session queues, context window monitoring, and context compaction.

### FR-021: Events, Streaming, and Tracing

The harness runtime plan must include assistant token streaming, UI event
streams, run/session/message/function identifiers, and one trace that spans the
whole turn.

### FR-022: Harness Training Evaluator

The product must define a deterministic evaluator that scores harness designs
and implementation artifacts against the capability catalog, contract coverage,
failure semantics, and observability requirements.

### FR-023: Product Boundary Definition

The product must explicitly define itself as an enterprise business Agent
Harness delivery system, not as a business Agent, generic Agent production
platform, language model trainer, or prompt manager.

### FR-024: Business Context Intake

The product must accept and structure business goals, business PRDs, workflows,
roles, risks, constraints, success metrics, and acceptance criteria as first
class inputs to harness delivery.

### FR-025: Business Environment Inventory

The product must capture the business environment required by the target Agent,
including tools, APIs, databases, data sources, knowledge bases, permission
systems, approval processes, secrets, logging, monitoring, and audit systems.

### FR-026: Business Agent Harness Blueprint

The product must transform business context and environment inventory into a
Business Agent Harness blueprint covering Agent purpose, tool contracts,
knowledge access, policy, approval, budget, session, events, tracing, and
evaluation.

### FR-027: Enterprise Delivery Package

The product must produce a delivery package for each target business Agent
Harness, including PRD traceability, architecture, worker contracts,
implementation plan, environment integration plan, evaluator plan, CI evidence,
and run evidence.

### FR-028: Business Evaluation Mapping

The product must map business success criteria and acceptance criteria into
deterministic evaluator checks, regression fixtures, and run evidence so that
harness training optimizes business-relevant outcomes.

## Non-Functional Requirements

### NFR-001: Auditability

The repository must preserve enough structured evidence for reviewers to audit
why a change exists and whether it followed the agile process.

### NFR-002: Maintainability

Gate logic must remain dependency-free and small enough to run locally and in CI
without bootstrapping a separate toolchain.

### NFR-003: Fail-Closed Governance

When CI cannot prove that PRD, epic, story, code, and commit metadata are
consistent, it must reject the change.

### NFR-004: Replaceability

Harness capabilities must be specified so that one implementation can be
replaced without changing neighboring capabilities when the public contract is
preserved.

### NFR-005: Observability

Harness capabilities must emit enough structured events and trace identifiers
for debugging a full turn across workers.

### NFR-006: Recoverability

Durable turn, approval, budget, session, and compaction behavior must be
specified with recovery paths for interrupted or resumed runs.

### NFR-007: Enterprise Readiness

Business Agent Harness delivery must account for auditability, access control,
environment integration risk, operational handoff, and repeatable evaluation.

### NFR-008: Local Secret Hygiene

Local secret files must remain outside version control. The repository must
ignore `.env` and `.env.*`, and CI must reject any tracked local secret file.

## Constraints

- The early quality gate must use only the Python standard library.
- All implementation branches must follow `<type>/<description>` using an
  allowed issue category.
- The sibling `autoresearch` checkout is reference material only and must not be
  modified or submitted as part of this project.
- Local secrets must be stored in ignored files such as `.env` and never
  committed.

## Assumptions and Dependencies

- GitHub Actions is the initial CI environment.
- BMad artifacts may be added later, but the core gate must remain runnable
  without BMad-specific commands.
- The repository uses Markdown documents as the source of product truth until a
  richer issue tracker is introduced.
- The initial runtime decomposition can be expressed as documents before code
  exists.
- The business Agent owner supplies or approves the business PRD and environment
  inventory.

## Out of Scope

- Training language models.
- Tuning the sibling `autoresearch` benchmark.
- Building a large harness runtime before the agile planning and gate spine is
  stable.
- Selecting iii itself as a mandatory runtime substrate. The reference article
  informs decomposition, but this project may implement equivalent contracts
  with different technology.
- Owning the business outcome directly. The product builds and trains the
  harness that serves a business Agent; the business team remains accountable
  for business goals and domain correctness.

## Success Metrics

- CI can validate the PRD -> Epic -> Story -> Code chain without external
  dependencies.
- A reviewer can identify why a code change exists from IDs in the commit and
  source file.
- No code is merged without a corresponding story implementation plan.
- CI rejects unsupported branch flows and malformed work branch names when
  running in GitHub Actions.
- CI rejects PRDs that omit required requirement classes.
- CI deletes merged allowed work branches after successful
  merge.
- CI rejects commits that are not bound to an issue.
- Each planned harness capability maps to at least one Epic and Story.
- Harness runtime stories specify contract, state, failure, and observability
  expectations before implementation.
- Every business Agent delivery package maps business goals and business
  environment inputs to harness capabilities and evaluator checks.
- Local `.env` files are ignored and never tracked.
