"""vector060_api_proxy.py - API Proxy Agent

Purpose: Forward API requests through a simulated proxy layer while logging all
interactions. Useful for replay or throttling experiments.
"""

from __future__ import annotations

import json
import os
import random
import time
from typing import Iterable, Dict, Any, List

AUDIT_LOG = "/test/vector060_api_proxy.log"


def audit_log(event: str) -> None:
    os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event}\n")


class APIProxyAgent:
    def forward(self, request: Dict[str, Any]) -> Dict[str, Any]:
        audit_log(json.dumps(request, ensure_ascii=False))
        time.sleep(random.uniform(0.05, 0.15))
        response = {"status": 200, "data": "ok"}
        audit_log(json.dumps(response))
        return response

    def run(self, requests: Iterable[Dict[str, Any]] | None = None) -> List[Dict[str, Any]]:
        audit_log("apiproxy start")
        if requests is None:
            requests = [{"path": "/status"}]
        responses: List[Dict[str, Any]] = []
        for req in requests:
            responses.append(self.forward(req))
        audit_log("apiproxy end")
        return responses


def run(requests: Iterable[Dict[str, Any]] | None = None) -> List[Dict[str, Any]]:
    return APIProxyAgent().run(requests)


if __name__ == "__main__":  # pragma: no cover
    run()
