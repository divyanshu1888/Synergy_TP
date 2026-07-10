# Task 9 - Calibration Data Analysis Pipeline

## Overview

This project implements a complete calibration data analysis pipeline using Python. The pipeline processes raw calibration measurements, performs statistical analysis, analyzes calibration relationships, engineers machine learning features, and generates output reports and visualizations.

The project is divided into three major parts:

1. Replicate Statistics
2. Correlation & Calibration Analysis
3. Feature Engineering


## Project Structure

```
task_9/
│
├── data/
│   └── calibration_measurements.csv
│
├── output/
│   ├── replicate_summary.csv
│   ├── correlation_summary.csv
│   ├── calibration_summary.csv
│   ├── engineered_features.csv
│   ├── ml_ready_dataset.csv
│   ├── calibration_curve_biochem.png
│   ├── calibration_curve_electronics.png
│   ├── calibration_curve_mechanical.png
│   └── correlation_signal_input.png
│
├── src/
│   ├── main.py
│   ├── replicate_statistics.py
│   ├── correlation_analysis.py
│   └── feature_engineering.py
│
└── README.md
```

---

## Features

### Part 1 - Replicate Statistics

- Loads calibration measurement data
- Groups replicate measurements
- Calculates:
  - Mean
  - Standard Deviation
  - Coefficient of Variation (CV)
- Assigns stability flags
- Computes confidence intervals
- Generates:
  - `replicate_summary.csv`

---

### Part 2 - Correlation Analysis

Performs statistical analysis between calibration variables.

Calculates:

- Pearson Correlation
- Spearman Correlation
- Linear Regression
- Slope
- Intercept
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Generates:

- `correlation_summary.csv`
- `calibration_summary.csv`
- Calibration plots
- Scatter plot

---

### Part 3 - Feature Engineering

Creates additional features including:

- Rolling Average Signal
- Normalized Signal
- Power (Electronics)
- Error Percentage
- Stress Ratio (Mechanical)
- ML Readiness Flag

Generates:

- `engineered_features.csv`
- `ml_ready_dataset.csv`

---

## Requirements

Install the required libraries:

```bash
pip install pandas numpy scipy matplotlib scikit-learn
```

---

## Running the Project

From the project directory execute:

```bash
python src/main.py data/calibration_measurements.csv output
```

---

## Output Files

| File | Description |
|------|-------------|
| replicate_summary.csv | Replicate statistics |
| correlation_summary.csv | Correlation and regression metrics |
| calibration_summary.csv | Calibration model summary |
| engineered_features.csv | Dataset with engineered features |
| ml_ready_dataset.csv | Filtered ML-ready records |
| calibration_curve_*.png | Calibration plots |
| correlation_signal_input.png | Scatter plot of signal vs input |


## Packages Used

- Pandas
- NumPy
- SciPy
- Matplotlib
- Scikit-learn


## Author
**Divyanshu Penta**

GitHub: divyanshu1888
