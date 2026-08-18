import csv
from datetime import datetime
from pathlib import Path

INPUT_FILE = Path("data/network_events.csv")

def load_events():
    events = []

    with INPUT_FILE.open("r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["timestamp"] = datetime.fromisoformat(row["timestamp"])
            row["destination_port"] = int(row["destination_port"])
            events.append(row)

    return events
def calculate_intervals(events):
    intervals = []

    for i in range(1, len(events)):
        previous = events[i - 1]["timestamp"]
        current = events[i]["timestamp"]

        interval = (current - previous).total_seconds()
        intervals.append(interval)

    return intervals
def detect_periodic_beacon(intervals, tolerance=2.0):
    if len(intervals) < 3:
        return False

    average_interval = sum(intervals) / len(intervals)

    matching_intervals = [
        interval
        for interval in intervals
        if abs(interval - average_interval) <= tolerance
    ]

    consistency = len(matching_intervals) / len(intervals)

    return consistency >= 0.80
if __name__ == "__main__":
    events = load_events()
    intervals = calculate_intervals(events)
    detected = detect_periodic_beacon(intervals)

    print(f"Loaded {len(events)} network events")
    print(f"Connection intervals: {intervals}")
    print(f"Periodic beacon detected: {detected}")
