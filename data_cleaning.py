import pandas as pd

# Load dataset
df = pd.read_csv("messy_sales_data.csv")

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize city names
df["City"] = df["City"].str.title()

# Fill missing values
df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Convert data types
df["Quantity"] = df["Quantity"].astype(int)
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nTotal Revenue:", df["Revenue"].sum())
print("Revenue by City:")
print(df.groupby("City")["Revenue"].sum())
