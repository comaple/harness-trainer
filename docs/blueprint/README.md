# Business Agent Harness Blueprint

The Business Agent Harness Blueprint is the third delivery artifact for an
enterprise business Agent Harness. It follows business context intake and
business environment inventory, and supports `FR-026` / `STORY-022`.

Create one blueprint per target business Agent. The blueprint turns approved
business intent and confirmed environment items into the harness design that
can drive worker contracts, implementation stories, evaluator expectations,
and bounded code-agent work packages.

Use [business-agent-harness-template.md](business-agent-harness-template.md) to
capture:

- Agent purpose, in-scope user tasks, out-of-scope tasks, and source inputs
- mappings from business goals and requirements to harness capabilities
- mappings from environment items to worker contract candidates and policy
  rules
- knowledge access, approval flow, budget constraints, session and memory
  rules, events, tracing, and evaluator expectations
- risks, missing dependencies, implementation story slices, allowed edit
  surfaces, validation commands, and evidence requirements

The completed blueprint is ready only when it can produce bounded
implementation stories without relying on chat history. Code agents may execute
those stories, but they must not redefine business goals, environment access
boundaries, policy decisions, or acceptance criteria without traceable owner
approval.
