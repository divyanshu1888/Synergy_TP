\# Task 4 - Messy CSV Cleaning



\## Objective



The objective of this task is to clean a messy CSV dataset using Python and pandas. The dataset contains duplicate records, inconsistent categories, missing values, invalid values, mixed units, and inconsistent data types. After cleaning, the dataset is validated and saved for further analysis and visualization.



\---



\## Folder Structure



task\_4/

│

├── data/

│   └── messy\_students.csv

│

├── output/

│   ├── cleaned\_students.csv

│   ├── summary\_before.json

│   ├── summary\_after.json

│   └── cleaning\_report.md

│

├── src/

│   ├── clean\_data.py

│   ├── validate\_data.py

│   └── main.py

│

└── README.md



\---



\## Required Packages



\- Python 3.x

\- pandas



Install pandas using:



pip install pandas



\---



\## Setup Instructions



Clone the repository and navigate to the project folder.



Make sure the input dataset exists at:



task\_4/data/messy\_students.csv



\---



\## Run Command



```bash

python task\_4/src/main.py task\_4/data/messy\_students.csv task\_4/output/cleaned\_students.csv

```



\---



\## Expected Output Files



After execution, the following files are generated:



\- cleaned\_students.csv

\- summary\_before.json

\- summary\_after.json

\- cleaning\_report.md



\---



\## Cleaning Logic



The program performs the following operations:



\- Removes duplicate records

\- Standardizes domain names

\- Converts attendance percentages into numeric values

\- Converts textual scores into numeric values

\- Converts study hours into numeric values

\- Converts height into centimeters

\- Converts weight into kilograms

\- Standardizes submitted values

\- Handles missing values using median imputation

\- Validates the cleaned dataset before saving



\---



\## Validation Rules



The cleaned dataset satisfies the following conditions:



\- No duplicate student IDs

\- Attendance between 0 and 100

\- Numeric score values

\- Numeric study hours

\- Numeric height values

\- Numeric weight values

\- Standardized domains

\- Standardized submission status

\- No missing values in critical columns

