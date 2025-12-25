import json
import os

KEYWORD_TOPICS = {
    # Delivery related
    "delivery": "delivery issue",
    "late": "delivery delay",
    "delay": "delivery delay",
    "rider": "delivery partner issue",
    "boy": "delivery partner issue",
    "rude": "delivery partner rude",
    "impolite": "delivery partner rude",

    # Food related
    "cold": "food quality issue",
    "stale": "food quality issue",
    "bad taste": "food quality issue",
    "spoiled": "food quality issue",
    "raw": "food quality issue",

    # Order issues
    "missing": "items missing",
    "wrong": "wrong order delivered",
    "cancel": "order cancellation issue",

    # App / technical
    "app": "app performance issue",
    "crash": "app crash issue",
    "login": "login issue",
    "map": "maps not working",

    # Pricing & payment
    "price": "pricing issue",
    "expensive": "pricing issue",
    "refund": "refund issue",
    "payment": "payment issue",

    # Support
    "support": "customer support issue",
    "help": "customer support issue"
}



def extract_topic(text):
    text = text.lower()
    for key, topic in KEYWORD_TOPICS.items():
        if key in text:
            return topic
    return None

if __name__ == "__main__":
    if not os.path.exists("data/raw_reviews.json"):
        print("❌ raw_reviews.json not found. Run fetch_reviews.py first.")
        exit()

    with open("data/raw_reviews.json", "r", encoding="utf-8") as f:
        reviews = json.load(f)

    topic_data = []

    for r in reviews:
        topic = extract_topic(r["content"])
        if topic:
            topic_data.append({
                "date": r["date"],
                "topic": topic
            })

    with open("data/topic_reviews.json", "w", encoding="utf-8") as f:
        json.dump(topic_data, f, indent=2)

    print(f"Extracted topics from {len(topic_data)} reviews")
