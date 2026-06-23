import pandas as pd

data = {
    "Order_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "Salesperson": ["John","Sarah","John","Emma","Sarah","Michael","Emma","Michael","John","Sarah"],
    "Region": ["North","South","North","West","South","East","West","East","North","South"],
    "Amount": [1200,850,650,1700,950,1300,400,900,1500,1100]
}

df = pd.DataFrame(data)

df.to_csv("sales_data.csv", index=False)

print("sales_data.csv created successfully")