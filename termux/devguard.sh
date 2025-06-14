#!/data/data/com.termux/files/usr/bin/bash
# devguard.sh — Disables USB debugging & developer options before gameplay
adb shell settings put global development_settings_enabled 0
adb shell settings put global adb_enabled 0
adb shell settings put secure show_touches 0
adb shell settings put secure pointer_location 0
echo "[devguard] Developer flags cleared"
