# Business Evaluation Mapping

Business evaluation mapping is the fourth delivery artifact for an enterprise
business Agent Harness. It follows business context intake, business
environment inventory, and the Business Agent Harness Blueprint, and supports
`FR-028` / `STORY-024`.

Create one evaluation mapping per target business Agent. The mapping turns
business success criteria and acceptance criteria into evaluator checks,
regression fixtures, run evidence, failure classes, and keep/discard/crash
decision evidence.

Use [business-evaluation-mapping-template.md](business-evaluation-mapping-template.md)
to capture:

- source inputs from PRD, story, spec, intake, inventory, blueprint, and worker
  contracts
- coverage from each business success criterion and acceptance criterion to a
  deterministic check or explicit manual review evidence
- regression fixtures, scenarios, sandboxes, mocks, and validation commands
- failure classes for incorrect tool use, missing approval, policy violation,
  unsupported data access, budget overrun, poor task outcome, and crash cases
- run evidence and keep/discard/crash decision evidence

The completed mapping is ready only when reviewers can see how each business
criterion will be evaluated without relying on chat history. Code agents may
execute bounded work packages against the mapping, but they must not redefine
business success criteria, acceptance criteria, policy, approval, access, or
budget expectations without traceable owner approval.
