import pandas as pd


def load_data(file_path):
    """Load the customer churn dataset."""
    return pd.read_csv(file_path)


def explore_data(df):
    """Display basic dataset information."""
    print("\nDataset Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nStatistical Summary:")
    print(df.describe(include="all"))
def remove_duplicates(df):
    """Remove duplicate records."""
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate records found: {duplicates}")

    df = df.drop_duplicates()

    print(f"Dataset shape after removing duplicates: {df.shape}")

    return df
  
def handle_missing_values(df):
    """Fill missing values."""

    # Numeric columns
    numeric_columns = [
        "Monthly_Charges",
        "Total_Charges",
        "Support_Calls"
    ]

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    # Categorical column
    df["Payment_Method"] = df["Payment_Method"].fillna(
        df["Payment_Method"].mode()[0]
    )

    return df
    
def validate_data(df):
    """Validate cleaned dataset."""

    print("\nRemaining Missing Values:")
    print(df.isnull().sum())

    print("\nRemaining Duplicate Records:")
    print(df.duplicated().sum())

    print("\nData Validation:")

    print(f"Age >= 0: {(df['Age'] >= 0).all()}")

    print(f"Tenure >= 0: {(df['Tenure_Months'] >= 0).all()}")

    print(f"Monthly Charges > 0: {(df['Monthly_Charges'] > 0).all()}")

    print(f"Support Calls >= 0: {(df['Support_Calls'] >= 0).all()}")

    print(
        f"Valid Churn Values: "
        f"{df['Churn'].isin(['Yes', 'No']).all()}"
    )

def save_cleaned_data(df):
    """Save cleaned dataset."""
    df.to_csv("data/customer_churn_cleaned.csv", index=False)
    print("\nCleaned dataset saved successfully!")