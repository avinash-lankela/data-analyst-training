import os
import matplotlib.pyplot as plt


def create_charts_folder():
    """Create charts folder if it doesn't exist."""
    os.makedirs("charts", exist_ok=True)


def plot_contract_type(df):
    """Bar chart for churn by contract type."""

    create_charts_folder()

    churn_data = (
        df[df["Churn"] == "Yes"]
        .groupby("Contract_Type")
        .size()
    )

    plt.figure(figsize=(8, 5))

    churn_data.plot(kind="bar")

    plt.title("Churn by Contract Type")
    plt.xlabel("Contract Type")
    plt.ylabel("Number of Churned Customers")

    plt.tight_layout()

    plt.savefig("charts/churn_by_contract.png")

    plt.close()

    print("✓ Contract Type chart saved.")

def plot_region(df):
    """Bar chart for churn by region."""

    create_charts_folder()

    churn_data = (
        df[df["Churn"] == "Yes"]
        .groupby("Region")
        .size()
    )

    plt.figure(figsize=(8, 5))

    churn_data.plot(kind="bar")

    plt.title("Churn by Region")
    plt.xlabel("Region")
    plt.ylabel("Number of Churned Customers")

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
    """Bar chart for churn by tenure segment."""

    create_charts_folder()

    df["Tenure_Segment"] = df["Tenure_Months"].apply(
        lambda x:
        "New"
        if x <= 12
        else "Established"
        if x <= 36
        else "Long-Term"
    )

    churn_data = (
        df[df["Churn"] == "Yes"]
        .groupby("Tenure_Segment")
        .size()
    )

    plt.figure(figsize=(8, 5))

    churn_data.plot(kind="bar")

    plt.title("Churn by Tenure Segment")
    plt.xlabel("Tenure Segment")
    plt.ylabel("Number of Churned Customers")

    plt.tight_layout()

    plt.savefig("charts/churn_by_tenure.png")

    plt.close()

    print("✓ Tenure chart saved.")

def plot_support_calls(df):
    """Bar chart for support calls vs churn."""

    create_charts_folder()

    churn_data = (
        df[df["Churn"] == "Yes"]
        .groupby("Support_Calls")
        .size()
    )

    plt.figure(figsize=(8, 5))

    churn_data.plot(kind="bar")

    plt.title("Support Calls vs Churn")
    plt.xlabel("Support Calls")
    plt.ylabel("Number of Churned Customers")

    plt.tight_layout()

    plt.savefig("charts/churn_by_support_calls.png")

    plt.close()

    print("✓ Support Calls chart saved.")