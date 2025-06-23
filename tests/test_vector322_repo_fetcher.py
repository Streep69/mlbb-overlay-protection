from pathlib import Path
import sys
import json

sys.path.append(str(Path(__file__).resolve().parent.parent))
import vector322_repo_fetcher as v322
import mlbb_repo_fetcher

class DummyRepo:
    def __init__(self, name: str) -> None:
        self.full_name = name
        self.description = "desc"
        self.html_url = "http://example.com"
        self.stargazers_count = 1
        self.language = "Python"

class DummyGithub:
    def __init__(self, token: str) -> None:
        self.token = token
    def get_user(self):
        class U:
            login = "user"
        return U()
    def search_repositories(self, query: str, sort: str | None = None, order: str | None = None):
        return [DummyRepo("owner/repo")]

class DummyException(Exception):
    pass

def test_repo_fetcher(monkeypatch, tmp_path: Path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("GH_PAT", "x")
    monkeypatch.setattr(mlbb_repo_fetcher, "Github", DummyGithub)
    monkeypatch.setattr(mlbb_repo_fetcher, "BadCredentialsException", DummyException)
    monkeypatch.setattr(mlbb_repo_fetcher, "GithubException", DummyException)
    result = v322.run()
    assert result == "vector322 executed"
    data = json.loads(Path("mlbb_repos.json").read_text(encoding="utf-8"))
    assert data[0]["full_name"] == "owner/repo"
