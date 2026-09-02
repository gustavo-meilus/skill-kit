## 1. Package and workflow boundary

- [x] 1.1 Add Codex and Claude manifests for `relentless-web-researcher` using the existing host-package conventions; verify the manifests parse and point to the bundled skills directory.
- [x] 1.2 Add the retrieved-content non-authority rule to the research skill; verify the skill structural validator still passes.

## 2. Structural verification

- [x] 2.1 Add a focused, dependency-free test that resolves checked-in marketplace entries and asserts their required host manifest and `skills/` directory; verify the test fails for an intentionally incomplete fixture or isolated assertion and passes for the repository state.
- [x] 2.2 Run the focused marketplace check and the existing test suite; verify both exit successfully without adding a test framework or runtime dependency.

## 3. Host evidence

- [x] 3.1 Document the reproducible Codex marketplace add, install, discovery, and uninstall procedure; verify no documentation claims host success without an observed record.
- [x] 3.2 When a clean Codex environment is available, perform the documented flow and record the exact version and observed result; otherwise retain the host-support status as pending.
