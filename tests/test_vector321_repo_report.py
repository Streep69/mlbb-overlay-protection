from pathlib import Path
import json
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector321_repo_report as v321


def test_generate_report(tmp_path: Path):
    data = [
        {"category": "maphack"},
        {"category": "drone"},
        {"category": "maphack"}
    ]
    index = tmp_path / "mlbb_repos.json"
    index.write_text(json.dumps(data), encoding="utf-8")
    counts = v321.generate_report(index)
    assert counts["maphack"] == 2
    assert counts["drone"] == 1
    assert v321.run(index) == "vector321 executed"
