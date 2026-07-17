import pandas as pd
import random
from datetime import datetime, timedelta
customers = [
    "John","Alice","David","Sophia","Emma",
    "James","Michael","Olivia","Daniel","Liam",
    "Noah","Mia","Charlotte","Ava","William"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

categories = {
    "Electronics":["Laptop","Mobile","Headphones","Monitor","Keyboard"],
    "Furniture":["Chair","Table","Sofa","Cupboard","Desk"],
    "Clothing":["T-Shirt","Jeans","Jacket","Shoes","Cap"],
    "Groceries":["Rice","Milk","Bread","Eggs","Oil"]
}

salespersons = [
    "Rahul",
    "Priya",
    "Amit",
    "Sneha",
    "Kiran",
    "Ravi",
    "Pooja"
]

# -----------------------------
# Generate Records
# -----------------------------

records = []

start_date = datetime(2025,1,1)

for i in range(500):

    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])

    quantity = random.randint(1,10)

    if category=="Electronics":
        price = random.randint(5000,50000)

    elif category=="Furniture":
        price = random.randint(2000,20000)

    elif category=="Clothing":
        price = random.randint(300,5000)

    else:
        price = random.randint(50,1000)

    order_date = start_date + timedelta(days=random.randint(0,364))

    records.append([
        i+1,
        order_date.strftime("%Y-%m-%d"),
        random.choice(customers),
        random.choice(regions),
        category,
        product,
        quantity,
        price,
        random.choice(salespersons)
    ])

columns = [
    "Order_ID",
    "Order_Date",
    "Customer",
    "Region",
    "Category",
    "Product",
    "Quantity",
    "Unit_Price",
    "Salesperson"
]

df = pd.DataFrame(records,columns=columns)
# -----------------------------
# Add Missing Values (5%)
# -----------------------------

for col in df.columns:
    if col != "Order_ID":
        missing_rows = df.sample(frac=0.05).index
        df.loc[missing_rows, col] = None
    # -----------------------------
# Add Duplicate Records
# -----------------------------

duplicates = df.sample(10)

df = pd.concat([df,duplicates],ignore_index=True)
# -----------------------------
# Add Outliers
# -----------------------------

outlier_rows = df.sample(5).index

df.loc[outlier_rows,"Unit_Price"] = [
    200000,
    300000,
    250000,
    500000,
    750000
]
# -----------------------------
# Save Dataset
# -----------------------------

df.to_csv("retail_sales.csv",index=False)

