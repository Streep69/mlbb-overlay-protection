from pathlib import Path

AGENTS_FILE = Path(__file__).resolve().parent.parent / 'AGENTS.md'


def test_loadtest_agent_registered():
    text = AGENTS_FILE.read_text()
    assert 'LoadTestAgent' in text
    assert 'vector315_overlay_loadtest.py' in text
