import pandas as pd
import os

# Correct file path (based on verified filename)
file_path = os.path.join("data", "raw", "Web Analytic_Dataset.csv")

# Read CSV
df = pd.read_csv(file_path)

print("FIRST 5 ROWS:")
print(df.head())

print("\nDATA INFO:")
print(df.info())

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nTOTAL ROWS:")
print(len(df))
