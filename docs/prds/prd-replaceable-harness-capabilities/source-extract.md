# Source Extract: Replaceable Harness Capabilities

## Source

- GitHub issue: `#4`
- Title: `BR-002: Replaceable Harness Capabilities`
- Source requirement: `docs/prd.md`

## Extracted Requirement

The product must help teams design and train harnesses as replaceable
capabilities rather than as a monolithic agent framework.

## Acceptance Signal

- `BR-002` must be decomposed into Epic and Story work before implementation.
- Implementation commits must reference issue `#4`, `BR-002`, and the relevant
  Story ID.

## PRD Implications

- The PRD must define what makes a harness capability replaceable.
- The capability catalog must capture replacement boundaries and evaluator
  evidence, not only a list of runtime areas.
- Worker contracts must support comparable implementations of the same
  capability.
- Evaluators must score replacement safety, not just implementation coverage.

