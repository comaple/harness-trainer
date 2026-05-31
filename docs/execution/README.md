# Code Agent Execution Package

The Code Agent Execution Package is the bounded work artifact for programmers
and code agents. It supports `FR-029` / `STORY-026` and turns approved business
intent, specs, worker contracts, evaluator expectations, and review evidence
into one implementation-ready package.

Create one execution package per bounded implementation task. The package
must be prepared before implementation starts, and reviewers should update it
with implementation evidence, test evidence, evaluator output, and final review
decision before the work is kept, revised, discarded, retried, or handed off.

Use [code-agent-execution-package-template.md](code-agent-execution-package-template.md)
to capture:

- issue, epic, `FR-XXX`, `STORY-XXX`, target business Agent Harness, and owner
- source spec, worker contract, blueprint slice, evaluation mapping, and
  enterprise delivery package references
- allowed edit surface, disallowed changes, required commands, evaluator
  checks, fixtures, and expected pass signals
- implementation evidence, test evidence, evaluator output, run evidence,
  event evidence, trace evidence, assumptions, deviations, and open risks
- review outcome: keep, revise, discard, retry, or handoff

The package is ready only when a programmer or code agent can implement the
task without redefining business goals, PRD scope, environment access,
policy, approval, budget, evaluator criteria, or delivery readiness. It must
not contain secret values, credentials, private keys, or unsafe production
data.
