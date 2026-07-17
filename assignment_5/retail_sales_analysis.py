import os
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("retail_sales.csv")

# -----------------------------
# Sample Data
# -----------------------------

def clean_data(df):
    # Remove duplicate records
    df = df.drop_duplicates().copy()
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
    df.to_csv("retail_sales_cleaned.csv", index=False)
    return df

def business_analysis(df):
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

def create_visualizations(df):
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
def generate_summary(df):
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
def main():
    global df

    print("\n========== PART A : DATA EXPLORATION ==========\n")

    print("First 10 Rows:")
    print(df.head(10))

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    df = clean_data(df)

    business_analysis(df)

    create_visualizations(df)

    generate_summary(df)  

if __name__ == "__main__":
    main()