# Comparison Report: Manual Parser vs Pandas

This report compares the summary produced by the hand-written CSV parser (`manual_parser.py`) against the summary produced by pandas (`pandas_parser.py`) for the same input file, `task_3/data/submissions.csv`.

## Field-by-field comparison

| Field | Manual Parser | Pandas | Match |
| --- | --- | --- | --- |
| total_students | 7 | 7 | Yes |
| num_submitted | 5 | 5 | Yes |
| num_missing_submissions | 2 | 2 | Yes |
| average_score | 4.86 | 4.86 | Yes |
| highest_scorer | {'name': 'Isha', 'score': 9} | {'name': 'Isha', 'score': 9} | Yes |
| lowest_scorer_submitted | {'name': 'Rohan', 'score': 4} | {'name': 'Rohan', 'score': 4} | Yes |
| domain_average_score | {'ML': 5.0, 'Web': 5.0, 'Electronics': 9.0, 'Mechanical': 0.0} | {'Electronics': 9.0, 'ML': 5.0, 'Mechanical': 0.0, 'Web': 5.0} | Yes |
| students_not_submitted | ['Kabir', 'Dev'] | ['Kabir', 'Dev'] | Yes |
| students_below_5 | ['Kabir', 'Rohan', 'Dev'] | ['Kabir', 'Rohan', 'Dev'] | Yes |

## Conclusion

Both the manual parser and pandas produced identical results for every field in the summary. This confirms that the hand-written CSV reading, type conversion, and aggregation logic behaves equivalently to pandas' built-in CSV loading and groupby/aggregation functions for this dataset.
