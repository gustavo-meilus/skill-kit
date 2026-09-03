from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "plugins" / "llm-knowledge-base-maintainer"
SKILL = PACKAGE / "skills" / "llm-knowledge-base-maintainer"


class KnowledgeBaseMaintainerPackageTests(unittest.TestCase):
    def test_package_and_default_layout_are_complete(self) -> None:
        for path in (PACKAGE / "plugin.json", PACKAGE / ".claude-plugin/plugin.json", PACKAGE / ".codex-plugin/plugin.json"):
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["skills"], "./skills/")

        layout = (SKILL / "references" / "DEFAULT_LAYOUT.md").read_text(encoding="utf-8")
        for required in ("id:", "title:", "summary:", "version:", "updated:", "provenance:", "llms.txt", "manifest.jsonl"):
            self.assertIn(required, layout)

    def test_invocation_boundary_is_discriminating(self) -> None:
        frontmatter = (SKILL / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
        self.assertIn("knowledge-base creation", frontmatter)
        self.assertIn("ordinary prose", frontmatter)
        self.assertIn("hosted retrieval infrastructure", frontmatter)


if __name__ == "__main__":
    unittest.main()
