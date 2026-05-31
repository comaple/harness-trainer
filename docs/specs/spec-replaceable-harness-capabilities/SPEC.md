---
id: SPEC-replaceable-harness-capabilities
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #4. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Replaceable Harness Capabilities

## Why

`harness-trainer` needs replaceable harness capabilities because enterprise
Agent Harnesses must improve without becoming monolithic runtimes. Teams need a
way to compare, replace, and retrain individual harness responsibilities while
preserving neighboring contracts, business intent, traceability, and evaluator
evidence.

## Capabilities

- id: CAP-1
  intent: Harness architects can describe each harness responsibility as a
    named capability with an explicit replacement boundary.
  success: Every planned capability has a catalog entry that names its product
    area, contract surface, state ownership, events, failure behavior,
    replacement boundary, and evaluator evidence.

- id: CAP-2
  intent: Harness developers can define worker contracts that allow alternative
    implementations of the same capability to be compared.
  success: Two implementations of a capability can be evaluated against the
    same function IDs, inputs, outputs, errors, timeouts, state reads/writes,
    emitted events, trace tags, and version expectations.

- id: CAP-3
  intent: Reviewers can determine whether replacing a capability is safe before
    it enters implementation or integration.
  success: A replacement claim is reviewable through contract compatibility,
    state-boundary clarity, failure-mode equivalence, observability evidence,
    and regression evaluator results.

- id: CAP-4
  intent: The harness training evaluator can score replacement safety as a
    first-class outcome.
  success: The evaluator reports whether a capability can be swapped while
    preserving its declared contract, failure semantics, trace evidence, and
    regression fixtures.

## Constraints

- Replaceability must be designed at the capability boundary, not retrofitted
  after runtime implementation.
- The project must not treat a list of runtime areas as sufficient; each
  capability needs contract, state, failure, event, replacement, and evaluator
  evidence.
- The capability catalog and worker contract model must stay technology-neutral
  until an implementation story requires a concrete runtime choice.
- Implementation work for issue #4 must trace to `BR-002` and the relevant
  `STORY-XXX` IDs.
- Replacement safety must be evaluated without rewriting neighboring
  capabilities when the public contract is preserved.

## Non-goals

- This SPEC does not choose a mandatory external harness runtime.
- This SPEC does not implement the full harness runtime.
- This SPEC does not define business-domain behavior for a specific Agent.
- This SPEC does not train or tune language models.

## Success signal

A reviewer can inspect a planned harness capability and decide whether it is
replaceable by reading its catalog row, worker contract, state boundary, failure
semantics, emitted events, trace evidence, and evaluator checks without relying
on unstated runtime assumptions.

## Assumptions

- `capability` means a replaceable harness responsibility, not a business Agent
  feature.
- Replacement safety can initially be specified and evaluated through
  documentation artifacts before runtime code exists.
- `EPIC-002` and `STORY-009` through `STORY-018` remain the active
  decomposition path for `BR-002`.

## Open Questions

- Should capability contracts use a machine-readable schema before runtime code
  starts?
- Should replacement safety require golden fixtures for every capability or
  only for capabilities with side effects, policy, state, or external calls?

