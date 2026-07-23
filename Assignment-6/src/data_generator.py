import pandas as pd
import numpy as np
import random


def generate_customer_data(num_customers=1000):
    """Generate the initial customer churn dataset."""

    random.seed(42)
    np.random.seed(42)

    regions = ["North", "South", "East", "West"]
    contract_types = ["Monthly", "Annual", "Two-Year"]
    payment_methods = ["Credit Card", "Bank Transfer", "PayPal"]

    data = []

    for i in range(1, num_customers + 1):

        customer_id = f"CUST{i:04d}"

        age = random.randint(18, 70)

        gender = random.choice(["Male", "Female"])

        region = random.choice(regions)

        tenure = random.randint(1, 72)

        contract = random.choices(
            contract_types,
            weights=[50, 30, 20]
        )[0]

        monthly_charge = round(random.uniform(20, 150), 2)

        total_charge = round(monthly_charge * tenure, 2)

        support_calls = random.randint(0, 8)

        payment_method = random.choice(payment_methods)

        has_internet = random.choice(["Yes", "No"])

        has_premium = random.choice(["Yes", "No"])

                # Business logic for churn probability
        churn_probability = 0.10

        if contract == "Monthly":
            churn_probability += 0.30

        if tenure < 12:
            churn_probability += 0.25

        if monthly_charge > 100:
            churn_probability += 0.20

        if support_calls >= 5:
            churn_probability += 0.25

        if contract == "Two-Year":
            churn_probability -= 0.15

        if tenure > 36:
            churn_probability -= 0.10

        churn_probability = max(0.05, min(churn_probability, 0.95))

        churn = np.random.choice(
            ["Yes", "No"],
            p=[churn_probability, 1 - churn_probability]
        )

        data.append([          
            customer_id,
            age,
            gender,
            region,
            tenure,
            contract,
            monthly_charge,
            total_charge,
            support_calls,
            payment_method,
            has_internet,
            has_premium,
            churn
        ]) 
        
        

    columns = [
        "Customer_ID",
        "Age",
        "Gender",
        "Region",
        "Tenure_Months",
        "Contract_Type",
        "Monthly_Charges",
        "Total_Charges",
        "Support_Calls",
        "Payment_Method",
        "Has_Internet",
        "Has_Premium",
        "Churn"
    ]

    df = pd.DataFrame(data, columns=columns)
        # -----------------------------
    # Introduce Missing Values (~5%)
    # -----------------------------
    missing_columns = [
        "Monthly_Charges",
        "Total_Charges",
        "Payment_Method",
        "Support_Calls"
    ]

    for column in missing_columns:
        missing_indices = df.sample(frac=0.05, random_state=42).index
        df.loc[missing_indices, column] = np.nan
        # -----------------------------
    # Add Duplicate Records (20 rows)
    # -----------------------------
    duplicates = df.sample(n=20, random_state=42)
    df = pd.concat([df, duplicates], ignore_index=True)
        # -----------------------------
    # Add Outliers
    # -----------------------------
    outlier_indices = df.sample(10, random_state=10).index

    df.loc[outlier_indices[:3], "Monthly_Charges"] = [350, 450, 550]

    df.loc[outlier_indices[3:6], "Support_Calls"] = [18, 22, 30]

    df.loc[outlier_indices[6:], "Tenure_Months"] = [120, 140, 180, 200]
    df.to_csv("data/customer_churn.csv", index=False)

    print("Customer churn dataset generated successfully!")

    return df