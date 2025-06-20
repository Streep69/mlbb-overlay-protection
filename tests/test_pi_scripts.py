import importlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

MODULES = [
    'cleaner',
    'devguard',
    'fps_validator',
    'game_lobby_detector',
    'overlay_flag_monitor',
    'playprotect_guard',
    'render_fallback',
    'sync_to_pi',
    'your_remaining_modules_here',
]


def test_pi_modules_run():
    for name in MODULES:
        mod = importlib.import_module(f'pi.{name}')
        assert mod.run() == f'{name} executed'


def test_heartbeat_run_once():
    hb = importlib.import_module('pi.heartbeat')
    assert hb.run(iterations=1, interval=0) is None
