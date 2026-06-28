import json


def read_csv_manual(file_path: str) -> list:
    rows = []
    with open(file_path, "r") as f:
        lines = f.readlines()

    if not lines:
        return rows
    header = lines[0].strip().split(",")

    for line in lines[1:]:
        line = line.strip()

        # Skips empty lines
        if not line:
            continue
        values = line.split(",")
        
        if len(values) != len(header):
            print(f"Skipping malformed row: {line}")
            continue
            
        row = {}
        for i in range(len(header)):
            row[header[i]] = values[i]

        rows.append(row)

    return rows

def convert_types(rows: list) -> list:
    converted = []
    for row in rows:
        new_row = dict(row) 
        # Converts score to integer
        try:
            new_row["score"] = int(row["score"])
        except ValueError:
            new_row["score"] = 0

        submitted_val = row["submitted"].strip().lower()
        new_row["submitted"] = "yes" if submitted_val == "yes" else "no"

        converted.append(new_row)
    return converted

def calculate_summary(rows: list) -> dict:
    total = len(rows)
    submitted = [r for r in rows if r["submitted"] == "yes"]
    not_submitted = [r for r in rows if r["submitted"] == "no"]

    scores_all = [r["score"] for r in rows]
    scores_submitted = [r["score"] for r in submitted]

    average_score = round(sum(scores_all) / total, 2) if total > 0 else 0

    highest = max(rows, key=lambda r: r["score"])
    lowest_submitted = min(submitted, key=lambda r: r["score"]) if submitted else None

    # Domain-wise average score
    domain_scores = {}
    for r in rows:
        d = r["domain"]
        if d not in domain_scores:
            domain_scores[d] = []
        domain_scores[d].append(r["score"])

    domain_average = {d: round(sum(v) / len(v), 2) for d, v in domain_scores.items()}

    return {
        "total_students": total,
        "submitted_count": len(submitted),
        "missing_submissions": len(not_submitted),
        "average_score": average_score,
        "highest_scorer": highest["name"],
        "lowest_scorer_among_submitted": lowest_submitted["name"] if lowest_submitted else None,
        "domain_wise_average_score": domain_average,
        "students_who_did_not_submit": [r["name"] for r in not_submitted],
        "students_scoring_below_5": [r["name"] for r in rows if r["score"] < 5]
    }


def write_json(data: dict, output_path: str) -> None:
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {output_path}")
