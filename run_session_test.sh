#!/bin/bash
# run_session_test.sh — Codex Phantom Stack Test Runner

echo "== Codex Test Session: $(date) =="
echo "Validating all vectors/scripts..."
python3 /scripts/validate_syms.sh
python3 /scripts/validate_rodata.sh

echo "Running overlay and tapbot tests..."
python3 /vectors/vector150_maphack.py --test
python3 /vectors/vector223_entropy.py --test

echo "Session log written to /test/session_log_$(date +%Y%m%d).log"
