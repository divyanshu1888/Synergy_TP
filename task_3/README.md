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

1. Clone/open the `Synergy_TP` repository.
2. Create and activate a virtual environment (if not already done for
   the repo):
python -m venv venv

venv\Scripts\activate        # Windows

source venv/bin/activate     # macOS/Linux   

3. Install dependencies: `pip install -r requirements.txt`.

## 5. Exact Run Command

Run from the **repository root** (not from inside `task_3/`):
python task_3/src/main.py task_3/data/submissions.csv

## 6. Expected Output Files

- `task_3/output/manual_summary.json`
- `task_3/output/pandas_summary.json`
- `task_3/output/comparison_report.md`

## 7. Explanation of Implemented Logic

**`manual_parser.py`**
- `read_csv_manual()` opens the file with a context manager, reads the
  header line, then splits every remaining line on commas. Blank lines
  are skipped, and any line whose number of comma-separated values
  doesn't match the header length is treated as malformed and skipped
  (with a printed warning) instead of crashing the program.
- `convert_types()` converts the `score` field to `int` and the
  `submitted` field to `bool` (`yes`/`y`/`true`/`1` -> `True`,
  everything else -> `False`). Rows with a non-numeric score are
  skipped the same way malformed rows are.
- `calculate_summary()` computes all nine required statistics
  using plain Python loops and dict/list comprehensions.
- `write_json()` writes any dict to disk as pretty-printed JSON.

**`pandas_parser.py`**
- `read_csv_pandas()` loads the same CSV with `pd.read_csv()` and
  applies the identical `score`/`submitted` normalization rules as the
  manual parser, so the two outputs are directly comparable.
- `calculate_summary_pandas()` computes the same nine statistics using
  pandas idioms (`groupby`, `mean`, `idxmax`/`idxmin`, boolean
  indexing).

**`main.py`**
- Runs both parsers on the path passed as a command-line argument,
  writes both summary JSON files, then compares the two summaries
  field-by-field and writes `comparison_report.md`.

On the provided `submissions.csv`, all nine fields match exactly
between the manual parser and pandas, confirming the manual
implementation is correct.