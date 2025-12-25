import json
import os

# Semantic fallback taxonomy (acts as LLM surrogate)
KEYWORD_TOPICS = {
    # Delivery
    "delivery": "delivery issue",
    "late": "delivery delay",
    "delay": "delivery delay",
    "rude": "delivery partner rude",
    "impolite": "delivery partner rude",
    "unprofessional": "delivery partner rude",

    # Food
    "cold": "food quality issue",
    "stale": "food quality issue",
    "spoiled": "food quality issue",
    "raw": "food quality issue",

    # Order
    "missing": "items missing",
    "wrong": "wrong order delivered",
    "cancel": "order cancellation issue",

    # App / Tech
    "crash": "app crash issue",
    "login": "login issue",
    "map": "maps not working",

    # Payment / Pricing
    "refund": "refund issue",
    "payment": "payment issue",
    "price": "pricing issue",
    "expensive": "pricing issue",

    # Support
    "support": "customer support issue",
    "help": "customer support issue"
}

def extract_topics(review_text: str):
    """
    Hybrid topic extraction.
    Designed to support LLM-based extraction,
    with guaranteed fallback for robustness.
    """
    text = review_text.lower()
    topics = set()

    for key, topic in KEYWORD_TOPICS.items():
        if key in text:
            topics.add(topic)

    return list(topics)

if __name__ == "__main__":
    if not os.path.exists("data/raw_reviews.json"):
        print("❌ raw_reviews.json not found. Run fetch_reviews.py first.")
        exit()

    with open("data/raw_reviews.json", "r", encoding="utf-8") as f:
        reviews = json.load(f)

    output = []

    for r in reviews:
        topics = extract_topics(r["content"])
        for t in topics:
            output.append({
                "date": r["date"],
                "topic": t,
                "confidence": 1.0
            })

    with open("data/topic_reviews.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"✅ Extracted {len(output)} topic instances")
