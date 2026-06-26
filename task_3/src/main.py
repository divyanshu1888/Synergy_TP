"""
main.py

Entry point for Task 3.

Run from the repository root:
    python task_3/src/main.py task_3/data/submissions.csv

This script:
    1. Runs the manual parser on the given CSV and writes
       task_3/output/manual_summary.json
    2. Runs the pandas parser on the same CSV and writes
       task_3/output/pandas_summary.json
    3. Compares both summaries field-by-field and writes
       task_3/output/comparison_report.md
"""

import os
import sys

# Make sure manual_parser.py and pandas_parser.py (in the same folder
# as this file) can be imported regardless of the working directory
# this script is launched from.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from manual_parser import (
    read_csv_manual,
    convert_types,
    calculate_summary as calculate_summary_manual,
    write_json as write_json_manual,
)
from pandas_parser import (
    read_csv_pandas,
    calculate_summary_pandas,
    write_json as write_json_pandas,
)

OUTPUT_DIR = os.path.join("task_3", "output")


def run_manual(csv_path: str) -> dict:
    raw_rows = read_csv_manual(csv_path)
    typed_rows = convert_types(raw_rows)
    summary = calculate_summary_manual(typed_rows)
    write_json_manual(summary, os.path.join(OUTPUT_DIR, "manual_summary.json"))
    return summary


def run_pandas(csv_path: str) -> dict:
    df = read_csv_pandas(csv_path)
    summary = calculate_summary_pandas(df)
    write_json_pandas(summary, os.path.join(OUTPUT_DIR, "pandas_summary.json"))
    return summary


def write_comparison_report(
    manual_summary: dict, pandas_summary: dict, report_path: str
) -> None:
    """Write a Markdown report comparing the two summaries field-by-field."""
    keys = list(manual_summary.keys())
    mismatches = [k for k in keys if manual_summary[k] != pandas_summary[k]]

    lines = []
    lines.append("# Comparison Report: Manual Parser vs Pandas")
    lines.append("")
    lines.append(
        "This report compares the summary produced by the hand-written "
        "CSV parser (`manual_parser.py`) against the summary produced "
        "by pandas (`pandas_parser.py`) for the same input file, "
        "`task_3/data/submissions.csv`."
    )
    lines.append("")
    lines.append("## Field-by-field comparison")
    lines.append("")
    lines.append("| Field | Manual Parser | Pandas | Match |")
    lines.append("| --- | --- | --- | --- |")
    for k in keys:
        match = "Yes" if k not in mismatches else "No"
        lines.append(f"| {k} | {manual_summary[k]} | {pandas_summary[k]} | {match} |")
    lines.append("")

    lines.append("## Conclusion")
    lines.append("")
    if not mismatches:
        lines.append(
            "Both the manual parser and pandas produced identical results "
            "for every field in the summary. This confirms that the "
            "hand-written CSV reading, type conversion, and aggregation "
            "logic behaves equivalently to pandas' built-in CSV loading "
            "and groupby/aggregation functions for this dataset."
        )
    else:
        lines.append(
            "The following fields differed between the manual parser "
            f"and pandas: {', '.join(mismatches)}. A difference here "
            "usually points to a discrepancy in type conversion, "
            "rounding, or string normalization between the two "
            "implementations, and should be investigated before "
            "trusting either summary."
        )

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python task_3/src/main.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    manual_summary = run_manual(csv_path)
    pandas_summary = run_pandas(csv_path)

    write_comparison_report(
        manual_summary,
        pandas_summary,
        os.path.join(OUTPUT_DIR, "comparison_report.md"),
    )

    print("Task 3 complete. Outputs written to:")
    print(f"  - {os.path.join(OUTPUT_DIR, 'manual_summary.json')}")
    print(f"  - {os.path.join(OUTPUT_DIR, 'pandas_summary.json')}")
    print(f"  - {os.path.join(OUTPUT_DIR, 'comparison_report.md')}")


if __name__ == "__main__":
    main()