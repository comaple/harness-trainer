---
id: SPEC-business-environment-inventory
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #26. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Business Environment Inventory

## Why

`harness-trainer` needs a business environment inventory because enterprise
Agent Harness delivery cannot move from business intent to blueprint, worker
contracts, or implementation until the target Agent's operating environment is
known. Delivery teams need a structured artifact that records the tools, APIs,
databases, data sources, knowledge bases, permissions, approvals, secrets,
logging, monitoring, and audit systems that the harness must integrate with,
protect, observe, and evaluate.

## Capabilities

- id: CAP-1
  intent: Platform engineers can document the target business Agent's external
    operating environment before blueprint work begins.
  success: The inventory captures tools, APIs, databases, data sources,
    knowledge bases, permission systems, approval processes, secrets, logging,
    monitoring, and audit systems as named environment items.

- id: CAP-2
  intent: Harness architects can determine integration boundaries for each
    environment item.
  success: Each item records owner, access method, access boundary,
    credential or secret handling need, and the expected harness capability
    area it affects.

- id: CAP-3
  intent: Delivery teams can identify governance and safety requirements before
    code-agent or programmer implementation starts.
  success: Each item records permission, approval, audit, privacy, operational,
    or security constraints that can shape policy rules, review gates, or
    worker contracts.

- id: CAP-4
  intent: Evaluator designers can plan how environment integrations will be
    tested without depending on unsafe production access.
  success: Each item records test strategy, fixture or sandbox expectation,
    observability evidence, and failure or fallback behavior.

- id: CAP-5
  intent: Blueprint authors can transform environment evidence into the
    Business Agent Harness blueprint.
  success: Inventory items can be mapped to tool contracts, knowledge access,
    policy, approval, budget, session, events, tracing, and evaluation sections
    of `FR-026`.

## Constraints

- Inventory must follow business context intake for the same target Agent and
  must precede Business Agent Harness Blueprint work.
- Inventory must separate confirmed environment facts from assumptions, open
  questions, and access requests.
- Inventory must not expose secret values in repository files, issues, pull
  requests, logs, or CI output.
- Inventory must record access boundaries before implementation workers or code
  agents are given environment-related work.
- Inventory must be implementation-neutral: it may describe integration needs
  and constraints, but it must not force a specific runtime, provider, database
  client, or SDK unless the business environment already requires one.
- Inventory artifacts must be usable by downstream specs, stories, contracts,
  evaluators, and delivery packages without relying on chat history.

## Non-goals

- This SPEC does not implement environment integrations.
- This SPEC does not grant access to tools, APIs, databases, secrets, or
  production systems.
- This SPEC does not replace enterprise security, compliance, or data-governance
  approval processes.
- This SPEC does not produce the final Harness Blueprint; that belongs to
  `FR-026` and `STORY-022`.
- This SPEC does not make programmers or code agents owners of business
  environment access decisions.

## Success signal

A harness delivery lead can take a completed inventory artifact and determine
which environment items are confirmed, which are blocked by missing access or
owner confirmation, how each item maps to harness capability areas, and whether
the target business Agent is ready for `FR-026` blueprint, worker contract,
policy, evaluator, and bounded implementation work.

## Assumptions

- The business owner or platform owner can identify accountable owners for
  environment items.
- Initial inventory can be document-based before a UI, API, or machine-readable
  schema exists.
- Production secret values are never needed in the inventory; only secret
  existence, owner, storage location class, rotation expectation, and access
  process are needed.

## Open Questions

- Which inventory fields should be hard blockers for blueprint generation, and
  which should remain reviewer warnings?
- Should the first implementation be Markdown-only, or should it also define a
  machine-readable schema for later automation?
