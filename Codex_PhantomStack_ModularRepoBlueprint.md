# Codex Phantom Stack – Unified Modular Repo Blueprint

---

## I. Structure & Directory Layout

```plaintext
/vectors/        # All vectorXXX.py (maphack, ESP, entropy, tapbot, anti-detection, overlays)
/scripts/        # Utility, rotation, build, deploy, validation, log cleaners, ADB, pipeline
/docs/           # Chat logs, anti-ban guides, crosscheck, full context, update manuals
/pi/             # Pi-side AI, overlay, minimap, signal encoder, synthetic input modules
/termux/         # Termux clients: overlay injector, tapbot, pipe listener, system spoofer
/test/           # Session logs, replays, fake audits, AI training/test data
README.md        # Executive summary, project logic, build pipeline
Codex_PhantomStack_MasterLog.md
Codex_PhantomStack_SuperCrosscheck.md
```

---

## II. Cross-Referenced Core Concepts & Safeguards

- **Obfuscation & Rotation:**  
  - Fully automated scripts rotate filenames, symbol names, .rodata encryption, and generate a manifest per build.
  - Loader patches in MLBB dynamically parse manifest to dlopen correct .so library.
- **Humanization:**  
  - Tapbots/randomizer logic uses Markov, Gaussian, and AI-recorded session replay.
- **Anti-detection Vectors:**  
  - Overlay is hidden from screenshots/logs via MediaProjection, framebuffer, or Pi-driven fake screen injection.
  - System process maps and appops are faked; permissions appear "granted" in UI but are denied at kernel level.
- **Manifest/Validation:**  
  - Each build's output is tracked via JSON manifest: timestamp, filename, XOR key, symbol prefix, hash.
- **Test/CI:**  
  - Scripts for validating symbol stripping, .rodata content, loader integrity; regression logs saved to `/test/`.
- **Deployment:**  
  - Termux and Pi scripts for secure sync, hot-reload, and session update; all cross-referenced for minimal on-device risk.

---

## III. Suggested Working Tree with Comments

```plaintext
/vectors/
  vector150_maphack.py        # ESP, minimap, overlay core
  vector223_entropy.py        # Tap entropy engine, humanize bot
  vector291_logclean.py       # Advanced log and process cleaner
  vector330_injector.py       # Safe overlay/tap injector

/scripts/
  compile_obf.sh              # Build, obfuscate, manifest, validate, rotate
  deploy_obf.sh               # ADB push, root perms, manifest sync
  loader_patch.c              # JNI loader patch, manifest reader
  validate_syms.sh            # Checks for unmangled symbols
  validate_rodata.sh          # Ensures .rodata encrypted
  rotate_so.sh                # Fast .so filename/symbol swap

/docs/
  README.md
  Codex_PhantomStack_MasterLog.md
  Codex_PhantomStack_SuperCrosscheck.md
  anti_ban_guide.md
  vector_list.md

/pi/
  ai_overlay_engine.py        # Overlay from AI/ML, frame blending
  signal_encoder.py           # AI to overlay/tap signal relay

/termux/
  codex_pipe_listener.py      # Pipe overlay/tap signals from Pi
  overlay_faker.py            # Ensure overlay invisible to logs/screenshots
  tapbot_entropy.py           # Mimic human input

/test/
  session_log_2025-06-24.log
  replay_synthetic_001.json
  validation_report_2025-06-24.md
```

---

## IV. Practices for Memory-Safe, Trace-Safe, Next-Gen Project

- **Chunked Docs:**  
  Keep master log and super crosscheck modular (import only what’s needed per GPT/AI session).
- **Scripted Validation:**  
  Every build/check rotates filenames, keys, and generates reports/logs.
- **Minimal On-Device Footprint:**  
  MLBB/Termux only see newest .so and manifest; AI logic, overlays, and signal encoding live on Pi for security.
- **Continuous Analysis:**  
  Import/export all chat/crosscheck logs for future GPT sessions (never start “from scratch”).
- **Test/Replay:**  
  Use `/test/` for session playback and validation, not just logs.

---
