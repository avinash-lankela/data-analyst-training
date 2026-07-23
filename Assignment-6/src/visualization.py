import os
import pandas as pd
import matplotlib.pyplot as plt

def create_charts_folder():
    """Create charts folder if it doesn't exist."""
    os.makedirs("charts", exist_ok=True)

def calculate_churn_rate(df, group_column):
    """Calculate churn rate (%) for a given grouping."""

    churn_rate = (
        df.groupby(group_column)["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
    )

    return churn_rate

def plot_contract_type(df):
    """Bar chart for churn rate by contract type."""

    create_charts_folder()

    churn_rate = calculate_churn_rate(df, "Contract_Type")

    plt.figure(figsize=(8, 5))

    churn_rate.plot(kind="bar")

    plt.title("Churn Rate by Contract Type")
    plt.xlabel("Contract Type")
    plt.ylabel("Churn Rate (%)")

    plt.tight_layout()

    plt.savefig("charts/churn_by_contract.png")

    plt.close()

    print("✓ Contract Type chart saved.")

def plot_region(df):
    """Bar chart for churn rate by region."""

    create_charts_folder()

    churn_rate = calculate_churn_rate(df, "Region")

    plt.figure(figsize=(8, 5))

    churn_rate.plot(kind="bar")

    plt.title("Churn Rate by Region")
    plt.xlabel("Region")
    plt.ylabel("Churn Rate (%)")

    plt.tight_layout()

    plt.savefig("charts/churn_by_region.png")

    plt.close()

    print("✓ Region chart saved.")

def plot_churn_distribution(df):
    """Pie chart showing churn distribution."""

    create_charts_folder()

    churn_counts = df["Churn"].value_counts()

    plt.figure(figsize=(6, 6))

    plt.pie(
        churn_counts,
        labels=churn_counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )

    plt.title("Customer Churn Distribution")

    plt.savefig("charts/churn_distribution.png")

    plt.close()

    print("✓ Churn distribution chart saved.")

def plot_tenure(df):
    """Bar chart for churn rate by standardized tenure segment."""

    create_charts_folder()

    df["Tenure_Segment"] = pd.cut(
        df["Tenure_Months"],
        bins=[0, 12, 36, 1000],
        labels=[
            "New Customer",
            "Established Customer",
            "Long-Term Customer",
        ],
        include_lowest=True,
    )

    churn_rate = calculate_churn_rate(df, "Tenure_Segment")

    plt.figure(figsize=(8, 5))

    churn_rate.plot(kind="bar")

    plt.title("Churn Rate by Tenure Segment")
    plt.xlabel("Tenure Segment")
    plt.ylabel("Churn Rate (%)")

    plt.tight_layout()

    plt.savefig("charts/churn_by_tenure.png")

    plt.close()

    print("✓ Tenure chart saved.")

def plot_support_calls(df):
    """Bar chart for churn rate by support calls."""

    create_charts_folder()

    churn_rate = calculate_churn_rate(df, "Support_Calls")

    plt.figure(figsize=(8, 5))

    churn_rate.plot(kind="bar")

    plt.title("Churn Rate by Support Calls")
    plt.xlabel("Support Calls")
    plt.ylabel("Churn Rate (%)")

    plt.tight_layout()

    plt.savefig("charts/churn_by_support_calls.png")

    plt.close()

    print("✓ Support Calls chart saved.")