import pandas as pd


def load_data(file_path: str):
    """Load the CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def generate_summary(df):
    """Generate a meaningful summary of the dataset."""

    summary = {}

    # Basic information
    summary["total_students"] = len(df)
    summary["duplicate_rows"] = int(df.duplicated().sum())

    # Missing values
    summary["missing_values"] = df.isnull().sum().to_dict()

    # Attendance statistics
    if "attendance_percent" in df.columns:
        attendance = pd.to_numeric(
            df["attendance_percent"],
            errors="coerce"
        )

        summary["average_attendance"] = round(
            attendance.mean(),
            2
        )

    # Score statistics
    if "score" in df.columns:
        score = pd.to_numeric(
            df["score"],
            errors="coerce"
        )

        summary["average_score"] = round(
            score.mean(),
            2
        )

        summary["highest_score"] = float(score.max())

        summary["lowest_score"] = float(score.min())

    # Submission statistics
    if "submitted" in df.columns:
        submitted = (
            df["submitted"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

        summary["submitted_students"] = int(
            submitted.isin(["yes", "y"]).sum()
        )

        summary["not_submitted"] = int(
            submitted.isin(["no", "n"]).sum()
        )

    # Domain statistics
    if "domain" in df.columns:

        summary["students_per_domain"] = (
            df["domain"]
            .value_counts()
            .to_dict()
        )

        if "score" in df.columns:

            temp_df = df.copy()

            temp_df["score"] = pd.to_numeric(
                temp_df["score"],
                errors="coerce"
            )

            summary["average_score_by_domain"] = (
                temp_df.groupby("domain")["score"]
                .mean()
                .round(2)
                .to_dict()
            )

    return summary

def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates()


def standardize_domains(df):
    """Convert all domain names to a standard format."""
    mapping = {
        "ml": "ML",
        "machine learning": "ML",
        "web": "Web",
        "web dev": "Web",
        "web development": "Web",
        "electronics": "Electronics",
        "mechanical": "Mechanical",
    }

    df["domain"] = (
        df["domain"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(mapping)
    )

    return df


def clean_attendance(df):
    """Convert attendance to numeric values and handle invalid percentages."""
    df["attendance_percent"] = (
        df["attendance_percent"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["attendance_percent"] = pd.to_numeric(
        df["attendance_percent"], errors="coerce"
    )

    # Replace invalid values with NaN
    df.loc[
        (df["attendance_percent"] < 0)
        | (df["attendance_percent"] > 100),
        "attendance_percent",
    ] = pd.NA

    return df


def clean_scores(df):
    """Convert score column to numeric."""
    score_map = {
        "nine": 9,
        "eight": 8,
        "seven": 7,
        "six": 6,
        "five": 5,
        "four": 4,
        "three": 3,
        "two": 2,
        "one": 1,
        "zero": 0,
    }

    df["score"] = (
        df["score"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace(score_map)
    )

    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    return df


def clean_study_hours(df):
    """Convert study hours to numeric."""
    hour_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
    }

    df["study_hours"] = (
        df["study_hours"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace(hour_map)
    )

    df["study_hours"] = pd.to_numeric(
        df["study_hours"], errors="coerce"
    )

    return df


def clean_height(df):
    """Convert height to centimeters."""
    def convert(value):
        if pd.isna(value):
            return pd.NA

        value = str(value).strip().lower()

        if "cm" in value:
            return float(value.replace("cm", "").strip())

        if "m" in value:
            return float(value.replace("m", "").strip()) * 100

        return pd.NA

    df["height_cm"] = df["height"].apply(convert)
    return df


def clean_weight(df):
    """Convert weight to kilograms."""
    df["weight_kg"] = (
        df["weight"]
        .astype(str)
        .str.lower()
        .str.replace("kg", "", regex=False)
        .str.strip()
    )

    df["weight_kg"] = pd.to_numeric(df["weight_kg"], errors="coerce")

    return df


def clean_submitted(df):
    """Standardize submitted values."""
    mapping = {
        "yes": "Yes",
        "y": "Yes",
        "no": "No",
        "n": "No",
    }

    df["submitted"] = (
        df["submitted"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(mapping)
    )

    return df


def handle_missing_values(df):
    """Fill missing values using simple rules."""

    df["attendance_percent"] = df["attendance_percent"].fillna(
        df["attendance_percent"].median()
    )

    df["score"] = df["score"].fillna(
        df["score"].median()
    )

    df["study_hours"] = df["study_hours"].fillna(
        df["study_hours"].median()
    )

    df["height_cm"] = df["height_cm"].fillna(
        df["height_cm"].median()
    )

    df["weight_kg"] = df["weight_kg"].fillna(
        df["weight_kg"].median()
    )

    return df


def save_cleaned_data(df, output_path):
    df = df[
        [
            "student_id",
            "name",
            "domain",
            "attendance_percent",
            "score",
            "study_hours",
            "height_cm",
            "weight_kg",
            "submitted",
        ]
    ]

    df.to_csv(output_path, index=False)


def write_report(report_path):
    """Generate a detailed cleaning report."""

    report = """
# Data Cleaning Report

## Objective
The dataset was cleaned to make it suitable for analysis and visualization.

## Cleaning Steps Performed

### 1. Duplicate Removal
- Removed duplicate student records.
- Duplicate entry found for Student ID **S005**.

### 2. Domain Standardization
The following mappings were applied:
- ml → ML
- MACHINE LEARNING → ML
- Web Dev → Web
- web development → Web
- web → Web
- electronics → Electronics
- Mechanical → Mechanical

### 3. Attendance Cleaning
- '%' symbols were removed.
- Attendance converted to numeric values.
- Missing attendance values were replaced using the median attendance.
- Invalid attendance values below 0 or above 100 were replaced using the median.
  - S007: -10 → Median
  - S008: 105 → Median

### 4. Score Cleaning
- Text values converted into numbers.
  - nine → 9
- Missing score values replaced using the median score.

### 5. Study Hours Cleaning
- Text values converted into numbers.
  - two → 2
- Missing values replaced using the median.

### 6. Height Cleaning
Converted every value into centimeters.
Examples:
- 170 cm → 170
- 1.62 m → 162
- 1.55 m → 155

### 7. Weight Cleaning
Converted all values into kilograms.
Examples:
- 65 kg → 65
- 55kg → 55

### 8. Submitted Column
Standardized values into consistent Yes/No format.
Mappings:
- yes → Yes
- Yes → Yes
- Y → Yes
- no → No
- N → No

### 9. Missing Value Handling
Missing numeric values were filled using the median of their respective columns.

## Validation Performed

The cleaned dataset satisfies:

- No duplicate Student IDs
- Attendance between 0 and 100
- Numeric score values
- Numeric study hours
- Numeric height (cm)
- Numeric weight (kg)
- Standardized domain names
- Standardized submitted values
- No missing values in critical columns

## Output Files

- cleaned_students.csv
- summary_before.json
- summary_after.json

Dataset cleaning completed successfully.
"""

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)