import json
import pandas as pd
from datetime import datetime, timedelta
import os

# Today = T
T = datetime.today().date()

# Start = T - 30 days
START = T - timedelta(days=30)

if not os.path.exists("data/topic_reviews.json"):
    print("❌ topic_reviews.json not found. Run extract_topics.py first.")
    exit()

with open("data/topic_reviews.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert string date → date object
df["date"] = pd.to_datetime(df["date"]).dt.date

# Filter only last 30 days
df = df[(df["date"] >= START) & (df["date"] <= T)]

# Pivot table (Topic x Date)
pivot = pd.pivot_table(
    df,
    values="topic",
    index="topic",
    columns="date",
    aggfunc="count",
    fill_value=0
)

os.makedirs("output", exist_ok=True)

# Save CSV
pivot.to_csv("output/trend_report.csv")

print("✅ CSV generated successfully → output/trend_report.csv")
