import random
from datetime import datetime, timedelta

CATEGORIES = ["Dairy", "Meat", "Drinks", "Vegetables"]

FREEZER_ITEMS = ["Ice Cream", "Frozen Meat", "Frozen Pizza"]
FRIDGE_ITEMS = ["Milk", "Juice", "Vegetables", "Eggs"]

def generate_data(n):
    data = []
    today = datetime.now()

    for _ in range(n):
        section = random.choice(["FREEZER", "FRIDGE"])

        if section == "FREEZER":
            item = random.choice(FREEZER_ITEMS)
        else:
            item = random.choice(FRIDGE_ITEMS)

        expiry = today + timedelta(days=random.randint(-5, 10))
        consumed = random.choice([True, False])

        data.append({
            "section": section,
            "item": item,
            "expiry": expiry,
            "consumed": consumed
        })

    return data


def analyze_chunk(chunk):
    today = datetime.now()

    freezer = {"count": 0, "expired": 0}
    fridge = {"count": 0, "expired": 0}

    for item in chunk:
        section = item["section"]

        if section == "FREEZER":
            freezer["count"] += 1
            if item["expiry"] < today:
                freezer["expired"] += 1

        else:
            fridge["count"] += 1
            if item["expiry"] < today:
                fridge["expired"] += 1

    return freezer, fridge


def merge_results(results):
    final_freezer = {"count": 0, "expired": 0}
    final_fridge = {"count": 0, "expired": 0}

    for freezer, fridge in results:
        final_freezer["count"] += freezer["count"]
        final_freezer["expired"] += freezer["expired"]

        final_fridge["count"] += fridge["count"]
        final_fridge["expired"] += fridge["expired"]

    return final_freezer, final_fridge
