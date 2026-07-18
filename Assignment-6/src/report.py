import pandas as pd


def generate_summary_report(df):
    """Generate churn summary report."""

    summary = []

    for contract in df["Contract_Type"].unique():

        segment_data = df[df["Contract_Type"] == contract]

        total_customers = len(segment_data)
        churned_customers = len(segment_data[segment_data["Churn"] == "Yes"])
        churn_rate = round((churned_customers / total_customers) * 100, 2)

        summary.append({
            "Segment": contract,
            "Total Customers": total_customers,
            "Churned Customers": churned_customers,
            "Churn Rate": churn_rate
        })

    summary_df = pd.DataFrame(summary)

    summary_df.to_csv(
        "data/churn_summary.csv",
        index=False
    )

    print("✓ Churn summary saved.")