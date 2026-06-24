import csv
import os
from typing import Any


def read_submissions(filepath: str) -> list[dict[str, Any]]:
    """Reads student data from a CSV file and returns a list of records."""

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    students = []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["score"] = int(row["score"])
            row["submitted"] = row["submitted"].strip().lower()
            students.append(dict(row))

    return students


def get_submitted_students(students: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Returns only students who submitted their work."""

    return [s for s in students if s["submitted"] == "yes"]



def get_missing_submissions(students: list[dict[str, Any]]) -> list[str]:
    """Returns names of students who did not submit."""

    return [s["name"] for s in students if s["submitted"] != "yes"]


def calculate_average_score(students: list[dict[str, Any]]) -> float:
    """Calculates the average score across all students."""

    if not students:
        return 0.0

    total = sum(s["score"] for s in students)
    return round(total / len(students), 2)


def get_domain_wise_average(students: list[dict[str, Any]]) -> dict[str, float]:
    """Computes the average score per domain."""

    domain_scores = {}

    for s in students:
        domain = s["domain"]
        if domain not in domain_scores:
            domain_scores[domain] = []
        domain_scores[domain].append(s["score"])

    result = {}
    for domain, scores in domain_scores.items():
        result[domain] = round(sum(scores) / len(scores), 2)

    return result


def write_summary(summary: dict[str, Any], output_path: str) -> None:
    """Writes the summary dictionary to a JSON file."""

    import json
    import os

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)