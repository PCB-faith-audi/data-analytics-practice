import pandas as pd

data = {
    "order_id": [101, 102, 103, 104, 105, 106],
    "branch": ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Mombasa", "Nairobi"],
    "product": ["Phone", "Laptop", "Headphones", "Phone", "Phone", "Laptop"],
    "quantity": [2, 1, 5, 1, 3, 2],
    "unit_price": [15000, 65000, 2500, 15000, 15000, 65000],

}

df = pd.DataFrame(data)

print(df.head())

print(df.shape)