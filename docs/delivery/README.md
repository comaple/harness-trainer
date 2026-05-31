# Enterprise Delivery Package

The Enterprise Delivery Package is the final delivery artifact for one target
business Agent Harness. It supports `FR-027` / `STORY-023` and packages the
evidence needed for enterprise review, handoff, and harness-training decisions.

Create one delivery package per target business Agent Harness. The package
does not replace upstream artifacts. It references the approved source of truth
for each required artifact and records the evidence needed to audit the path
from business goal to implementation and run evidence.

Use [enterprise-delivery-package-template.md](enterprise-delivery-package-template.md)
to capture:

- source inputs from the business PRD, intake, environment inventory,
  blueprint, worker contracts, implementation stories, specs, and evaluation
  mapping
- PRD traceability from business goals and acceptance criteria to FR, story,
  issue, contract, evaluator, and run evidence
- architecture, worker contract, implementation plan, and environment
  integration evidence
- evaluator plan, CI evidence, run evidence, and keep/discard/crash decisions
- operational handoff owners, runbooks, support boundaries, rollback
  expectations, and open risks

The package is ready only when an enterprise reviewer can inspect a single
document and understand what was approved, what was built, what was tested,
what evidence supports the decision, and what remains open. It must not contain
secret values, production credentials, or unreviewed assumptions presented as
confirmed facts.
