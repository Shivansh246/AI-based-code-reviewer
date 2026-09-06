import json

finding = {
    "id": "SQL001",
    "source": "llm",
    "file": "example.py",
    "line": 5,
    "title": "Possible SQL Injection",
    "severity": "high",
    "confidence": 0.94,
    "description": "User input is directly used in a SQL query."
}

json_text = json.dumps(finding, indent=2)

parsed = json.loads(json_text)

print(parsed["title"])
print(parsed["severity"])
print(parsed["confidence"])