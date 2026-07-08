import sys
import numpy as np

# Import from analyzer.py
from analyzer import (
    read_submissions,
    get_submitted_students,
    calculate_average_score,
    get_domain_wise_average,
    get_missing_submissions,
    write_summary,
)


def main():
    # Step 1: Get file paths from the command line
    # When you run: python task_2/src/main.py data/submissions.csv output/summary.json
    # sys.argv[1] = "data/submissions.csv"
    # sys.argv[2] = "output/summary.json"

    if len(sys.argv) < 3:
        print("Please provide input and output file paths.")
        print("Example: python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Step 2: Read the CSV file
    df = read_submissions(input_file)

    # Stop if the file couldn't be loaded
    if df.empty:
        print("Could not load data. Please check the input file.")
        return

    # Step 3: Calculating all the required values
    
    # Total number of students
    total_students = len(df)

    # Students who submitted
    submitted_df = get_submitted_students(df)
    submitted_count = len(submitted_df)

    # Students who did NOT submit
    missing_names = get_missing_submissions(df)
    missing_count = len(missing_names)

    # Average score of all students
    average_score = calculate_average_score(df)

    # Highest scorer (find the row with the maximum score)
    highest_score_index = df["score"].idxmax()
    highest_scorer = df.loc[highest_score_index, "name"]
    highest_score_value = df.loc[highest_score_index, "score"]

    # Lowest scorer among submitted students only
    lowest_score_index = submitted_df["score"].idxmin()
    lowest_scorer = submitted_df.loc[lowest_score_index, "name"]
    lowest_score_value = submitted_df.loc[lowest_score_index, "score"]

    # Domain-wise average scores
    domain_averages = get_domain_wise_average(df)

    # Students who scored below 5
    below_5_df = df[df["score"] < 5]
    students_below_5 = below_5_df["name"].tolist()

    # Step 4: Print results to the terminal
    print("=" * 40)
    print("        STUDENT SUBMISSION REPORT")
    print("=" * 40)
    print("Total Students        :", total_students)
    print("Submitted             :", submitted_count)
    print("Missing Submissions   :", missing_count)
    print("Average Score         :", average_score)
    print("Highest Scorer        :", highest_scorer, "(Score:", int(highest_score_value), ")")
    print("Lowest Scorer (submitted):", lowest_scorer, "(Score:", int(lowest_score_value), ")")
    print("Missing Submissions   :", missing_names)
    print("Students Below 5      :", students_below_5)
    print()
    print("Domain-wise Averages:")
    for domain, avg in domain_averages.items():
        print("  ", domain, "->", avg)
    print("=" * 40)

    # Step 5: Build the summary dictionary and save it
    summary = {
        "total_students": total_students,
        "submitted_count": submitted_count,
        "missing_count": missing_count,
        "average_score": average_score,
        "highest_scorer": {
            "name": highest_scorer,
            "score": int(highest_score_value)
        },
        "lowest_scorer_among_submitted": {
            "name": lowest_scorer,
            "score": int(lowest_score_value)
        },
        "domain_wise_average": domain_averages,
        "missing_submissions": missing_names,
        "students_below_5": students_below_5,
    }

    write_summary(summary, output_file)


# Python runs this when you call the file directly
if __name__ == "__main__":
    main()
