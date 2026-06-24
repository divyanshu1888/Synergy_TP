import sys
from analyzer import read_submissions, get_submitted_students, get_missing_submissions, calculate_average_score, get_domain_wise_average, write_summary


def main():
    students = read_submissions("task_2/data/submissions.csv")

    submitted = get_submitted_students(students)
    missing = get_missing_submissions(students)
    avg_score = calculate_average_score(students)
    domain_avg = get_domain_wise_average(students)

    summary = {
        "total_students": len(students),
        "submitted_count": len(submitted),
        "missing_submissions": missing,
        "average_score": avg_score,
        "domain_wise_average": domain_avg,
    }

    write_summary(summary, "task_2/output/summary.json")

    print("Total Students    :", len(students))
    print("Submitted         :", len(submitted))
    print("Missing           :", missing)
    print("Average Score     :", avg_score)
    print("Domain Averages   :", domain_avg)
    print("\nSummary saved to task_2/output/summary.json")


if __name__ == "__main__":
    main()