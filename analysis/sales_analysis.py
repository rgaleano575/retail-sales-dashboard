import pandas as pd

# Load the sales dataset
df = pd.read_csv("data/posadas_retail_sales.csv")

# Basic overview
print("Total revenue:", round(df["Revenue"].sum(), 2))
print("Total units sold:", df["Units_Sold"].sum())
print("Total gross profit:", round(df["Gross_Profit"].sum(), 2))
print("Average gross margin:", df["Gross_Margin"].mean())

# Revenue by category
category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by category:")
print(category_revenue)

# Revenue by sales channel
channel_revenue = (
    df.groupby("Sales_Channel")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by sales channel:")
print(channel_revenue)

# Best-selling products by units
product_units = (
    df.groupby("Product")["Units_Sold"]
    .sum()
    .sort_values(ascending=False)
)

print("\nUnits sold by product:")
print(product_units)

# Products with low inventory
low_inventory = df[df["Inventory_Level"] <= 5][
    ["Product", "Inventory_Level"]
].drop_duplicates()

print("\nProducts requiring inventory attention:")
print(low_inventory)
