\# Task 5 – Data Visualization using Matplotlib



\## Objective



The objective of this task is to visualize the cleaned student dataset generated in Task 4. The plots provide insights into student performance, attendance, and submission statistics using Matplotlib.



\---



\## Folder Structure



task\_5/

│

├── output/

│   ├── attendance\_vs\_score.png

│   ├── domain\_average\_score.png

│   ├── submission\_status\_count.png

│   └── plot\_summary.md

│

├── src/

│   ├── visualize.py

│   └── main.py

│

└── README.md



\---



\## Required Packages



\- Python 3.x

\- pandas

\- matplotlib



Install the required packages:



```bash

pip install pandas matplotlib

```



\---



\## Input File



This task uses the cleaned dataset generated in Task 4.



```

task\_4/output/cleaned\_students.csv

```



\---



\## Run Command



```bash

python task\_5/src/main.py task\_4/output/cleaned\_students.csv task\_5/output

```



\---



\## Generated Output



Running the program creates:



\- domain\_average\_score.png

\- attendance\_vs\_score.png

\- submission\_status\_count.png

\- plot\_summary.md



\---



\## Visualization Details



\### Domain Average Score



Displays the average score achieved by students in each domain using a bar chart.



\### Attendance vs Score



Displays the relationship between attendance percentage and score using a scatter plot.



\### Submission Status Count



Displays the number of students who submitted and did not submit the assignment using a bar chart.



\---



\## Libraries Used



\- pandas

\- matplotlib.pyplot



\---



\## Features



\- Reads cleaned CSV data

\- Generates three plots

\- Saves figures automatically

\- Uses proper titles and axis labels

\- Uses tight\_layout() for clean formatting

\- Does not require manually opening plot windows

