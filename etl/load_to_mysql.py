import pandas as pd
import mysql.connector
import os

# -----------------------
# DB CONNECTION
# -----------------------
conn = mysql.connector.connect(
    host="localhost",
    user="nirmitbansal",
    password="nirmit2708",
    database="web_analytics_dw"
)

cursor = conn.cursor()

# -----------------------
# LOAD CLEANED DATA
# -----------------------
file_path = os.path.join("data", "processed", "web_analytics_cleaned.csv")
df = pd.read_csv(file_path)

# -----------------------
# INSERT INTO dim_source
# -----------------------
sources = df["Source / Medium"].unique()

source_id_map = {}

for source in sources:
    cursor.execute(
        "INSERT IGNORE INTO dim_source (source_medium) VALUES (%s)",
        (source,)
    )
    conn.commit()

cursor.execute("SELECT source_id, source_medium FROM dim_source")
for row in cursor.fetchall():
    source_id_map[row[1]] = row[0]

# -----------------------
# INSERT INTO dim_date
# -----------------------
dates = df[["Year", "Month of the year"]].drop_duplicates()

date_id_map = {}

for _, row in dates.iterrows():
    cursor.execute(
        "INSERT INTO dim_date (year, month) VALUES (%s, %s)",
        (int(row["Year"]), int(row["Month of the year"]))
    )
    conn.commit()

cursor.execute("SELECT date_id, year, month FROM dim_date")
for row in cursor.fetchall():
    date_id_map[(row[1], row[2])] = row[0]

# -----------------------
# INSERT INTO FACT TABLE
# -----------------------
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO fact_web_analytics (
            source_id, date_id, users, new_users, sessions,
            pageviews, transactions, revenue, quantity_sold,
            conversion_rate, avg_session_duration_seconds, bounce_rate
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        source_id_map[row["Source / Medium"]],
        date_id_map[(row["Year"], row["Month of the year"])],
        row["Users"],
        row["New Users"],
        row["Sessions"],
        row["Pageviews"],
        row["Transactions"],
        row["Revenue"],
        row["Quantity Sold"],
        row["Conversion Rate (%)"],
        row["Avg. Session Duration (Seconds)"],
        row["Bounce Rate"]
    ))

conn.commit()

print("✅ Data loaded successfully into MySQL")

cursor.close()
conn.close()
