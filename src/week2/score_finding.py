import json
from pathlib import Path

from scoring import score_finding


def load_finding(file_path):
    with open(file_path) as file:
        return json.load(file)


def save_finding(finding, file_path):
    with open(file_path, "w") as file:
        json.dump(finding, file, indent=2)


def calculate_exploitability(finding):
    """
    Estimate exploitability using simple transparent rules.
    """

    score = 5.0

    title = finding.get("title", "").lower()
    description = finding.get("description", "").lower()
    evidence = finding.get("evidence", "").lower()

    text = f"{title} {description} {evidence}"

    # Remote exploitation is generally easier to perform at scale.
    if "remote" in text:
        score += 2

    # Common remotely exploitable attack patterns.
    if "sql injection" in text or "command injection" in text:
        score += 2

    # Authentication requirements make exploitation harder.
    if "authentication required" in text or "requires authentication" in text:
        score -= 2

    return max(0, min(10, score))


def calculate_impact(finding):
    """
    Estimate impact using simple transparent rules.
    """

    score = 5.0

    title = finding.get("title", "").lower()
    description = finding.get("description", "").lower()
    evidence = finding.get("evidence", "").lower()

    text = f"{title} {description} {evidence}"

    # High-impact outcomes.
    if "remote code execution" in text or "code execution" in text:
        score += 4

    if "data loss" in text or "sensitive data" in text:
        score += 2

    if "privilege escalation" in text:
        score += 2

    return max(0, min(10, score))


def main():
    input_file = Path("schemas/example_llm.json")
    output_file = Path("schemas/example_llm_scored.json")

    finding = load_finding(input_file)

    exploitability = calculate_exploitability(finding)
    impact = calculate_impact(finding)

    result = score_finding(
        exploitability,
        impact
    )

    finding["exploitability"] = result["exploitability"]
    finding["impact"] = result["impact"]
    finding["risk_score"] = result["risk_score"]
    finding["severity"] = result["severity"]

    save_finding(finding, output_file)

    print(json.dumps(finding, indent=2))


if __name__ == "__main__":
    main()