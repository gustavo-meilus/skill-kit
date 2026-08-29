# Plugin authoring

A Skill Kit plugin earns its place by solving one recurring job well.

Before adding one:

1. Define one clear job, trigger, and non-use condition.
2. Keep the skill focused; move detailed material into references loaded only when needed.
3. Use deterministic scripts or hooks only when instructions alone cannot provide the needed guarantee.
4. Bound authority and state what the plugin cannot claim.
5. Document host-specific behavior instead of assuming feature parity.
6. Add completion criteria and the smallest relevant verification.
7. Add the plugin to both marketplace manifests and keep public display metadata consistent.
8. Have a maintainer review the package for scope, evidence, and user-facing truth.

Use the existing `plugins/<plugin>/` layout as the template. Do not add shared frameworks, boilerplate, or always-loaded context without a present need.
