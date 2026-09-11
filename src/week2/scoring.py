def calculate_risk_score(exploitability, impact):
    """
    Calculate a transparent risk score from 0 to 10.

    Exploitability contributes 60%.
    Impact contributes 40%.
    """

    if not 0 <= exploitability <= 10:
        raise ValueError("Exploitability must be between 0 and 10.")

    if not 0 <= impact <= 10:
        raise ValueError("Impact must be between 0 and 10.")

    score = (0.6 * exploitability) + (0.4 * impact)

    return round(score, 2)


def map_severity(score):
    """
    Convert the numerical risk score into a severity level.
    """

    if not 0 <= score <= 10:
        raise ValueError("Risk score must be between 0 and 10.")

    if score < 3:
        return "low"

    if score < 6:
        return "medium"

    if score < 8:
        return "high"

    return "critical"


def score_finding(exploitability, impact):
    """
    Calculate both risk score and severity.
    """

    score = calculate_risk_score(exploitability, impact)
    severity = map_severity(score)

    return {
        "exploitability": exploitability,
        "impact": impact,
        "risk_score": score,
        "severity": severity
    }


if __name__ == "__main__":
    result = score_finding(
        exploitability=8,
        impact=8
    )

    print(result)