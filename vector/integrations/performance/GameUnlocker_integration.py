"""Integration for https://github.com/ahkehra/GameUnlocker"""
from __future__ import annotations
import subprocess
import tempfile
from pathlib import Path

def setup() -> Path:
    """Clone the repository."""
    temp = Path(tempfile.mkdtemp(prefix='GameUnlocker_'))
    subprocess.run(['git', 'clone', '--depth', '1', 'https://github.com/ahkehra/GameUnlocker.git', str(temp)], check=True)
    return temp

def integrate(config):
    """Integrate detected modules.

    Detected symbols: none
    TODO: wire into overlay lifecycle.
    """
    raise NotImplementedError
