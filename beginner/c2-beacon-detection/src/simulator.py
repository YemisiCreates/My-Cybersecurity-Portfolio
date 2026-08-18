import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

OUTPUT_FILE = Path("data/network_events.csv")

def create_event(timestamp, source_ip, destination_ip, destination_port):
    return {
        "timestamp": timestamp.isoformat(),
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "destination_port": destination_port,
    }


def generate_beacon_traffic(count=20, interval=30, jitter=0.10):
    events = []
    current_time = datetime.now()

    for _ in range(count):
        event = create_event(
            current_time,
            "192.168.1.25",
            "203.0.113.50",
            443,
        )

        events.append(event)
        jitter_amount = interval * jitter
        next_interval = interval + random.uniform(-jitter_amount, jitter_amount)

        current_time += timedelta(seconds=next_interval)

    return events


def save_events(events):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", newline="") as file:
        fieldnames = [
            "timestamp",
            "source_ip",
            "destination_ip",
            "destination_port",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)
if __name__ == "__main__":
    events = generate_beacon_traffic()
    save_events(events)
    print(f"Generated {len(events)} network events.")
    print(f"Saved to {OUTPUT_FILE}")
