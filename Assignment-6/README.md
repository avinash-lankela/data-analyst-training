# Customer Churn Analysis

## Project Objective

The objective of this project is to analyze customer churn by generating a synthetic customer dataset, cleaning the data, calculating key performance indicators (KPIs), performing business analysis, segmenting customers based on churn risk, and creating visualizations to support data-driven business decisions.

---

## Dataset Description

The generated dataset contains customer information, including:

- Customer ID
- Age
- Gender
- Region
- Tenure (Months)
- Contract Type
- Monthly Charges
- Total Charges
- Support Calls
- Payment Method
- Internet Service
- Premium Subscription
- Churn Status

The dataset intentionally includes missing values and duplicate records to demonstrate data cleaning techniques.

---

## Features

- Synthetic customer churn dataset generation
- Missing value handling
- Duplicate record removal
- Exploratory Data Analysis (EDA)
- KPI calculation
- Business analysis
- Customer risk segmentation
- Data visualization
- Churn summary report generation

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

---

## Project Structure

```
Assignment-6/
│
├── data/
│   ├── customer_churn.csv
│   ├── customer_churn_cleaned.csv
│   └── churn_summary.csv
│
├── charts/
│   ├── churn_by_contract.png
│   ├── churn_by_region.png
│   ├── churn_distribution.png
│   ├── churn_by_tenure.png
│   └── churn_by_support_calls.png
│
├── src/
│   ├── analysis.py
│   ├── data_cleaning.py
│   ├── data_generator.py
│   ├── report.py
│   ├── summary.py
│   └── visualization.py
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Data Cleaning

The following preprocessing steps are performed:

- Removed duplicate records
- Filled missing numerical values using the median
- Filled missing categorical values using the mode
- Verified that no missing values remained after cleaning
- Saved the cleaned dataset for further analysis

---

## Business Analysis Performed

The project analyzes customer churn based on:

- Contract Type
- Region
- Gender
- Tenure
- Monthly Charges
- Support Calls
- Premium Subscription

It also calculates:

- Total Customers
- Churned Customers
- Retained Customers
- Churn Rate
- Retention Rate

---

## Customer Risk Segmentation

Customers are classified into three risk levels:

- **High Risk**
  - Tenure less than 12 months
  - Support Calls greater than or equal to 5
  - Monthly Charges greater than 100

- **Medium Risk**
  - Tenure less than 24 months
  - OR Support Calls greater than or equal to 3

- **Low Risk**
  - All remaining customers

---

## Visualizations Generated

The project generates the following charts:

- Churn by Contract Type
- Churn by Region
- Overall Churn Distribution
- Churn by Tenure
- Churn by Support Calls

All charts are saved inside the **charts/** folder.

---

## Generated Files

### Data

- customer_churn.csv
- customer_churn_cleaned.csv
- churn_summary.csv

### Charts

- churn_by_contract.png
- churn_by_region.png
- churn_distribution.png
- churn_by_tenure.png
- churn_by_support_calls.png

---

## Key Business Insights

- Overall churn rate is approximately **41.16%**.
- Customers with **Monthly contracts** have the highest churn rate.
- Customers with **less than one year of tenure** are more likely to churn.
- Customers making **five or more support calls** show significantly higher churn.
- Long-term customers have a much lower churn rate.

---

## Business Recommendations

- Encourage customers to switch from monthly contracts to long-term plans.
- Improve onboarding and engagement during the first year.
- Monitor customers with frequent support calls and provide proactive assistance.
- Offer retention discounts or loyalty rewards to high-risk customers.
- Continuously monitor customer risk levels to reduce future churn.

---

## How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python run.py
```

---

## Output

After execution, the project automatically:

- Generates the customer churn dataset
- Cleans the dataset
- Performs business analysis
- Segments customers by risk level
- Creates visualizations
- Generates the churn summary report

---

