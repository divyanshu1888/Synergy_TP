import pandas as pd
import numpy as np
from scipy.stats import t


def load_data(file_path):
    return pd.read_csv(file_path)


def calculate_confidence_interval(mean, std, n):
    if n < 2:
        return np.nan, np.nan

    margin = t.ppf(0.975, n - 1) * (std / np.sqrt(n))
    return mean - margin, mean + margin


def assign_stability_flag(cv):
    if np.isnan(cv):
        return "unreliable"
    elif cv <= 0.05:
        return "stable"
    elif cv <= 0.15:
        return "moderate"
    else:
        return "unstable"


def calculate_replicate_statistics(df):

    groups = df.groupby([
        "domain",
        "condition",
        "input_type",
        "input_value",
        "input_unit",
        "signal_unit"
    ])

    result = []

    for name, group in groups:

        values = group["signal"].dropna().to_numpy()

        count = len(values)

        mean = np.mean(values)
        median = np.median(values)

        if count >= 2:
            variance = np.var(values, ddof=1)
            std = np.std(values, ddof=1)
            se = std / np.sqrt(count)
            low, high = calculate_confidence_interval(mean, std, count)
        else:
            variance = np.nan
            std = np.nan
            se = np.nan
            low = np.nan
            high = np.nan

        if mean != 0:
            cv = std / mean
        else:
            cv = np.nan

        result.append({
            "domain": name[0],
            "condition": name[1],
            "input_type": name[2],
            "input_value": name[3],
            "input_unit": name[4],
            "signal_unit": name[5],
            "replicate_count": count,
            "mean_signal": mean,
            "median_signal": median,
            "variance_signal": variance,
            "standard_deviation_signal": std,
            "standard_error_signal": se,
            "confidence_interval_lower": low,
            "confidence_interval_upper": high,
            "coefficient_of_variation": cv,
            "minimum_signal": np.min(values),
            "maximum_signal": np.max(values),
            "stability_flag": assign_stability_flag(cv)
        })

    return pd.DataFrame(result)


def save_replicate_summary(summary_df, output_path):
    summary_df.to_csv(output_path, index=False)