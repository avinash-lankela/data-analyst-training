# CSV Sales Report Generator

## Overview

This project analyzes sales transaction data stored in CSV files and generates business reports using Python.

## Files

* sales_data.csv – Original sales dataset
* sales_data_bad.csv – Dataset containing invalid and missing values for data quality testing
* csv_sales_report.py – Main Python script
* README.md – Project documentation

## Features

### Required Tasks

1. Read sales data from CSV
2. Calculate Total Revenue
3. Calculate Average Transaction Amount
4. Generate Sales by Employee Report
5. Generate Sales by Region Report
6. Identify Top Salesperson
7. Find Largest Transaction
8. Display Transactions Above $1000

### Data Quality Handling

* Skips records with missing amounts
* Skips records with invalid amounts
* Continues processing without crashing

### Stretch Goals

* Revenue contribution percentage by salesperson
* Highest revenue region
* Employee ranking by revenue (descending)

## Requirements

* Python 3.x
* Pandas

## Installation

```bash
pip install pandas
```

## Run the Program

```bash
python3 csv_sales_report.py
```

## Repository

data-analyst-training
