from pathlib import Path
import sys
import unittest


SCRIPT_DIR = (
    Path(__file__).resolve().parents[1]
    / "plugins"
    / "ai-fingerprint-mitigator"
    / "skills"
    / "ai-fingerprint-mitigator"
    / "scripts"
)
sys.path.insert(0, str(SCRIPT_DIR))

import prose_audit  # noqa: E402


class ProseAuditTests(unittest.TestCase):
    def test_unicode_word_count_and_phrase_scope(self):
        result = prose_audit.audit("Ação, café e coração.")

        self.assertEqual(result["metrics"]["words"], 4)
        self.assertIn("Stock-phrase checks are English-specific", result["note"])

    def test_phrase_hits_have_bounded_locations_and_keep_json_shape(self):
        result = prose_audit.audit(
            "Opening line.\nIt is important to note this point."
        )

        self.assertEqual(
            set(result),
            {
                "note",
                "metrics",
                "stock_phrase_hits",
                "repeated_sentence_openers",
                "signals",
            },
        )
        hit = result["stock_phrase_hits"]["canned_intro"][0]
        self.assertTrue(hit.startswith("line 2: "))
        self.assertLessEqual(len(hit.removeprefix("line 2: ")), 160)
        self.assertEqual(result["signals"], ["stock_phrase_patterns"])


if __name__ == "__main__":
    unittest.main()
