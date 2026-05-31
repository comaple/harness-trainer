---
id: SPEC-code-agent-execution-package
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #42. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Code Agent Execution Package

## Why

`harness-trainer` needs a Code Agent Execution Package because programmers and
code agents are execution roles inside enterprise Agent Harness delivery, not
owners of business intent or design boundaries. Each implementation task must
carry enough context, constraints, commands, and evidence requirements to keep
code-agent-assisted work tied to approved business goals, PRD requirements,
stories, specs, worker contracts, evaluator expectations, and review outcomes.

## Capabilities

- id: CAP-1
  intent: Delivery leads can hand programmers or code agents a bounded work
    package.
  success: The package identifies the issue reference, `FR-XXX` requirement
    ID, `STORY-XXX` story ID, epic, source spec or worker contract, target
    business Agent Harness, and owner for the task.

- id: CAP-2
  intent: Implementers can understand the allowed edit surface before changing
    files.
  success: The package lists allowed files, directories, artifacts, commands,
    and explicitly disallowed changes, including business goals, PRD scope,
    environment access boundaries, policy decisions, approval rules, budget
    limits, and evaluator criteria that require owner approval to change.

- id: CAP-3
  intent: Reviewers can see which evaluator and CI evidence is required before
    accepting work.
  success: The package declares required local commands, CI workflows,
    evaluator checks, fixtures or scenarios, expected pass signals, and failure
    classes for the task.

- id: CAP-4
  intent: Code agents can report implementation evidence in a reviewable
    format.
  success: The package defines fields for changed artifacts, implementation
    summary, test evidence, evaluator output, run evidence, event evidence,
    trace evidence, assumptions, deviations, and open risks.

- id: CAP-5
  intent: Delivery reviewers can decide whether assisted work should be kept,
    revised, discarded, retried, or handed off.
  success: The package records reviewer, decision, decision rationale,
    required follow-up, linked PR or commit, and evidence used for keep, revise,
    discard, retry, or handoff.

- id: CAP-6
  intent: Enterprise delivery packages can audit code-agent-assisted work from
    business intent to delivery evidence.
  success: The execution package can be referenced by the Enterprise Delivery
    Package with issue, story, spec or contract, allowed edit surface,
    validation command, evaluator evidence, review evidence, and final decision.

## Constraints

- A package must be scoped to one bounded implementation task.
- A package must preserve traceability to issue, FR, Story, and, when
  applicable, epic, spec, worker contract, blueprint slice, evaluation mapping,
  and enterprise delivery package.
- A package must constrain code agents and programmers from redefining business
  goals, acceptance criteria, policy decisions, approval requirements, access
  boundaries, budget limits, evaluator criteria, or delivery readiness without
  traceable owner approval.
- Required evidence must be explicit before implementation starts.
- Package output must separate confirmed evidence from assumptions, deviations,
  open risks, missing evidence, and reviewer decisions.
- The package must not contain secret values, credentials, private keys, or
  unsafe production data.
- The package must be usable without relying on chat history.

## Non-goals

- This SPEC does not implement the Agent Harness runtime.
- This SPEC does not grant code agents autonomous authority to choose scope.
- This SPEC does not replace business owner, product owner, architect,
  platform, security, or reviewer decisions.
- This SPEC does not redefine PRD requirements, worker contracts, evaluator
  criteria, or delivery readiness.
- This SPEC does not require every implementation task to be executed by a code
  agent; programmers can use the same package.
- This SPEC does not create the final Enterprise Delivery Package; it defines
  an auditable component that the delivery package can reference.

## Success signal

A harness delivery lead can hand a package to a programmer or code agent, and a
reviewer can later audit the resulting work from issue, FR, Story, spec or
contract, allowed edit surface, validation command, evaluator evidence, CI
evidence, implementation evidence, and review decision without relying on chat
history.

## Assumptions

- Initial execution packages can be Markdown-first before a machine-readable
  schema exists.
- Some evidence may link to external systems, but repository artifacts must
  retain enough metadata to audit the decision path.
- The first implementation can provide a reusable template and CI structure
  checks before enforcing package instances for every code change.

## Open Questions

- Which missing package fields should block review, and which should remain
  reviewer warnings?
- Should code-agent execution package instances be required for all future code
  changes or only for enterprise Agent Harness delivery work?
