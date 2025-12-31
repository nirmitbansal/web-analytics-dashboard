import pandas as pd
import os

# Load data
file_path = os.path.join("data", "raw", "Web Analytic_Dataset.csv")
df = pd.read_csv(file_path)

# BEFORE cleaning
print("BEFORE CLEANING:")
print(df["Quantity Sold"].head())
print("Data type:", df["Quantity Sold"].dtype)

# Remove commas and convert to integer
df["Quantity Sold"] = df["Quantity Sold"].str.replace(",", "")
df["Quantity Sold"] = df["Quantity Sold"].astype(int)

# AFTER cleaning
print("\nAFTER CLEANING:")
print(df["Quantity Sold"].head())
print("Data type:", df["Quantity Sold"].dtype)
