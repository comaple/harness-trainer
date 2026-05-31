# Source Extract: Harness Training Evaluator

## Issue

Source: GitHub issue #60

- Create the BMad SPEC for `STORY-018 / FR-022` harness training evaluator.
- Scope includes deterministic evaluator inputs, outputs, score dimensions,
  missing-coverage reporting, contract completeness, replacement safety,
  failure semantics, state boundaries, policy/approval safety, observability,
  traceability, passing/failing/replacement fixtures, evaluation run evidence,
  artifact lists, result status, score thresholds, and CI gate behavior.
- Acceptance requires deterministic criteria traceable to PRD, epic, story,
  catalog, and worker contracts; missing coverage and replacement-safety
  failures must be explainable; CI must accept or reject a harness contract
  package from evaluator output; mapping must include `HC-009`, `FR-022`,
  `STORY-018`, and `EPIC-002`.

## PRD

Source: `docs/prd.md`

### FR-022: Harness Training Evaluator

The product must define a deterministic evaluator that scores harness designs
and implementation artifacts against the capability catalog, contract coverage,
failure semantics, observability requirements, and replacement safety. The
evaluator must identify whether a capability can be swapped while preserving
its declared contract and regression evidence.

## Epic

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

- `EPIC-002` decomposes the target agent harness into replaceable, testable
  capabilities.
- `STORY-018` plans the harness training evaluator.
- Acceptance requires each capability to identify its public contract, state
  boundary, failure behavior, and observability evidence.
- Replacement-sensitive capabilities must identify evaluator evidence and
  replacement safety criteria before implementation begins.
- The decomposition must not require adopting any specific external harness
  framework.

## Story

Source: `docs/stories/STORY-018-harness-training-evaluator.md`

- As a harness trainer, a deterministic evaluator is needed for harness design
  and implementation artifacts so agents can iteratively improve the harness
  without relying on subjective review alone.
- Functional requirements: `FR-022`, `FR-013`, and `FR-014`.
- Evaluator dimensions:
  - capability coverage
  - contract completeness
  - replacement safety
  - failure semantics
  - state boundaries
  - policy and approval safety
  - observability
  - traceability to PRD/Epic/Story
- Replacement safety checks:
  - contract compatibility
  - state-boundary compatibility
  - failure-mode equivalence
  - event compatibility
  - trace compatibility
  - regression fixture result
- Implementation plan includes a dependency-free evaluator script, passing and
  failing harness design fixtures, accepted and rejected replacement-candidate
  fixtures, CI checks, `harness_score`, and a replacement safety report.
- Acceptance requires local execution without external dependencies, numeric
  score, missing coverage report, CI failure on coverage regressions,
  first-class replacement safety, replacement rejection for incompatible
  contract/state/failure/event/trace/fixture evidence, reading expectations
  from capability catalog and worker contracts, and referencing
  `docs/specs/spec-replaceable-harness-capabilities/SPEC.md`.

## Capability Catalog

Source: `docs/harness/capability-catalog.md`

### HC-009: Harness Training Evaluator

- Intent: Score harness designs and implementation artifacts against the
  capability catalog, worker contracts, failure semantics, observability, and
  replacement safety.
- Public contract surface: `evaluate_harness_artifacts`,
  `score_capability_coverage`, and `compare_replacement_candidate`
  operations.
- State ownership: Owns evaluator fixture set, scoring dimensions, score
  reports, missing-coverage reports, and replacement-safety reports.
- Emitted events: `evaluation.started`, `evaluation.completed`,
  `evaluation.failed`, and `replacement_candidate.rejected`.
- Failure behavior: Missing required catalog or contract evidence fails the
  evaluation; invalid replacement evidence is reported as rejected, not
  accepted with warnings.
- Replacement boundary: A replacement must preserve score dimensions, required
  evidence checks, rejection semantics, and report structure.
- Evaluator evidence: Passing and failing fixture documents plus accepted and
  rejected replacement-candidate fixtures.
- Trace evidence: Evaluation run ID, artifact list, score dimensions, missing
  coverage list, and replacement-safety result.

### HC-010: Capability Catalog Governance

- Intent: Keep capability definitions, worker contracts, and evaluator checks
  aligned as implementation proceeds.
- Public contract surface: `validate_capability_catalog`,
  `validate_contract_references`, and `validate_evaluator_evidence`
  operations.
- Failure behavior: Missing required fields, broken FR/story references, or
  absent evaluator evidence fail validation before implementation is accepted.

## Worker Contract

Source: `docs/harness/worker-contract.md`

- The replacement must pass current passing fixtures, current failing fixtures,
  and replacement comparison fixtures.
- If fixture results differ, the replacement is rejected until the contract
  version or fixtures are intentionally updated.
- Evaluator scoring expectations include contract completeness, catalog
  linkage, error clarity, state boundary clarity, event and trace evidence,
  replacement safety, and fixture coverage.

## Existing Evaluator Implementation

Source: `harness_eval.py`

- `harness_eval.py` is dependency-free and marked `Traceability: FR-022,
  STORY-018`.
- It reads:
  - `docs/harness/capability-catalog.md`
  - `docs/harness/worker-contract.md`
  - `docs/specs/spec-replaceable-harness-capabilities/SPEC.md`
  - `examples/harness-eval/*.json`
- Required runtime FR coverage spans `FR-013` through `FR-022`.
- Required catalog fields include capability ID/name, product area, owning
  FR/story IDs, intent, public contract surface, state ownership, emitted
  events, failure behavior, replacement boundary, evaluator evidence, and trace
  evidence.
- Required contract fields include function ID, capability ID, trigger name,
  input/output shape, recoverable errors, fail-closed errors, timeout,
  idempotency, state reads/writes, emitted events, trace tags, version
  expectations, and fixture expectations.
- Replacement checks include contract compatibility, state-boundary
  compatibility, failure-mode equivalence, event compatibility, trace
  compatibility, and regression fixture result.
- Output includes `harness_score`, `status`, `missing_coverage`,
  `replacement_safety`, and score dimensions.
- Strict mode exits non-zero unless the score passes; self-test exits non-zero
  when fixtures do not match expected outcomes.

## Fixtures

Source: `examples/harness-eval/`

- `passing-design.json` covers `FR-013` through `FR-022` and expects `pass`.
- `failing-design.json` covers only `FR-013` through `FR-015`, has incomplete
  contract and replacement evidence, and expects `fail`.
- `accepted-replacement.json` has all replacement checks true and expects
  `accepted`.
- `rejected-replacement.json` lacks state-boundary compatibility,
  failure-mode equivalence, and trace compatibility and expects `rejected`.

## Neighboring Specs

Source: `docs/specs/spec-replaceable-harness-capabilities/SPEC.md`

- The harness training evaluator must score replacement safety as a
  first-class outcome.
- Replacement safety can initially be specified and evaluated through
  documentation artifacts before runtime code exists.
- `EPIC-002` and `STORY-009` through `STORY-018` remain the active
  decomposition path for replaceable harness capabilities.

Source: `docs/specs/spec-business-evaluation-mapping/SPEC.md`

- Business evaluation mapping preserves separation between business-specific
  evaluation and generic replacement-safety evaluation.
- Business evaluation mapping does not replace `FR-022` replacement-safety
  evaluation for generic harness capability compatibility.

## Wrapper-Only Content

- GitHub issue URLs, user avatar metadata, API node IDs, timestamps, and local
  command invocation details are process metadata and are not part of the
  product contract.
