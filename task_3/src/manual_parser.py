"""
manual_parser.py

A CSV parser built by hand using only Python's built-in file I/O.

Restrictions (per task spec):
    - pandas is NOT used anywhere in this file.
    - the built-in csv module is NOT used anywhere in this file.

This parser only needs to support simple comma-separated data with a
single header row. Quoted commas and multi-line fields are explicitly
out of scope for this task.
"""

import json
from typing import List, Dict


def read_csv_manual(file_path: str) -> List[Dict]:
    """
    Read a CSV file by hand and turn it into a list of dictionaries.

    Steps:
        1. Open the file with a context manager so it is always closed.
        2. Read the first line as the header and split it on commas.
        3. Iterate over the remaining lines, split each on commas, and
           zip the values with the header to build one dict per row.
        4. Skip blank lines.
        5. Skip "malformed" rows -- rows whose number of comma-separated
           values does not match the number of header columns -- instead
           of letting the program crash.

    Args:
        file_path: Path to the CSV file to read.

    Returns:
        A list of dictionaries (one per valid row). All values are kept
        as raw strings at this stage; numeric/boolean conversion happens
        later in convert_types().
    """
    rows: List[Dict] = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        return rows

    header_line = lines[0].strip()
    header = [column.strip() for column in header_line.split(",")]

    for line_number, raw_line in enumerate(lines[1:], start=2):
        line = raw_line.strip()

        # Skip empty lines without crashing.
        if not line:
            continue

        values = [value.strip() for value in line.split(",")]

        # Malformed row: number of values does not match number of
        # header columns. Skip it (and log why) instead of crashing.
        if len(values) != len(header):
            print(
                f"[manual_parser] Skipping malformed row at line "
                f"{line_number}: {raw_line!r} "
                f"(expected {len(header)} fields, got {len(values)})"
            )
            continue

        row = dict(zip(header, values))
        rows.append(row)

    return rows


def convert_types(rows: List[Dict]) -> List[Dict]:
    """
    Convert raw string fields into the proper Python types.

        - "score"     -> int
        - "submitted" -> bool (True for yes/y/true/1, case-insensitive;
                                False otherwise)

    A row whose score cannot be converted to an int is treated as
    malformed and is skipped (with a message) rather than crashing the
    whole program.

    Args:
        rows: Output of read_csv_manual() -- list of dicts with string
              values.

    Returns:
        A new list of dicts with "score" as int and "submitted" as bool.
        The original list is not mutated.
    """
    converted: List[Dict] = []

    for row in rows:
        new_row = dict(row)  # shallow copy, don't mutate the input

        try:
            new_row["score"] = int(row["score"])
        except (KeyError, ValueError):
            print(f"[manual_parser] Skipping row with invalid score: {row}")
            continue

        submitted_raw = str(row.get("submitted", "")).strip().lower()
        new_row["submitted"] = submitted_raw in ("yes", "y", "true", "1")

        converted.append(new_row)

    return converted


def calculate_summary(rows: List[Dict]) -> Dict:
    """
    Compute the summary statistics required by the task spec.

    Expects each row to already have "score" as int and "submitted"
    as bool (i.e. rows should already have been through convert_types).

    Returns a dict with:
        total_students, num_submitted, num_missing_submissions,
        average_score, highest_scorer, lowest_scorer_submitted,
        domain_average_score, students_not_submitted, students_below_5
    """
    total_students = len(rows)

    submitted_rows = [r for r in rows if r["submitted"]]
    not_submitted_rows = [r for r in rows if not r["submitted"]]

    average_score = (
        round(sum(r["score"] for r in rows) / total_students, 2)
        if total_students
        else 0
    )

    highest_scorer = None
    if rows:
        top_row = max(rows, key=lambda r: r["score"])
        highest_scorer = {"name": top_row["name"], "score": top_row["score"]}

    lowest_scorer_submitted = None
    if submitted_rows:
        low_row = min(submitted_rows, key=lambda r: r["score"])
        lowest_scorer_submitted = {
            "name": low_row["name"],
            "score": low_row["score"],
        }

    domain_totals: Dict[str, List[int]] = {}
    for r in rows:
        domain_totals.setdefault(r["domain"], []).append(r["score"])

    domain_average_score = {
        domain: round(sum(scores) / len(scores), 2)
        for domain, scores in domain_totals.items()
    }

    students_not_submitted = [r["name"] for r in not_submitted_rows]
    students_below_5 = [r["name"] for r in rows if r["score"] < 5]

    return {
        "total_students": total_students,
        "num_submitted": len(submitted_rows),
        "num_missing_submissions": len(not_submitted_rows),
        "average_score": average_score,
        "highest_scorer": highest_scorer,
        "lowest_scorer_submitted": lowest_scorer_submitted,
        "domain_average_score": domain_average_score,
        "students_not_submitted": students_not_submitted,
        "students_below_5": students_below_5,
    }


def write_json(data: Dict, output_path: str) -> None:
    """Write a dictionary to disk as a pretty-printed JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)