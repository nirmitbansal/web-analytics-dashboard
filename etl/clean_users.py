import pandas as pd
import os

# Load data
file_path = os.path.join("data", "raw", "Web Analytic_Dataset.csv")
df = pd.read_csv(file_path)

# BEFORE cleaning
print("BEFORE CLEANING:")
print(df["Users"].head())
print("Data type:", df["Users"].dtype)

# Remove commas and convert to integer
df["Users"] = df["Users"].str.replace(",", "")
df["Users"] = df["Users"].astype(int)

# AFTER cleaning
print("\nAFTER CLEANING:")
print(df["Users"].head())
print("Data type:", df["Users"].dtype)
