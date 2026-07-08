import pandas as pd


def validate_cleaned_data(df):
    """Validate the cleaned dataset."""

    if df["student_id"].duplicated().any():
        return False

    if not df["attendance_percent"].between(0, 100).all():
        return False

    numeric_columns = [
        "score",
        "study_hours",
        "height_cm",
        "weight_kg",
    ]

    for column in numeric_columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            return False

    if not set(df["submitted"]).issubset({"Yes", "No"}):
        return False

    if not set(df["domain"]).issubset(
        {"ML", "Web", "Electronics", "Mechanical"}
    ):
        return False

    critical_columns = [
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

    if df[critical_columns].isnull().any().any():
        return False

    return True