# Adaptive Engineering Harness

Install this plugin, then copy `templates/engineering-harness.json` to a target repository only when its defaults need changing. The hook uses the repository's canonical `scripts/check`, `scripts/verify`, Make/Just target, package `check`/`verify`, or an explicit `verify_command`.

Claude Code and Copilot CLI load the included read-only roles and hooks. Codex loads the skill and hook; its opt-in role profiles are in `profiles/codex` because Codex plugins do not load custom agent profiles.
