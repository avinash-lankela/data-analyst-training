import pandas as pd


def calculate_kpis(df):
    """Calculate and display customer churn KPIs."""

    total_customers = len(df)

    churned_customers = len(df[df["Churn"] == "Yes"])

    churn_rate = (churned_customers / total_customers) * 100

    retention_rate = 100 - churn_rate

    print("\n" + "=" * 50)
    print("           CUSTOMER CHURN KPIs")
    print("=" * 50)

    print(f"Total Customers      : {total_customers}")
    print(f"Churned Customers    : {churned_customers}")
    print(f"Retention Customers  : {total_customers - churned_customers}")
    print(f"Churn Rate           : {churn_rate:.2f}%")
    print(f"Retention Rate       : {retention_rate:.2f}%")

    print("=" * 50)


def churn_by_contract(df):
    """Analyze churn by contract type."""

    print("\n" + "=" * 50)
    print("CHURN BY CONTRACT TYPE")
    print("=" * 50)

    result = (
        df.groupby("Contract_Type")["Churn"]
        .value_counts(normalize=True)
        .mul(100)
        .rename("Churn Rate")
        .reset_index()
    )

    result = result[result["Churn"] == "Yes"]

    print(result)


def churn_by_region(df):
    """Analyze churn by region."""

    print("\n" + "=" * 50)
    print("CHURN BY REGION")
    print("=" * 50)

    result = (
        df.groupby("Region")["Churn"]
        .value_counts(normalize=True)
        .mul(100)
        .rename("Churn Rate")
        .reset_index()
    )

    result = result[result["Churn"] == "Yes"]

    print(result)


def churn_by_gender(df):
    """Analyze churn by gender."""

    print("\n" + "=" * 50)
    print("CHURN BY GENDER")
    print("=" * 50)

    result = (
        df.groupby("Gender")["Churn"]
        .value_counts(normalize=True)
        .mul(100)
        .rename("Churn Rate")
        .reset_index()
    )

    result = result[result["Churn"] == "Yes"]

def churn_by_tenure(df):
    """Analyze churn by tenure group."""

    print("\n" + "=" * 50)
    print("CHURN BY TENURE")
    print("=" * 50)

    df["Tenure_Group"] = pd.cut(
        df["Tenure_Months"],
        bins=[0, 12, 24, 36, 60, 200],
        labels=["0-12", "13-24", "25-36", "37-60", "60+"]
    )

    result = (
        df.groupby("Tenure_Group")["Churn"]
        .value_counts(normalize=True)
        .mul(100)
        .rename("Churn Rate")
        .reset_index()
    )

    print(result[result["Churn"] == "Yes"])

def churn_by_monthly_charges(df):
    """Analyze churn by monthly charge groups."""

    print("\n" + "=" * 50)
    print("CHURN BY MONTHLY CHARGES")
    print("=" * 50)

    df["Charge_Group"] = pd.cut(
        df["Monthly_Charges"],
        bins=[0, 50, 80, 110, 600],
        labels=["Low", "Medium", "High", "Very High"]
    )

    result = (
        df.groupby("Charge_Group")["Churn"]
        .value_counts(normalize=True)
        .mul(100)
        .rename("Churn Rate")
        .reset_index()
    )

    print(result[result["Churn"] == "Yes"])

def churn_by_support_calls(df):
    """Analyze churn by support calls."""

    print("\n" + "=" * 50)
    print("CHURN BY SUPPORT CALLS")
    print("=" * 50)

    result = (
        df.groupby("Support_Calls")["Churn"]
        .value_counts(normalize=True)
        .mul(100)
        .rename("Churn Rate")
        .reset_index()
    )

    print(result[result["Churn"] == "Yes"])

def churn_by_premium(df):
    """Analyze churn by premium subscription."""

    print("\n" + "=" * 50)
    print("CHURN BY PREMIUM SUBSCRIPTION")
    print("=" * 50)

    result = (
        df.groupby("Has_Premium")["Churn"]
        .value_counts(normalize=True)
        .mul(100)
        .rename("Churn Rate")
        .reset_index()
    )

    print(result[result["Churn"] == "Yes"])

def customer_risk_segmentation(df):

    print("\n" + "=" * 50)
    print("CUSTOMER RISK SEGMENTATION")
    print("=" * 50)

    def classify(row):

        if (
            row["Tenure_Months"] < 12
            and row["Support_Calls"] >= 5
            and row["Monthly_Charges"] > 100
        ):
            return "High"

        elif (
            row["Tenure_Months"] < 24
            or row["Support_Calls"] >= 3
        ):
            return "Medium"

        else:
            return "Low"

    df["Risk_Level"] = df.apply(classify, axis=1)

    print(df["Risk_Level"].value_counts())

    return df