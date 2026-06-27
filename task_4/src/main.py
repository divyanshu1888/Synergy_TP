import sys
import json

from clean_data import (
    load_data,
    generate_summary,
    remove_duplicates,
    standardize_domains,
    clean_attendance,
    clean_scores,
    clean_study_hours,
    clean_height,
    clean_weight,
    clean_submitted,
    handle_missing_values,
    save_cleaned_data,
    write_report,
)

from validate_data import validate_cleaned_data


def main():
    if len(sys.argv) != 3:
        print("Usage: python task_4/src/main.py <input_csv> <output_csv>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    df = load_data(input_file)

    before_summary = generate_summary(df)

    df = remove_duplicates(df)
    df = standardize_domains(df)
    df = clean_attendance(df)
    df = clean_scores(df)
    df = clean_study_hours(df)
    df = clean_height(df)
    df = clean_weight(df)
    df = clean_submitted(df)
    df = handle_missing_values(df)

    after_summary = generate_summary(df)

    if not validate_cleaned_data(df):
        print("Validation failed!")
        return

    save_cleaned_data(df, output_file)

    with open("task_4/output/summary_before.json", "w") as f:
        json.dump(before_summary, f, indent=4)

    with open("task_4/output/summary_after.json", "w") as f:
        json.dump(after_summary, f, indent=4)

    write_report("task_4/output/cleaning_report.md")

    print("Task 4 completed successfully!")


if __name__ == "__main__":
    main()