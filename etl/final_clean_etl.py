import pandas as pd
import os

# Load raw data
file_path = os.path.join("data", "raw", "Web Analytic_Dataset.csv")
df = pd.read_csv(file_path)

# -------------------------------
# CLEAN NUMERIC COLUMNS
# -------------------------------
numeric_columns = [
    "Users", "New Users", "Sessions", "Pageviews",
    "Transactions", "Revenue", "Quantity Sold"
]

for col in numeric_columns:
    df[col] = df[col].str.replace(",", "").astype(int)

# -------------------------------
# CLEAN PERCENTAGE COLUMNS
# -------------------------------
# Fix special values like '<0.01'
df["Conversion Rate (%)"] = (
    df["Conversion Rate (%)"]
    .str.replace("%", "", regex=False)
    .str.replace("<0.01", "0.01", regex=False)
    .astype(float)
)
df["Bounce Rate"] = df["Bounce Rate"].str.replace("%", "").astype(float)

# -------------------------------
# CLEAN TIME COLUMN
# -------------------------------
df["Avg. Session Duration"] = pd.to_timedelta(df["Avg. Session Duration"])
df["Avg. Session Duration (Seconds)"] = df["Avg. Session Duration"].dt.total_seconds()

# Drop original time column
df.drop(columns=["Avg. Session Duration"], inplace=True)

# -------------------------------
# SAVE CLEANED DATA
# -------------------------------
output_path = os.path.join("data", "processed", "web_analytics_cleaned.csv")
df.to_csv(output_path, index=False)

print("✅ Cleaned dataset saved successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
