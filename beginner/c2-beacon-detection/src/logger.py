import json
from datetime import datetime
from pathlib import Path


LOG_FILE = Path("logs/alerts.json")


def save_alert(alert):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    alert_record = {
        "timestamp": datetime.now().isoformat(),
        **alert,
    }

    with LOG_FILE.open("a") as file:
        json.dump(alert_record, file)
        file.write("\n")
