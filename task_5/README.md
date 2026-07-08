# Task 5 – Data Visualization using Matplotlib



## Objective



The objective of this task is to visualize the cleaned student dataset generated in Task 4. The plots provide insights into student performance, attendance, and submission statistics using Matplotlib.





## Folder Structure



task_5/

│

├── output

│   ├── attendance_vs_score.png

│   ├── domain_average_score.png

│   ├── submission_status_count.png

│   └── plot_summary.md

│

├── src

│   ├── visualize.py

│   └── main.py

│

└── README.md



## Required Packages



- Python 3.x

- pandas

- matplotlib


Install the required packages:


pip install pandas matplotlib





## Input File



This task uses the cleaned dataset generated in Task 4.




task_4/output/cleaned_students.csv



## Run Command



python task_5/src/main.py task_4/output/cleaned_students.csv task\_5/output



## Generated Output



Running the program creates:



- domain_average_score.png

- attendance_vs_score.png

- submission_status_count.png

- plot_summary.md




## Visualization Details



### Domain Average Score



Displays the average score achieved by students in each domain using a bar chart.



### Attendance vs Score



Displays the relationship between attendance percentage and score using a scatter plot.



### Submission Status Count



Displays the number of students who submitted and did not submit the assignment using a bar chart.





## Libraries Used



- pandas

- matplotlib.pyplot





## Features



- Reads cleaned CSV data

- Generates three plots

- Saves figures automatically

- Uses proper titles and axis labels

- Uses tight\_layout() for clean formatting

- Does not require manually opening plot windows

