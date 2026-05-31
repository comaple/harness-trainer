# Business Context Intake

Business context intake is the first delivery artifact for a target business
Agent Harness. It captures confirmed business intent before the project creates
a Harness Blueprint, worker contracts, evaluator checks, or code-agent execution
packages.

Use [business-context-template.md](business-context-template.md) for each target
business Agent. The template follows
[SPEC-business-context-intake](../specs/spec-business-context-intake/SPEC.md)
and supports `FR-024` / `STORY-020`.

## Usage

1. Create one completed intake artifact per target business Agent.
2. Keep confirmed facts separate from assumptions and open questions.
3. Map each accepted business requirement to harness capability areas.
4. Use the completed intake as the source for the Business Agent Harness
   Blueprint, business evaluator checks, and bounded code-agent execution work.

## Completion Rule

An intake is ready for downstream blueprint work only when business goals,
workflows, roles, constraints, risks, success metrics, acceptance criteria, and
owner-confirmation assumptions are explicitly recorded.
