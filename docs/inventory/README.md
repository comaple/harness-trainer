# Business Environment Inventory

The business environment inventory is the second delivery artifact for an
enterprise business Agent Harness. It follows business context intake and
supports `FR-025` / `STORY-021`.

Create one inventory per target business Agent. The inventory records the
environment the harness must integrate with, protect, observe, and evaluate
before blueprint, worker contract, policy, evaluator, or code-agent execution
work begins.

Use [business-environment-template.md](business-environment-template.md) to
capture:

- tools, APIs, databases, data sources, knowledge bases, permissions, approval
  processes, secrets, logs, metrics, monitoring, and audit systems
- owners, access methods, access boundaries, risks, and test strategies
- assumptions, open questions, and access requests
- mappings to worker contracts, policy rules, and harness capability areas

Do not store secret values in this repository. Record only the secret's owner,
storage location class, handling requirement, rotation expectation, and access
request status.

The completed inventory feeds the Business Agent Harness Blueprint. Any
environment item that lacks an owner, access boundary, or test strategy should
be treated as a readiness issue before implementation workers or code agents
touch related integration work.
