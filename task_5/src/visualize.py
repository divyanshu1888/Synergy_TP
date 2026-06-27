import pandas as pd
import matplotlib.pyplot as plt


def load_cleaned_data(file_path):
    """Load the cleaned CSV dataset."""
    return pd.read_csv(file_path)


def plot_domain_average_score(df, output_path):
    """Generate bar chart for average score by domain."""

    averages = df.groupby("domain")["score"].mean()

    plt.figure(figsize=(6, 4))
    averages.plot(kind="bar")

    plt.title("Average Score by Domain")
    plt.xlabel("Domain")
    plt.ylabel("Average Score")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_attendance_vs_score(df, output_path):
    """Generate scatter plot for attendance vs score."""

    plt.figure(figsize=(6, 4))

    plt.scatter(
        df["attendance_percent"],
        df["score"]
    )

    plt.title("Attendance vs Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Score")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_submission_status_count(df, output_path):
    """Generate submission count bar chart."""

    counts = df["submitted"].value_counts()

    plt.figure(figsize=(5, 4))

    counts.plot(kind="bar")

    plt.title("Submission Status Count")
    plt.xlabel("Submitted")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def write_plot_summary(output_path):
    """Write explanation of generated plots."""

    summary = """
# Plot Summary

## 1. Domain Average Score
This bar chart compares the average score achieved by students across different domains.
It helps identify which domain performed the best overall.

## 2. Attendance vs Score
The scatter plot shows the relationship between attendance percentage and score.
It can be used to observe whether students with higher attendance generally score better.

## 3. Submission Status Count
This bar chart displays the number of students who submitted and did not submit the task.
It provides a quick overview of submission statistics.
"""

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(summary)