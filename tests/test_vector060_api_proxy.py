from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectors import vector060_api_proxy as v060


def test_api_proxy():
    responses = v060.APIProxyAgent().run([{"path": "/ping"}])
    assert responses[0]["status"] == 200
