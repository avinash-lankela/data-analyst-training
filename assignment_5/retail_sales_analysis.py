import matplotlib.pyplot as plt
import os
import pandas as pd
import random
from datetime import datetime, timedelta
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# -----------------------------
# Sample Data
# -----------------------------

customers = [
    "John","Alice","David","Sophia","Emma",
    "James","Michael","Olivia","Daniel","Liam",
    "Noah","Mia","Charlotte","Ava","William"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

categories = {
    "Electronics":["Laptop","Mobile","Headphones","Monitor","Keyboard"],
    "Furniture":["Chair","Table","Sofa","Cupboard","Desk"],
    "Clothing":["T-Shirt","Jeans","Jacket","Shoes","Cap"],
    "Groceries":["Rice","Milk","Bread","Eggs","Oil"]
}

salespersons = [
    "Rahul",
    "Priya",
    "Amit",
    "Sneha",
    "Kiran",
    "Ravi",
    "Pooja"
]

# -----------------------------
# Generate Records
# -----------------------------

records = []

start_date = datetime(2025,1,1)

for i in range(500):

    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])

    quantity = random.randint(1,10)

    if category=="Electronics":
        price = random.randint(5000,50000)

    elif category=="Furniture":
        price = random.randint(2000,20000)

    elif category=="Clothing":
        price = random.randint(300,5000)

    else:
        price = random.randint(50,1000)

    order_date = start_date + timedelta(days=random.randint(0,364))

    records.append([
        i+1,
        order_date.strftime("%Y-%m-%d"),
        random.choice(customers),
        random.choice(regions),
        category,
        product,
        quantity,
        price,
        random.choice(salespersons)
    ])

columns = [
    "Order_ID",
    "Order_Date",
    "Customer",
    "Region",
    "Category",
    "Product",
    "Quantity",
    "Unit_Price",
    "Salesperson"
]

df = pd.DataFrame(records,columns=columns)
# -----------------------------
# Add Missing Values (5%)
# -----------------------------

for col in df.columns:
    if col != "Order_ID":
        missing_rows = df.sample(frac=0.05).index
        df.loc[missing_rows, col] = None
    # -----------------------------
# Add Duplicate Records
# -----------------------------

duplicates = df.sample(10)

df = pd.concat([df,duplicates],ignore_index=True)
# -----------------------------
# Add Outliers
# -----------------------------

outlier_rows = df.sample(5).index

df.loc[outlier_rows,"Unit_Price"] = [
    200000,
    300000,
    250000,
    500000,
    750000
]
# -----------------------------
# Save Dataset
# -----------------------------

df.to_csv("retail_sales.csv",index=False)

print("\n========== PART A : DATA EXPLORATION ==========\n")

# Display first 10 rows
print("First 10 Rows:")
print(df.head(10))

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())
# Remove duplicate records
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)
# Categorical columns
df["Customer"] = df["Customer"].fillna("Unknown")
df["Region"] = df["Region"].fillna("Unknown")
df["Category"] = df["Category"].fillna("Unknown")
df["Product"] = df["Product"].fillna("Unknown")
df["Salesperson"] = df["Salesperson"].fillna("Unknown")

# Numeric columns
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())

# Date column
df["Order_Date"] = df["Order_Date"].fillna(df["Order_Date"].mode()[0])

# Check if missing values are removed
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# ==============================
# PART B : FEATURE ENGINEERING
# ==============================
# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Unit_Price"]
# Extract Month from Order_Date
df["Month"] = df["Order_Date"].dt.month_name()
print("\nDataset After Feature Engineering:")
print(df.head())
# Save updated dataset
df.to_csv("retail_sales.csv", index=False)
print("\n========== PART C : BUSINESS ANALYSIS ==========\n")
total_revenue = df["Revenue"].sum()

print("1. Total Company Revenue:")
print(total_revenue)
monthly_revenue = df.groupby("Month")["Revenue"].sum()

print("\n2. Monthly Revenue:")
print(monthly_revenue)
region_revenue = df.groupby("Region")["Revenue"].sum()

print("\n3. Revenue by Region:")
print(region_revenue)

print("\nHighest Revenue Region:")
print(region_revenue.idxmax())
category_revenue = df.groupby("Category")["Revenue"].sum()

print("\n4. Revenue by Category:")
print(category_revenue)

print("\nHighest Performing Category:")
print(category_revenue.idxmax())
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)

print("\n5. Top 5 Products by Revenue:")
print(top_products)
salesperson_summary = df.groupby("Salesperson").agg(
    Total_Revenue=("Revenue", "sum"),
    Number_of_Orders=("Order_ID", "count"),
    Average_Order_Value=("Revenue", "mean")
)

print("\n6. Salesperson Performance:")
print(salesperson_summary)
customer_revenue = df.groupby("Customer")["Revenue"].sum()

print("\n7. Customer with Highest Revenue:")
print(customer_revenue.idxmax())
largest_order = df.loc[df["Revenue"].idxmax()]

print("\n8. Largest Order:")
print(largest_order)
print("\n9. Revenue Distribution Across Categories:")
print(category_revenue)
Q1 = df["Revenue"].quantile(0.25)
Q3 = df["Revenue"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Revenue"] < lower) | (df["Revenue"] > upper)]

print("\n10. Outliers:")
print(outliers)

print("\nNumber of Outliers:")
print(len(outliers))
# Create charts folder
os.makedirs("charts", exist_ok=True)
monthly_revenue = df.groupby("Month")["Revenue"].sum()

# Arrange months in calendar order
month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_revenue = monthly_revenue.reindex(month_order)

plt.figure(figsize=(10,5))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_revenue.png")
plt.close()
region_revenue = df.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(8,5))
plt.bar(region_revenue.index, region_revenue.values)
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/revenue_by_region.png")
plt.close()
category_revenue = df.groupby("Category")["Revenue"].sum()

plt.figure(figsize=(7,7))
plt.pie(
    category_revenue,
    labels=category_revenue.index,
    autopct='%1.1f%%'
)
plt.title("Revenue by Category")
plt.savefig("charts/revenue_by_category.png")
plt.close()
top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
plt.barh(top_products.index, top_products.values)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig("charts/top10_products.png")
plt.close()
salesperson_revenue = df.groupby("Salesperson")["Revenue"].sum()

plt.figure(figsize=(8,5))
plt.bar(salesperson_revenue.index, salesperson_revenue.values)
plt.title("Salesperson Revenue")
plt.xlabel("Salesperson")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/salesperson_revenue.png")
plt.close()
print("\nAll charts have been saved successfully inside the 'charts' folder.")
# =====================================
# PART E - SUMMARY REPORT
# =====================================

summary = df.groupby("Region").agg(
    Revenue=("Revenue", "sum"),
    Orders=("Order_ID", "count"),
    Average_Revenue_per_Order=("Revenue", "mean")
)

summary = summary.reset_index()

summary.to_csv("retail_sales_summary.csv", index=False)

print("\nRetail Sales Summary CSV created successfully!")
print(summary)
def create_dataset():
    ...

def clean_data():
    ...

def business_analysis():
    ...

def create_visualizations():
    ...

def generate_summary():
    ...