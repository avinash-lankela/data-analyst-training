#!/usr/bin/env python
# coding: utf-8

# In[5]:


sales = [
    {'order_id': 1001, 'salesperson': 'John', 'amount': 1200},
    {'order_id': 1002, 'salesperson': 'Sarah', 'amount': 850},
    {'order_id': 1003, 'salesperson': 'John', 'amount': 650},
    {'order_id': 1004, 'salesperson': 'Emma', 'amount': 1700},
    {'order_id': 1005, 'salesperson': 'Sarah', 'amount': 950}
]
print("=" * 50)
print("SALES REPORT ANALYZER")
print("=" * 50)
# 1. Calculate Total Company Sales
total_sales = sum(sale['amount'] for sale in sales)
print(f"\n1. Total Company Sales: ${total_sales}")
# 2. Calculate Average Order Value
average_order_value = round(total_sales / len(sales), 2)

print(f"2. Average Order Value: ${average_order_value}")
# 3. Find Highest-Value Transaction
highest_transaction = max(sales, key=lambda sale: sale['amount'])

print("\n3. Highest-Value Transaction:")
print(f"   Order ID: {highest_transaction['order_id']}")
print(f"   Salesperson: {highest_transaction['salesperson']}")
print(f"   Amount: ${highest_transaction['amount']}")
# 4. Generate Sales Summary by Employee
sales_summary = {}

for sale in sales:
    salesperson = sale['salesperson']
    amount = sale['amount']

    if salesperson not in sales_summary:
        sales_summary[salesperson] = 0

    sales_summary[salesperson] += amount

print("\n4. Sales Summary by Employee:")
for employee, total in sales_summary.items():
     print(f"   {employee}: ${total}")
# 5. Identify Top Performer
top_performer = max(sales_summary, key=sales_summary.get)

print(f"\n5. Top Performer: {top_performer} (${sales_summary[top_performer]})")

# 6. Display Transactions Above $1000
print("\n6. Transactions Above $1000:")

count_above_1000 = 0

for sale in sales:
    if sale['amount'] > 1000:
        print(
            f"   Order ID: {sale['order_id']} | "
            f"Salesperson: {sale['salesperson']} | "
            f"Amount: ${sale['amount']}"
        )
        count_above_1000 += 1

# Stretch Goal 1
highest_salesperson = max(sales_summary, key=sales_summary.get)

print("\nSTRETCH GOALS")
print(f"1. Salesperson with Highest Total Sales: {highest_salesperson}")

# Stretch Goal 2
john_sales = sales_summary.get('John', 0)
john_percentage = round((john_sales / total_sales) * 100, 2)

print(f"2. Percentage of Total Sales from John: {john_percentage}%")

# Stretch Goal 3
print(f"3. Number of Transactions Above $1000: {count_above_1000}")

# Stretch Goal 4
company_target = 6000
additional_revenue_needed = max(0, company_target - total_sales)

print(f"4. Additional Revenue Needed to Reach $6000 Target: ${additional_revenue_needed}")

print("\n" + "=" * 50)
print("REPORT GENERATED SUCCESSFULLY")
print("=" * 50)




# In[ ]:




