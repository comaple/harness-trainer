---
id: SPEC-governed-harness-development
companions:
  - source-extract.md
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the
> complete, preservation-validated contract for what to build, test, and
> validate for issue #3. Source documents remain product truth; this SPEC
> distills the load-bearing contract for downstream execution.

# Governed Harness Development

## Why

`harness-trainer` needs governed harness development because enterprise Agent
Harness changes must be planned, traceable, reviewed, and gated before
integration. Without this governance spine, harness changes can bypass business
intent, lose Story context, or merge without evidence that requirements and code
remain consistent.

## Capabilities

- id: CAP-1
  intent: Maintainers can require every harness change to start from a declared
    product requirement before implementation begins.
  success: A change without a PRD requirement ID is rejected by the local or CI
    gate before merge.

- id: CAP-2
  intent: Maintainers can require each selected requirement to be decomposed
    into an Epic and at least one Story with an implementation plan.
  success: A requirement referenced by implementation work but not covered by a
    Story fails traceability validation.

- id: CAP-3
  intent: Reviewers can trace each implementation commit back to a GitHub issue,
    requirement ID, and Story ID.
  success: CI rejects checked commits whose messages omit an issue reference,
    valid requirement ID, or valid Story ID.

- id: CAP-4
  intent: CI can block unplanned or inconsistent harness changes before they
    enter `main`.
  success: The quality gate fails when documentation, code markers, commit
    metadata, or branch workflow evidence are inconsistent.

## Constraints

- Governance must preserve the chain: issue -> PRD requirement -> Epic -> Story
  -> implementation -> commit -> CI evidence.
- Implementation commits must reference an issue and the relevant requirement
  and Story IDs.
- CI must fail closed when it cannot prove traceability.
- Governance must apply before integration into `main`.
- Local secret files are outside the governance artifact set and must remain
  untracked.

## Non-goals

- This SPEC does not define the full Agent Harness runtime.
- This SPEC does not train language models or tune the sibling `autoresearch`
  benchmark.
- This SPEC does not replace human product ownership for business goals or
  domain correctness.

## Success signal

A harness change is only integrable when a reviewer can follow the complete
chain from issue and PRD requirement through Epic, Story, commit metadata, source
traceability, and passing CI gate without relying on unstated context.

## Assumptions

- `integration` means merge or direct push into `main`.
- GitHub issue references such as `#3` are the preferred issue binding format.
- The current governance spine is implemented through Markdown artifacts and
  `scripts/ci_check.py`.

## Open Questions

- Should human review approval become a required gate in addition to CI?
- Should requirement-to-issue linkage be enforced bidirectionally by API rather
  than commit-message convention alone?

