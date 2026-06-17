# CSV Sales Report Generator

## Assignment Overview

This project reads sales transaction data from CSV files and generates a detailed sales report using traditional Python programming techniques without using Pandas.

The program processes sales records, calculates key business metrics, handles invalid data, and generates summary reports for management review.

---

## Technologies Used

* Python 3
* CSV Module (Built-in Library)

No external libraries such as Pandas or NumPy were used.

---

## Project Files

### 1. sales_data.csv

Contains valid sales transaction records.

### 2. sales_data_bad.csv

Contains valid records along with invalid and missing transaction amounts for data quality testing.

### 3. csv_sales_report.py

Main Python script that processes CSV files and generates reports.

### 4. README.md

Project documentation.

---

## Features Implemented

### Core Requirements

* Read CSV file and store records
* Calculate Total Revenue
* Calculate Average Transaction Amount
* Generate Sales by Employee Report
* Generate Sales by Region Report
* Determine Top Salesperson
* Find Largest Transaction
* Display Transactions Above $1000

### Data Quality Handling

The program detects and skips:

* Missing transaction amounts
* Invalid transaction amounts (non-numeric values)

Processing continues without terminating the program.

### Stretch Goals Completed

* Revenue Contribution Percentage by Salesperson
* Highest Revenue Region
* Employees Sorted by Revenue (Descending Order)

---

## How to Run

Open terminal in the project folder and execute:

```bash
python csv_sales_report.py
```

or

```bash
python3 csv_sales_report.py
```

---

## Sample Output

The program displays:

* Total Revenue
* Average Transaction Amount
* Sales by Employee
* Sales by Region
* Top Salesperson
* Highest Revenue Region
* Largest Transaction
* Transactions Above $1000
* Revenue Contribution Percentage
* Employees Sorted by Revenue

---

## Learning Outcomes

Through this assignment, the following Python concepts were practiced:

* File Handling
* CSV Processing
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* Data Aggregation
* Sorting and Reporting

---

## Repository

data-analyst-training

## Commit Message

Completed Assignment 3 - CSV Sales Report Generator
