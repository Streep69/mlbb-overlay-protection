import asyncio

import aiohttp
import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pi import rest_server


@pytest.mark.asyncio
async def test_health_endpoint_responds():
    stop_event = asyncio.Event()
    server_task = asyncio.create_task(
        rest_server.start_server('127.0.0.1', 8081, stop_event)
    )

    # Wait briefly for the server to start
    await asyncio.sleep(0.1)
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8081/health') as resp:
            assert resp.status == 200
            data = await resp.json()
            assert data == {'status': 'ok'}

    stop_event.set()
    await server_task

