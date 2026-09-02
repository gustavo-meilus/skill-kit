import json
from pathlib import Path
import unittest


MANIFEST = Path(__file__).resolve().parents[1] / "hooks" / "hooks.json"


class HookManifestTests(unittest.TestCase):
    def test_windows_commands_use_powershell_plugin_root(self) -> None:
        hooks = json.loads(MANIFEST.read_text(encoding="utf-8"))["hooks"]
        for event in ("SessionStart", "Stop"):
            command = hooks[event][0]["hooks"][0]["commandWindows"]
            self.assertIn("$env:PLUGIN_ROOT", command)
            self.assertNotIn("%PLUGIN_ROOT%", command)


if __name__ == "__main__":
    unittest.main()
