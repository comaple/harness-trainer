# Source Extract: Skill and Prompt Assembly

## Issue

Source: GitHub issue #50

- Create the BMad SPEC for `STORY-013 / FR-017` skill and prompt assembly.
- Scope includes skill discovery, skill loading, skill body retrieval,
  per-function skill metadata before tool calls, deterministic prompt assembly
  from mode, identity, workspace context, skills, and overrides, prompt
  override precedence, provenance, validation, events, traces, and failure
  behavior for missing or malformed skill metadata.
- Acceptance requires prompt assembly to be deterministic from declared inputs,
  missing required skills or malformed metadata to fail closed with UI-safe
  diagnostics, and mapping to `HC-004`, `FR-017`, `STORY-013`, and `EPIC-002`.

## PRD

Source: `docs/prd.md`

### FR-017: Skill and Prompt Assembly

The harness runtime plan must include skill discovery, skill loading,
function-shape documentation, mode/identity prompt assembly, working directory
context, and prompt override behavior.

### FR-014: Worker Contract Model

The project must define a reusable worker contract model for harness
capabilities, including function IDs, inputs, outputs, errors, timeouts,
persisted state, emitted events, versioning expectations, and replaceability
boundaries. The contract must make it possible to compare two implementations
of the same capability against the same inputs, outputs, failures, and traces.

## Epic

Source: `docs/epics/EPIC-002-agent-harness-capabilities.md`

- `EPIC-002` decomposes the target agent harness into replaceable, testable
  capabilities.
- `FR-017` is part of EPIC-002.
- `STORY-013` plans skill and prompt assembly.
- Acceptance requires each capability to identify its public contract, state
  boundary, failure behavior, and observability evidence.
- Replacement-sensitive capabilities must identify evaluator evidence and
  replacement safety criteria before implementation begins.
- The decomposition must not require adopting any specific external harness
  framework.

## Story

Source: `docs/stories/STORY-013-skill-prompt-assembly.md`

- As a harness designer, skills and prompt assembly must be explicit
  capabilities so tool instructions and system prompts can evolve without
  rewriting the turn runtime.
- Functional requirements: `FR-017` and `FR-014`.
- Implementation plan:
  - Specify skill discovery and skill body retrieval.
  - Specify per-function skill metadata required before tool calls.
  - Specify default prompt assembly from mode, identity, workspace, and skills.
  - Specify prompt override behavior.
  - Define validation checks for missing or malformed skill metadata.
- Acceptance:
  - Skills document request shape, errors, and usage notes.
  - Prompt assembly is deterministic from declared inputs.
  - Prompt override behavior preserves tool discovery when required.

## Capability Catalog

Source: `docs/harness/capability-catalog.md`

### HC-004: Skill and Prompt Assembly

- Intent: Discover applicable skills, load their instructions, and assemble the
  working prompt from mode, identity, workspace context, skills, and overrides.
- Public contract surface: `discover_skills`, `load_skill_context`, and
  `assemble_prompt_context` operations.
- State ownership: Owns resolved skill list, prompt assembly inputs, prompt
  provenance, and applied override metadata.
- Emitted events: `skill.discovered`, `skill.loaded`, `prompt.assembled`, and
  `prompt.override_applied`.
- Failure behavior: Missing required skills or invalid override instructions
  fail closed; optional skill failures are recorded without blocking unless the
  story requires them.
- Replacement boundary: A replacement must preserve skill selection rules,
  prompt ordering rules, override precedence, and provenance output.
- Evaluator evidence: Fixtures for no-skill, single-skill, multi-skill,
  missing required skill, and prompt-override cases.
- Trace evidence: Prompt assembly spans listing skill IDs, source paths, and
  applied override identifiers.

## Worker Contract

Source: `docs/harness/worker-contract.md`

- Worker contracts are technology-neutral callable or event-triggered units at
  capability boundaries.
- Required fields: function ID, capability ID, trigger name, input shape,
  output shape, recoverable errors, fail-closed errors, timeout, idempotency,
  state reads, state writes, emitted events, trace tags, version expectations,
  and fixture expectations.
- Input shape must describe accepted fields, required fields, optional fields,
  and validation rules.
- Output shape must include enough status for neighboring capabilities to
  continue without implementation internals.
- Fail-closed errors must stop before side effects, tool execution, credential
  exposure, or irreversible state mutation, and must define required event or
  trace evidence.
- Trace tags must not include secrets or raw business data unless explicitly
  approved by a future security requirement.
- Replacement comparison requires accepted input shape, compatible output
  shape, equivalent failure behavior, emitted event compatibility, state
  boundary compatibility, trace compatibility, and fixture compatibility.

## Neighboring Spec

Source: `docs/specs/spec-turn-intake-orchestration/SPEC.md`

- Turn orchestration advances through model streaming, function execution,
  approval waiting, steering, teardown, completed, stopped, and failed states.
- UI and automation consumers observe lifecycle progress through events with
  turn ID, state, step cursor, timestamp, trace ID, and UI-safe status or error
  metadata.
- Turn orchestration does not implement skill and prompt assembly; the
  neighboring capability owns its own contract.

## Wrapper-Only Content

- GitHub issue URLs, user avatar metadata, API node IDs, and timestamps are
  process metadata and are not part of the product contract.
