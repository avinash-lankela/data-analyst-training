import pandas as pd

print("========== SALES ANALYTICS REPORT ==========\n")

# Task 1
df = pd.read_csv("sales_data.csv")

print("TASK 1: LOAD DATA")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# Task 2
print("\nTASK 2: DATASET OVERVIEW")

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Task 3
print("\nTASK 3: REVENUE METRICS")

total_revenue = df["Amount"].sum()
average_sale = df["Amount"].mean()
highest_sale = df["Amount"].max()
lowest_sale = df["Amount"].min()

print("Total Revenue:", total_revenue)
print("Average Sale:", average_sale)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)

# Task 4
print("\nTASK 4: EMPLOYEE PERFORMANCE REPORT")

employee_report = (
    df.groupby("salesperson")["Amount"]
      .sum()
      .sort_values(ascending=False)
)

print(employee_report)

# Task 5
print("\nTASK 5: REGIONAL PERFORMANCE REPORT")

region_report = (
    df.groupby("region")["Amount"]
      .sum()
      .sort_values(ascending=False)
)

print(region_report)

# Task 6
print("\nTASK 6: TOP PERFORMER DASHBOARD")

top_salesperson = employee_report.idxmax()
top_revenue = employee_report.max()

transaction_count = len(
    df[df["salesperson"] == top_salesperson]
)

print("Top Salesperson:", top_salesperson)
print("Revenue Generated:", top_revenue)
print("Transactions:", transaction_count)

# Task 7
print("\nTASK 7: HIGH VALUE TRANSACTIONS")

high_value = df[df["Amount"] > 1000]

print(high_value)

# Task 8
print("\nTASK 8: REVENUE CONTRIBUTION")

contribution = (
    df.groupby("salesperson")["Amount"]
      .sum()
      / total_revenue
      * 100
)

print(contribution.round(2))

# Task 9
print("\nTASK 9: DATA QUALITY CHECK")

bad_df = pd.read_csv("sales_data_bad.csv")

bad_df["Amount"] = pd.to_numeric(
    bad_df["Amount"],
    errors="coerce"
)

print(
    bad_df[
        bad_df["Amount"].isna()
    ]
)

# Stretch Goal 1
print("\nSTRETCH GOAL 1")

def revenue_category(amount):
    if amount >= 1200:
        return "High"
    elif amount >= 800:
        return "Medium"
    else:
        return "Low"

df["Revenue_Category"] = (
    df["Amount"]
      .apply(revenue_category)
)

print(
    df[
        ["order_id",
         "salesperson",
         "Amount",
         "Revenue_Category"]
    ]
)

# Stretch Goal 2
print("\nSTRETCH GOAL 2")

pivot_table = pd.pivot_table(
    df,
    index="salesperson",
    values="Amount",
    aggfunc="sum"
)

print(pivot_table)

# Stretch Goal 3
print("\nSTRETCH GOAL 3")

employee_report.to_csv(
    "employee_report.csv",
    header=["Total_Revenue"]
)

region_report.to_csv(
    "region_report.csv",
    header=["Total_Revenue"]
)

print("employee_report.csv created")
print("region_report.csv created")