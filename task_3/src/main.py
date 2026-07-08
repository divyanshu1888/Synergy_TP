import json
import sys

# We need to tell Python where to find our other files
sys.path.insert(0, "task_3/src")

#Importing files from each of the parser
from manual_parser import read_csv_manual, convert_types, calculate_summary, write_json
from pandas_parser import read_csv_pandas, calculate_summary_pandas, write_json as write_json_pandas


def write_comparison_report(manual_summary, pandas_summary, report_path):
    lines = ["# Comparison Report: Manual Parser vs Pandas\n\n"]

    all_match = True
    for key in manual_summary:
        m_val = manual_summary[key]
        p_val = pandas_summary.get(key)
        match = "MATCH" if m_val == p_val else "MISMATCH"
        if m_val != p_val:
            all_match = False
        lines.append(f"## {key}\n")
        lines.append(f"- Manual : {m_val}\n")
        lines.append(f"- Pandas : {p_val}\n")
        lines.append(f"- Result : {match}\n\n")

    if all_match:
        lines.append("## Conclusion\nBoth parsers produced identical results.\n")
    else:
        lines.append("## Conclusion\nThere are some differences between the two parsers. Review above.\n")

    with open(report_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Saved: {report_path}")

#Main Function
def main():
    input_path = sys.argv[1]

    # Manual Parser
    print("\n--- Running Manual Parser ---")
    raw_rows = read_csv_manual(input_path)
    rows = convert_types(raw_rows)
    manual_summary = calculate_summary(rows)
    write_json(manual_summary, "task_3/output/manual_summary.json")

    # Pandas Parser
    print("\n--- Running Pandas Parser ---")
    df = read_csv_pandas(input_path)
    pandas_summary = calculate_summary_pandas(df)
    write_json_pandas(pandas_summary, "task_3/output/pandas_summary.json")

    # Comparison Report
    print("\n--- Writing Comparison Report ---")
    write_comparison_report(
        manual_summary,
        pandas_summary,
        "task_3/output/comparison_report.md"
    )

    print("\nAll done!")


if __name__ == "__main__":
    main()
