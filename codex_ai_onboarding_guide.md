# Codex Phantom Stack: AI Onboarding Guide

## Project Overview
This project is a modular, anti-detection, AI-driven overlay/cheat architecture for Mobile Legends (MLBB), with a focus on safety, obfuscation, and maintainability.

## Repo Key Structure
- `/vectors/` — Modular Python agents for cheats, overlays, anti-detection.
- `/scripts/` — Build, deploy, obfuscation, and validation utilities.
- `/docs/` — Chat logs, guides, master logs, onboarding, vector manifest.
- `/pi/` and `/termux/` — Device-specific code (AI overlay, pipe listener, tapbot).
- `/test/` — Session logs, validation runs, and AI training/test data.

## How to Expand
- Add new features as vectors in `/vectors/`
- Log all architecture changes in `/canvas/codex_canvas.md`
- After each deployment, export updated logs and crosscheck files to `/docs/`

## For AI Agents
- Always reference the latest manifest, master log, and canvas when reasoning about changes
- Update the cross-reference and chunk outputs for memory safety
