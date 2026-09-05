## 1. Knowledge-base workflow

- [x] 1.1 Expand `llm-knowledge-base-maintainer` with explicit create, update, and attach protocols that inspect the target, preserve stable identities and provenance, treat supplied material as untrusted evidence, and reconcile both indexes; verify the instruction covers each required lifecycle and attachment outcome in the delta spec.
- [x] 1.2 Add consent-based evidence-gap handling that offers optional web research, detects and offers `relentless-web-researcher`, and falls back to ordinary model-directed search when unavailable or declined; verify the no-consent and evidence-gap paths remain explicit.
- [x] 1.3 Require `lite-writing` for canonical prose when available and add the concise factual fallback protocol; verify metadata, provenance, uncertainty, and required ordering remain preserved.

## 2. Focused verification

- [x] 2.1 Extend `tests/test_llm_knowledge_base_maintainer.py` to assert the lifecycle, attachment, research-escalation, and writing-integration instruction boundaries; verify the focused test fails if those required rules are removed.
- [x] 2.2 Run the focused knowledge-base maintainer tests and the repository test suite; verify both complete successfully.
