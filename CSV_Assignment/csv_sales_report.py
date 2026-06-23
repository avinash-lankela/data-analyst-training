import csv

file_name = "sales_data_bad.csv"

total_revenue = 0
transaction_count = 0

sales_by_employee = {}
sales_by_region = {}

largest_transaction = 0
largest_transaction_record = None

high_value_transactions = []

with open(file_name, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            amount = float(row["Amount"])

        except (ValueError, TypeError, KeyError):
            print(
                f"Skipping Invalid Record: "
                f"Order ID {row['order_id']}"
            )
            continue

        total_revenue += amount
        transaction_count += 1

        employee = row["salesperson"]

        if employee in sales_by_employee:
            sales_by_employee[employee] += amount
        else:
            sales_by_employee[employee] = amount

        region = row["region"]

        if region in sales_by_region:
            sales_by_region[region] += amount
        else:
            sales_by_region[region] = amount

        if amount > largest_transaction:
            largest_transaction = amount
            largest_transaction_record = row

        if amount > 1000:
            high_value_transactions.append(row)

average_transaction = total_revenue / transaction_count

top_salesperson = max(
    sales_by_employee,
    key=sales_by_employee.get
)

highest_region = max(
    sales_by_region,
    key=sales_by_region.get
)

print("\n========== SALES REPORT ==========")

print(f"\nTotal Revenue: ${total_revenue:.2f}")

print(
    f"Average Transaction Amount: "
    f"${average_transaction:.2f}"
)

print("\nSales By Employee")

for employee, revenue in sales_by_employee.items():
    print(f"{employee}: ${revenue:.2f}")

print("\nSales By Region")

for region, revenue in sales_by_region.items():
    print(f"{region}: ${revenue:.2f}")

print(
    f"\nTop Salesperson: "
    f"{top_salesperson} "
    f"(${sales_by_employee[top_salesperson]:.2f})"
)

print(
    f"Highest Revenue Region: "
    f"{highest_region} "
    f"(${sales_by_region[highest_region]:.2f})"
)

print("\nLargest Transaction")

print(
    f"Order ID: {largest_transaction_record['order_id']}"
)

print(
    f"Salesperson: "
    f"{largest_transaction_record['salesperson']}"
)

print(
    f"Amount: ${largest_transaction:.2f}"
)

print("\nTransactions Above $1000")

for transaction in high_value_transactions:
    print(
        f"Order ID: {transaction['order_id']}, "
        f"Salesperson: {transaction['salesperson']}, "
        f"Amount: ${float(transaction['Amount']):.2f}"
    )

print("\nRevenue Contribution Percentage")

for employee, revenue in sales_by_employee.items():
    percentage = (revenue / total_revenue) * 100

    print(
        f"{employee}: "
        f"{percentage:.2f}%"
    )

print("\nEmployees Sorted By Revenue")

sorted_employees = sorted(
    sales_by_employee.items(),
    key=lambda item: item[1],
    reverse=True
)

for employee, revenue in sorted_employees:
    print(f"{employee}: ${revenue:.2f}")