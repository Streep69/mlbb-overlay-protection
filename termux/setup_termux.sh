#!/usr/bin/env bash
# Setup Termux environment for mlbb-overlay-protection
set -Eeuo pipefail

pkg update -y
pkg install -y git python
pip install --upgrade pip
pip install -r "$HOME/mlbb-overlay-protection/requirements.txt"
