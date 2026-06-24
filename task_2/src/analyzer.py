import pandas as pd
import numpy as np
import json
import os


# Function 1: Read the CSV file and return a DataFrame
def read_submissions(file_path: str) -> pd.DataFrame:
    # Check if the file exists before trying to open it
    if not os.path.exists(file_path):
        print("Error: File not found -", file_path)
        return pd.DataFrame()  # Return an empty table if file is missing

    # Read the CSV file into a pandas DataFrame (like a table)
    df = pd.read_csv(file_path)

    # Check if the file was empty
    if df.empty:
        print("Error: The CSV file is empty.")
        return pd.DataFrame()

    # Make sure the score column has numbers only
    # If something is not a number, replace it with 0
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df["score"] = df["score"].fillna(0)

    return df


# -----------------------------------------------------------
# Function 2: Get only the students who submitted
# -----------------------------------------------------------
def get_submitted_students(df: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where the "submitted" column says "yes"
    submitted = df[df["submitted"] == "yes"]
    return submitted


# Function 3: Calculate the average score of all students
def calculate_average_score(df: pd.DataFrame) -> float:
    # Get the score column as a numpy array
    scores = df["score"].values 

    # Use numpy to calculate the average (mean)
    average = np.mean(scores)

    # Round it to 2 decimal places so it looks clean
    average = round(float(average), 2)

    return average


# Function 4: Find the average score for each domain
def get_domain_wise_average(df: pd.DataFrame) -> dict:
    # Get the list of unique domains (e.g., ML, Web, Electronics)
    all_domains = df["domain"].unique()

    # Create an empty dictionary to store results
    domain_averages = {}

    # Go through each domain one by one
    for domain in all_domains:
        # Filter rows that belong to this domain
        domain_rows = df[df["domain"] == domain]

        # Get the scores as a numpy array
        scores = domain_rows["score"].values

        # Calculate average using numpy
        avg = np.mean(scores)

        # Save it in the dictionary, rounded to 2 decimal places
        domain_averages[domain] = round(float(avg), 2)

    return domain_averages


# Function 5: Get students who did NOT submit
def get_missing_submissions(df: pd.DataFrame) -> list:
    # Filter rows where submitted is "no"
    missing = df[df["submitted"] == "no"]

    # Get the names as a plain Python list
    missing_names = missing["name"].tolist()

    return missing_names


# Function 6: Write the summary to a JSON file
def write_summary(summary: dict, output_path: str) -> None:
    # Make sure the output folder exists, create it if it doesn't
    output_folder = os.path.dirname(output_path)
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write the dictionary as a JSON file
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=4)

    print("Summary written to:", output_path)
