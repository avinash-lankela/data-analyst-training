from src.report import generate_summary_report
from src.visualization import (
    plot_contract_type,
    plot_region,
    plot_churn_distribution,
    plot_tenure,
    plot_support_calls,
)

from src.data_generator import generate_customer_data
from src.data_cleaning import (
    load_data,
    explore_data,
    remove_duplicates,
    handle_missing_values,
    validate_data,
    save_cleaned_data,
)
from src.analysis import (
    calculate_kpis,
    churn_by_contract,
    churn_by_region,
    churn_by_gender,
    churn_by_tenure,
    churn_by_monthly_charges,
    churn_by_support_calls,
    churn_by_premium,
    customer_risk_segmentation,
)

# Generate dataset
generate_customer_data()

# Load dataset
df = load_data("data/customer_churn.csv")

# Explore dataset
explore_data(df)

# Clean dataset
df = remove_duplicates(df)
df = handle_missing_values(df)

# Validate cleaned dataset
validate_data(df)

# Save cleaned dataset
save_cleaned_data(df)

# KPI & Business Analysis
calculate_kpis(df)
churn_by_contract(df)
churn_by_region(df)
churn_by_gender(df)
churn_by_tenure(df)
churn_by_monthly_charges(df)
churn_by_support_calls(df)
churn_by_premium(df)

# Risk Segmentation
df = customer_risk_segmentation(df)

# Visualizations
plot_contract_type(df)
plot_region(df)
plot_churn_distribution(df)
plot_tenure(df)
plot_support_calls(df)

generate_summary_report(df)