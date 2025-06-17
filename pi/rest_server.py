import asyncio
from aiohttp import web
from typing import Optional


async def handle_health(request: web.Request) -> web.Response:
    """Return server health status."""
    return web.json_response({"status": "ok"})


async def start_server(
    host: str = "127.0.0.1",
    port: int = 8080,
    stop_event: Optional[asyncio.Event] = None,
) -> asyncio.Event:
    """Start an aiohttp server and block until ``stop_event`` is set."""
    app = web.Application()
    app.router.add_get("/health", handle_health)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()

    # Wait until cancelled
    if stop_event is None:
        stop_event = asyncio.Event()
    try:
        await stop_event.wait()
    finally:
        await runner.cleanup()
    return stop_event


def run(host: str = "127.0.0.1", port: int = 8080) -> None:
    """Run the server until interrupted."""
    stop_event = asyncio.Event()
    try:
        asyncio.run(start_server(host, port, stop_event))
    except KeyboardInterrupt:
        stop_event.set()
