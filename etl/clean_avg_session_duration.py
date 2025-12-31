import pandas as pd
import os

# Load data
file_path = os.path.join("data", "raw", "Web Analytic_Dataset.csv")
df = pd.read_csv(file_path)

# BEFORE cleaning
print("BEFORE CLEANING:")
print(df["Avg. Session Duration"].head())
print("Data type:", df["Avg. Session Duration"].dtype)

# Convert HH:MM:SS to total seconds
df["Avg. Session Duration"] = pd.to_timedelta(df["Avg. Session Duration"])
df["Avg. Session Duration (Seconds)"] = df["Avg. Session Duration"].dt.total_seconds()

# AFTER cleaning
print("\nAFTER CLEANING (SECONDS):")
print(df["Avg. Session Duration (Seconds)"].head())
print("Data type:", df["Avg. Session Duration (Seconds)"].dtype)
