from src.analyzer import detect_periodic_beacon
from src.scoring import calculate_risk_score, get_severity


def test_regular_intervals_detect_beacon():
    intervals = [30, 30, 30, 30, 30]

    detected, consistency, average_interval = detect_periodic_beacon(intervals)

    assert detected is True
    assert consistency == 1.0
    assert average_interval == 30.0

def test_irregular_intervals_do_not_detect_beacon():
    intervals = [10, 45, 18, 70, 25]

    detected, consistency, average_interval = detect_periodic_beacon(intervals)

    assert detected is False

def test_insufficient_intervals_do_not_detect_beacon():
    intervals = [30, 30]

    detected, consistency, average_interval = detect_periodic_beacon(intervals)

    assert detected is False
    assert consistency == 0.0
    assert average_interval == 0.0

def test_high_consistency_produces_high_severity():
    score = calculate_risk_score(True, 1.0)
    severity = get_severity(score)

    assert score == 100
    assert severity == "High"

def test_no_detection_produces_zero_risk():
    score = calculate_risk_score(False, 0.0)
    severity = get_severity(score)

    assert score == 0
    assert severity == "Informational"
