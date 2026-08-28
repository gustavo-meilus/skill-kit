## More With Less engineering policy

For project development, debugging, refactoring, architecture, specification, dependencies, tooling, agents, hooks, MCP, automation, and verification:

- For non-trivial work, load and follow `$more-with-less` before choosing the implementation approach.
- Build the minimum sufficient solution that satisfies the real requirements and preserves existing guarantees.
- Understand the relevant code and behavior before simplifying; fix root causes rather than duplicating symptom patches.
- Prefer deletion/reuse, existing project mechanisms, standard/native capabilities, installed dependencies, and deterministic checks before custom machinery.
- Keep context, tools, permissions, state, files, abstractions, agents, handoffs, and orchestration as small as practical.
- Use one agent by default. Add specialists/reviewers only for concrete independence, isolation, expertise, or parallelism needs.
- Make specification and verification proportional to uncertainty, consequence, and coordination.
- Never simplify away required correctness, security, authorization, data integrity, accessibility, operability, observability, acceptance criteria, or rollback/recovery safeguards.
- Before completion, run the project's authoritative verification and state the evidence actually obtained.
- After implementation, inspect the diff for unrelated changes and remove obsolete or unnecessary complexity.
