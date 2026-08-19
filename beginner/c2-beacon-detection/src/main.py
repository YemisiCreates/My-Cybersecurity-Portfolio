from src.analyzer import load_events, calculate_intervals, detect_periodic_beacon
from src.scoring import calculate_risk_score, get_severity
from src.alert import create_alert, print_alert


def main():
    # Load network telemetry
    events = load_events()

    # Analyse timing between connections
    intervals = calculate_intervals(events)

    # Detect periodic beacon-like behaviour
    detected, consistency, average_interval = detect_periodic_beacon(intervals)

    # Get network information from the first event
    source_ip = events[0]["source_ip"]
    destination_ip = events[0]["destination_ip"]
    destination_port = events[0]["destination_port"]

    # Create SOC-style alert
    alert = create_alert(
        detected,
        consistency,
        average_interval,
        source_ip,
        destination_ip,
        destination_port,
    )

    print_alert(alert)


if __name__ == "__main__":
    main()
