import pandas as pd

# Read CSV file
df = pd.read_csv("sales_data.csv")

print("\n===== CSV SALES REPORT =====")

# Total Revenue
total_revenue = df["Amount"].sum()
print(f"\nTotal Revenue: ${total_revenue}")

# Average Transaction Amount
average_transaction = df["Amount"].mean()
print(f"Average Transaction Amount: ${average_transaction:.2f}")

# Sales by Employee
print("\nSales by Employee:")
sales_by_employee = df.groupby("Salesperson")["Amount"].sum()
print(sales_by_employee)

# Sales by Region
print("\nSales by Region:")
sales_by_region = df.groupby("Region")["Amount"].sum()
print(sales_by_region)

# Top Salesperson
top_salesperson = sales_by_employee.idxmax()
top_sales_amount = sales_by_employee.max()

print("\nTop Salesperson:")
print(f"{top_salesperson} (${top_sales_amount})")

# Largest Transaction
largest_transaction = df["Amount"].max()

print("\nLargest Transaction:")
print(f"${largest_transaction}")

# Transactions Above $1000
print("\nTransactions Above $1000:")
print(df[df["Amount"] > 1000])

# ---------------------------
# Stretch Goal 1
# Revenue Contribution %
# ---------------------------
print("\nRevenue Contribution Percentage:")

revenue_percent = (sales_by_employee / total_revenue) * 100

for employee, percent in revenue_percent.items():
    print(f"{employee}: {percent:.2f}%")

# ---------------------------
# Stretch Goal 2
# Highest Revenue Region
# ---------------------------
highest_region = sales_by_region.idxmax()
highest_region_sales = sales_by_region.max()

print("\nHighest Revenue Region:")
print(f"{highest_region} (${highest_region_sales})")

# ---------------------------
# Stretch Goal 3
# Sort Employees by Revenue
# ---------------------------
print("\nEmployees Sorted By Revenue:")

sorted_employees = sales_by_employee.sort_values(ascending=False)

print(sorted_employees)

# ---------------------------
# Data Quality Exercise
# ---------------------------
print("\n===== DATA QUALITY REPORT =====")

try:
    bad_df = pd.read_csv("sales_data_bad.csv")

    bad_df["Amount"] = pd.to_numeric(
        bad_df["Amount"],
        errors="coerce"
    )

    cleaned_df = bad_df.dropna(subset=["Amount"])

    print("\nValid Records:")
    print(cleaned_df)

    print("\nTotal Revenue From Valid Records:")
    print(cleaned_df["Amount"].sum())

except FileNotFoundError:
    print("sales_data_bad.csv not found")