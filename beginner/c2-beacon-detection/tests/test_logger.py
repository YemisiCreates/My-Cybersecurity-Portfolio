import json

from src.logger import save_alert


def test_save_alert_writes_json(tmp_path, monkeypatch):
    test_log = tmp_path / "alerts.json"

    monkeypatch.setattr("src.logger.LOG_FILE", test_log)

    alert = {
        "detection": "Possible C2 Beaconing",
        "detected": True,
        "risk_score": 100,
        "severity": "High",
        "source_ip": "192.168.1.25",
        "destination_ip": "203.0.113.50",
        "destination_port": 443,
        "average_interval_seconds": 30.14,
        "interval_consistency_percent": 100.0,
    }

    save_alert(alert)

    with test_log.open("r") as file:
        saved = json.loads(file.readline())

    assert saved["detection"] == "Possible C2 Beaconing"
    assert saved["risk_score"] == 100
    assert saved["severity"] == "High"
    assert saved["source_ip"] == "192.168.1.25"
