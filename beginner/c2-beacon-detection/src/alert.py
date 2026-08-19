from src.scoring import calculate_risk_score, get_severity


def create_alert(
    detected,
    consistency,
    average_interval,
    source_ip,
    destination_ip,
    destination_port,
):
    score = calculate_risk_score(detected, consistency)
    severity = get_severity(score)

    alert = {
        "detection": "Possible C2 Beaconing",
        "detected": detected,
        "risk_score": score,
        "severity": severity,
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "destination_port": destination_port,
        "average_interval_seconds": round(average_interval, 2),
        "interval_consistency_percent": round(consistency * 100, 2),
    }
    
    return alert

def print_alert(alert):
    print("\n=== C2 BEACON DETECTION ALERT ===")
    print(f"Detection: {alert['detection']}")
    print(f"Detected: {alert['detected']}")
    print(f"Risk Score: {alert['risk_score']}/100")
    print(f"Severity: {alert['severity']}")
    print(f"Source: {alert['source_ip']}")
    print(f"Destination: {alert['destination_ip']}:{alert['destination_port']}")
    print(f"Average Interval: {alert['average_interval_seconds']} seconds")
    print(f"Interval Consistency: {alert['interval_consistency_percent']}%")
