"""
pandas_parser.py

Runs the same analysis as manual_parser.py, but using pandas instead of
hand-written parsing logic. This lets us cross-check the manual parser
against a trusted, high-level library in comparison_report.md.
"""

import json
from typing import Dict

import pandas as pd


def read_csv_pandas(file_path: str) -> pd.DataFrame:
    """
    Load the CSV file into a pandas DataFrame and normalize types so
    the result is directly comparable with the manual parser's output.

        - "score"     -> int
        - "submitted" -> bool (same yes/y/true/1 convention as
                                manual_parser.convert_types)
    """
    df = pd.read_csv(file_path)

    df["score"] = df["score"].astype(int)
    df["submitted"] = (
        df["submitted"]
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["yes", "y", "true", "1"])
    )

    return df


def calculate_summary_pandas(df: pd.DataFrame) -> Dict:
    """
    Compute the same summary statistics as manual_parser.calculate_summary,
    but using pandas operations (groupby, mean, idxmax/idxmin, etc.).
    """
    total_students = int(len(df))

    submitted_df = df[df["submitted"]]
    not_submitted_df = df[~df["submitted"]]

    average_score = (
        round(float(df["score"].mean()), 2) if total_students else 0
    )

    highest_scorer = None
    if total_students:
        top_row = df.loc[df["score"].idxmax()]
        highest_scorer = {
            "name": top_row["name"],
            "score": int(top_row["score"]),
        }

    lowest_scorer_submitted = None
    if not submitted_df.empty:
        low_row = submitted_df.loc[submitted_df["score"].idxmin()]
        lowest_scorer_submitted = {
            "name": low_row["name"],
            "score": int(low_row["score"]),
        }

    # Convert numpy types (int64/float64) to native Python types so the
    domain_average_score = {
        str(domain): float(avg)
        for domain, avg in df.groupby("domain")["score"].mean().round(2).items()
    }

    students_not_submitted = not_submitted_df["name"].tolist()
    students_below_5 = df[df["score"] < 5]["name"].tolist()

    return {
        "total_students": total_students,
        "num_submitted": int(len(submitted_df)),
        "num_missing_submissions": int(len(not_submitted_df)),
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
