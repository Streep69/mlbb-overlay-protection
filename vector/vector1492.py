"""Vector module 149: Tkinter dashboard with REST endpoint."""
from __future__ import annotations
import logging
import threading
import asyncio
import os
<<<<<<< HEAD

try:
    from aiohttp import web
except ModuleNotFoundError:  # pragma: no cover - optional aiohttp dependency
    web = None

try:
    import tkinter as tk
except ModuleNotFoundError:  # pragma: no cover - optional GUI dependency
    tk = None
=======
from aiohttp import web
import tkinter as tk
>>>>>>> origin/main

LOGGER = logging.getLogger(__name__)

class SecurityDashboard:
    """Simple Tkinter dashboard."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Anti-Cheat Dashboard")
        label = tk.Label(self.root, text="Dashboard initialized")
        label.pack(padx=10, pady=10)

    def start(self) -> None:
        threading.Thread(target=self.root.mainloop, daemon=True).start()

<<<<<<< HEAD
async def handle_status(request: 'web.Request') -> 'web.Response':
=======
async def handle_status(request: web.Request) -> web.Response:
>>>>>>> origin/main
    """Return OK status."""
    return web.json_response({"status": "ok"})

async def start_server() -> None:
<<<<<<< HEAD
    if web is None:
        LOGGER.warning('aiohttp not installed; REST server disabled')
        return
=======
>>>>>>> origin/main
    app = web.Application()
    app.router.add_get('/status', handle_status)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()


def run() -> str:
    """Initialize dashboard and REST server."""
<<<<<<< HEAD
    if not os.environ.get('DISPLAY') or tk is None:
        LOGGER.warning('GUI dependencies unavailable; skipping dashboard')
=======
    if not os.environ.get('DISPLAY'):
        LOGGER.warning('No display found; skipping GUI')
>>>>>>> origin/main
        return 'vector149 executed'
    dashboard = SecurityDashboard()
    dashboard.start()
    asyncio.run(start_server())
    LOGGER.info("Vector149 dashboard and server started")
    return 'vector149 executed'
