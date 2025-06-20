"""Vector module 150: IsolationForest anomaly detector."""
from __future__ import annotations
import json
import logging
from pathlib import Path
import numpy as np
from sklearn.ensemble import IsolationForest

LOGGER = logging.getLogger(__name__)

ASSETS = Path(__file__).resolve().parent.parent / 'sandbox' / 'assets'


def detect_anomalies() -> int:
    """Return number of detected anomalies."""
    normal_file = ASSETS / 'normal_sessions.json'
    anomaly_file = ASSETS / 'anomaly_sessions.json'
    normal = np.array(json.loads(normal_file.read_text()))
    anomaly = np.array(json.loads(anomaly_file.read_text()))
    clf = IsolationForest(contamination=0.1, random_state=42)
    clf.fit(normal)
    scores = clf.decision_function(anomaly)
    detected = int((scores < 0).sum())
    LOGGER.info("Detected %s anomalies", detected)
    return detected


def run() -> str:
    """Execute anomaly detection."""
    detect_anomalies()
    return 'vector150 executed'
