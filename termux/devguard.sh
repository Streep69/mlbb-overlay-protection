#!/usr/bin/env bash
adb shell settings put global development_settings_enabled 0
adb shell settings put global adb_enabled 0
adb shell settings put secure show_touches 0
echo "[devguard] Flags cleared"
