# Task 2: Python Recap Assignment

## Description

This folder contains the solution for Task 2 of the Synergy_TP project.

It demonstrates the use of Python functions, lists, dictionaries,
file handling, exception handling, type hints, and JSON output generation.

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/divyanshu1888/Synergy_TP.git

cd Synergy_TP

### 2. Install requirements

cd task_2

pip install -r requirements.txt

## Run the Python program

From the Synergy_TP root directory:

python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json

## Output

The program reads student submission data from
task_2/data/submissions.csv and generates a summary report in

task_2/output/summary.json

## Features

- Calculate total students
- Calculate submitted students
- Calculate missing submissions
- Calculate average score
- Find highest scorer
- Find lowest scorer among submitted students
- Calculate domain-wise average scores
- List students who did not submit
- List students scoring below 5

## Error Handling

The program handles:
- Missing input files
- Invalid score values
- Empty CSV files
- Missing output folders
