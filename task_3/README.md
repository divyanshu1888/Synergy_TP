# Task 3: Manual CSV Parser and Pandas Comparison

## 1. Objective

Build a CSV parser by hand using only Python's built-in file I/O, then
perform the same analysis using pandas. Comparing the two outputs shows
that a hand-written parser, type conversion step, and summary
calculation can reproduce exactly what pandas does under the hood.

## 2. Folder Structure
task_3/

README.md

data/

submissions.csv

output/

manual_summary.json

pandas_summary.json

comparison_report.md

src/

manual_parser.py

pandas_parser.py

main.py

## 3. Required Packages

- Python 3.9+
- pandas

Install from the repository root:

pip install -r requirements.txt

## 4. Setup Instructions

1. Clone/open the Synergy_TP repository.
2. Create and activate a virtual environment (if not already done for
   the repo):
python -m venv venv

venv\Scripts\activate        # Windows

source venv/bin/activate     # macOS/Linux   

3. Install dependencies: pip install -r requirements.txt.

## 5. Exact Run Command

Run from the **repository root** (not from inside task_3/):
python task_3/src/main.py task_3/data/submissions.csv

## 6. Expected Output Files

- task_3/output/manual_summary.json
- task_3/output/pandas_summary.json
- task_3/output/comparison_report.md

## 7. Explanation of Implemented Logic
The manual parser processes the CSV file by opening it with open(), reading each line, splitting the values using commas, and storing the data as dictionaries. It also converts the required fields to appropriate data types before generating a summary. The pandas parser performs the same operations using pd.read_csv(). Finally, both outputs are exported as JSON files and their results are documented in a Markdown comparison report.
