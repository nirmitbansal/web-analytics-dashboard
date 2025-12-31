import pandas as pd
import os

# Load data
file_path = os.path.join("data", "raw", "Web Analytic_Dataset.csv")
df = pd.read_csv(file_path)

# BEFORE cleaning
print("BEFORE CLEANING:")
print(df["Revenue"].head())
print("Data type:", df["Revenue"].dtype)

# Remove commas and convert to integer
df["Revenue"] = df["Revenue"].str.replace(",", "")
df["Revenue"] = df["Revenue"].astype(int)

# AFTER cleaning
print("\nAFTER CLEANING:")
print(df["Revenue"].head())
print("Data type:", df["Revenue"].dtype)
