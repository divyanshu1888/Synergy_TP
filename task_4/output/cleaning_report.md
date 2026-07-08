
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
