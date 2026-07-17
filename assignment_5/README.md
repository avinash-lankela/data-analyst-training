# Retail Sales Performance - Exploratory Data Analysis (EDA)

## Project Objective
The objective of this project is to analyze retail sales data by performing data cleaning, feature engineering, business analysis, outlier detection, and data visualization to generate meaningful business insights.

---

## Dataset Description

The dataset contains **500 retail sales records** with the following columns:

- Order_ID
- Order_Date
- Customer
- Region
- Category
- Product
- Quantity
- Unit_Price
- Salesperson
- Revenue
- Month

The dataset includes:

- Missing values
- Duplicate records
- Outliers
- One full year of retail sales data

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- NumPy

---

## Project Files

```
assignment_5/
│
├── generate_data.py
├── retail_sales_analysis.py
├── retail_sales.csv
├── retail_sales_cleaned.csv
├── retail_sales_summary.csv
├── README.md
│
└── charts/
    ├── monthly_revenue.png
    ├── revenue_by_region.png
    ├── revenue_by_category.png
    ├── top10_products.png
    └── salesperson_revenue.png
```

---

## Analysis Performed

1. Generated the retail sales dataset.
2. Loaded the dataset using Pandas.
3. Displayed the first 10 rows.
4. Displayed dataset shape.
5. Displayed column names.
6. Checked data types.
7. Identified missing values.
8. Removed duplicate records.
9. Filled missing values.
10. Converted Order_Date to datetime.
11. Created Revenue and Month columns.
12. Performed business analysis.
13. Calculated monthly revenue.
14. Calculated region-wise revenue.
15. Calculated category-wise revenue.
16. Identified top 5 products.
17. Evaluated salesperson performance.
18. Detected revenue outliers using the IQR method.
19. Generated charts.
20. Created a summary report.

---

## Visualizations

The project generates the following charts automatically:

- Monthly Revenue (Line Chart)
- Revenue by Region (Bar Chart)
- Revenue by Category (Pie Chart)
- Top 10 Products by Revenue (Horizontal Bar Chart)
- Salesperson Revenue (Bar Chart)

All charts are saved inside the **charts/** folder.

---

## Key Findings

- Calculated total company revenue.
- Identified monthly revenue trends.
- Determined the highest revenue region.
- Identified the best-performing product category.
- Listed the top 5 revenue-generating products.
- Evaluated salesperson performance.
- Identified the highest revenue customer.
- Displayed the largest order.
- Detected revenue outliers.

---

## How to Run the Project

### Install Required Libraries

```bash
pip install pandas matplotlib numpy
```

### Generate the Dataset

```bash
python generate_data.py
```

### Run the Analysis

```bash
python retail_sales_analysis.py
```

---

## Output

After execution, the project generates:

- retail_sales_cleaned.csv
- retail_sales_summary.csv
- Five visualization charts inside the `charts/` folder

---

#