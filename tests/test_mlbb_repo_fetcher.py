from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from mlbb_repo_fetcher import categorize_repo


def test_categorize_repo():
    assert categorize_repo("awesome-maphack", "ESP features") == "maphack"
    assert categorize_repo("drone-view-tool", "camera drone view") == "drone"
    assert categorize_repo("GameUnlocker", "boost fps") == "performance"
    assert categorize_repo("ml-api", "REST API") == "api"
    assert categorize_repo("stats-analyzer", "analytics suite") == "analytics"
    assert categorize_repo("random-repo", "nothing special") == "misc"
