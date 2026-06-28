import json
import pandas as pd

def read_csv_pandas(file_path: str):
    df = pd.read_csv(file_path)
    return df

def calculate_summary_pandas(df) -> dict:
    total = len(df)
    submitted = df[df["submitted"].str.lower() == "yes"]
    not_submitted = df[df["submitted"].str.lower() == "no"]

    average_score = round(df["score"].mean(), 2)
    highest = df.loc[df["score"].idxmax(), "name"]
    lowest_submitted = submitted.loc[submitted["score"].idxmin(), "name"] if not submitted.empty else None

    domain_average = (
        df.groupby("domain")["score"]
        .mean()
        .round(2)
        .to_dict()
    )

    return {
        "total_students": total,
        "submitted_count": int(len(submitted)),
        "missing_submissions": int(len(not_submitted)),
        "average_score": average_score,
        "highest_scorer": highest,
        "lowest_scorer_among_submitted": lowest_submitted,
        "domain_wise_average_score": domain_average,
        "students_who_did_not_submit": not_submitted["name"].tolist(),
        "students_scoring_below_5": df[df["score"] < 5]["name"].tolist()
    }

def write_json(data: dict, output_path: str) -> None:
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {output_path}")
