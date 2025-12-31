import pandas as pd
import os

# Load data
file_path = os.path.join("data", "raw", "Web Analytic_Dataset.csv")
df = pd.read_csv(file_path)

# BEFORE cleaning
print("BEFORE CLEANING:")
print(df["Transactions"].head())
print("Data type:", df["Transactions"].dtype)

# Remove commas and convert to integer
df["Transactions"] = df["Transactions"].str.replace(",", "")
df["Transactions"] = df["Transactions"].astype(int)

# AFTER cleaning
print("\nAFTER CLEANING:")
print(df["Transactions"].head())
print("Data type:", df["Transactions"].dtype)
