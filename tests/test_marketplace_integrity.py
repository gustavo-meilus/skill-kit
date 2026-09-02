from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def assert_package(name: str, package: Path, manifest_name: str) -> None:
    manifest = package / manifest_name
    if not manifest.is_file():
        raise AssertionError(f"{name}: missing {manifest}")
    if not (package / "skills").is_dir():
        raise AssertionError(f"{name}: missing {package / 'skills'}")
    skills = json.loads(manifest.read_text(encoding="utf-8")).get("skills")
    if not isinstance(skills, str) or not (package / skills).is_dir():
        raise AssertionError(f"{name}: manifest skills path does not resolve")


class MarketplaceIntegrityTests(unittest.TestCase):
    def test_checked_in_marketplaces_resolve_packages(self) -> None:
        catalogs = (
            (ROOT / ".agents/plugins/marketplace.json", ".codex-plugin/plugin.json", lambda entry: entry["source"]["path"]),
            (ROOT / ".claude-plugin/marketplace.json", ".claude-plugin/plugin.json", lambda entry: entry["source"]),
        )
        for catalog, manifest_name, source_of in catalogs:
            for entry in json.loads(catalog.read_text(encoding="utf-8"))["plugins"]:
                assert_package(entry["name"], (ROOT / source_of(entry)).resolve(), manifest_name)

    def test_incomplete_package_identifies_missing_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            with self.assertRaisesRegex(AssertionError, r"research: missing .*\\.codex-plugin"):
                assert_package("research", Path(temporary_directory), ".codex-plugin/plugin.json")


if __name__ == "__main__":
    unittest.main()
