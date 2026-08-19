def calculate_risk_score(detected, consistency):
    """
    Calculate a simple risk score for periodic beacon-like behaviour.

    Args:
        detected (bool): Whether periodic behaviour was detected.
        consistency (float): Proportion of intervals matching the expected pattern.

    Returns:
        int: Risk score between 0 and 100.
    """

    if not detected:
        return 0

    score = int(consistency * 100)

    return min(score, 100)


def get_severity(score):
    """
    Convert the numerical risk score into a SOC-style severity level.
    """

    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    elif score > 0:
        return "Low"
    else:
        return "Informational"
