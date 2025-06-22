import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import scripts.overlay_loadtest_analyzer as analyzer  # noqa: E402


def test_parse_log(tmp_path):
    log = tmp_path / "audit.log"
    log.write_text(
        """[2025-06-22 12:00:00] OverlayLoadTestVector started
[2025-06-22 12:00:00] Spawned {'id': '0-0'}
[2025-06-22 12:00:00] Spawned {'id': '0-1'}
[2025-06-22 12:00:00] Cycle 0 cleaned
[2025-06-22 12:00:01] OverlayLoadTestVector finished
"""
    )
    metrics = analyzer.parse_log(log)
    assert metrics == {"cycles": 1, "spawns": 2, "completed": True}


def test_run_outputs_json(tmp_path, capsys):
    log = tmp_path / "audit.log"
    log.write_text("[2025-06-22] Spawned {\"id\": \"0-0\"}\n")
    output = analyzer.run(str(log))
    parsed = json.loads(output)
    assert parsed["spawns"] == 1
