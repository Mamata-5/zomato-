from google_play_scraper import reviews, Sort
from datetime import datetime
import json, os

APP_ID = "com.application.zomato"

def fetch_reviews():
    result, _ = reviews(
        APP_ID,
        lang="en",
        country="in",
        sort=Sort.NEWEST,
        count=1000
    )

    data = []
    for r in result:
        data.append({
            "date": str(r["at"].date()),
            "content": r["content"]
        })

    os.makedirs("data", exist_ok=True)
    with open("data/raw_reviews.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(data)} reviews")

if __name__ == "__main__":
    fetch_reviews()
