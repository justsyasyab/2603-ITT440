import random
import time
from datetime import datetime, timedelta

# ANSI Colors for terminal flair
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def generate_data(n):
    """Generates bulk inventory with varied complexity levels."""
    data = []
    today = datetime.now()
    # Categories and their distribution
    categories = [("Dairy", 0.9), ("Meat", 0.08), ("Frozen", 0.02)] 
    cat_names = [c[0] for c in categories]
    cat_weights = [c[1] for c in categories]
    
    for _ in range(n):
        # Select category based on weight
        cat = random.choices(cat_names, weights=cat_weights)[0]
        section = "FREEZER" if cat == "Frozen" else "FRIDGE"
        expiry = today + timedelta(days=random.randint(-5, 10))
        data.append({"section": section, "cat": cat, "expiry": expiry})
    return data

def analyze_chunk(chunk):
    """Analyzes a chunk of items for expiration status."""
    today = datetime.now()
    freezer = {"count": 0, "expired": 0}
    fridge = {"count": 0, "expired": 0}

    for item in chunk:
        # Simulate sensor latency for complex items to ensure Multiprocessing speedup
        if item["cat"] in ["Meat", "Frozen"]:
            time.sleep(0.0001) 

        if item["section"] == "FREEZER":
            freezer["count"] += 1
            if item["expiry"] < today: 
                freezer["expired"] += 1
        else:
            fridge["count"] += 1
            if item["expiry"] < today: 
                fridge["expired"] += 1

    return freezer, fridge

def merge_results(results):
    """Merges dictionary results from multiple threads/processes."""
    f_freezer = {"count": 0, "expired": 0}
    f_fridge = {"count": 0, "expired": 0}
    for fz, fr in results:
        f_freezer["count"] += fz["count"]
        f_freezer["expired"] += fz["expired"]
        f_fridge["count"] += fr["count"]
        f_fridge["expired"] += fr["expired"]
    return f_freezer, f_fridge