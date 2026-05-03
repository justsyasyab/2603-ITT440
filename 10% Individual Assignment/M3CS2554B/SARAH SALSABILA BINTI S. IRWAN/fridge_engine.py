import random
import time
from datetime import datetime, timedelta

# ANSI Colors for a professional dashboard look
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

CATEGORIES = {
    "Dairy": ["Milk", "Cheese", "Yogurt"],
    "Meat": ["Chicken", "Beef", "Fish"],
    "Drink": ["Juice", "Soda", "Water"],
    "Veg": ["Carrot", "Spinach", "Broccoli"]
}

def generate_data(n):
    """Generates bulk inventory data with items, categories, and sections."""
    data = []
    today = datetime.now()
    cat_list = list(CATEGORIES.keys())
    for _ in range(n):
        cat = random.choice(cat_list)
        item_name = random.choice(CATEGORIES[cat])
        section = "TOP" if cat in ["Dairy", "Meat"] else "BOTTOM"
        expiry = today + timedelta(days=random.randint(-5, 10))
        consumed = random.choice(["Yes", "No"])
        data.append({
            "item": item_name, "category": cat, "section": section,
            "expiry": expiry, "consumed": consumed
        })
    return data

def analyze_chunk(chunk):
    """Core logic used for Sequence, Concurrent, and Parallel analysis."""
    today = datetime.now()
    results = {"TOP": {"total": 0, "expired": 0}, "BOTTOM": {"total": 0, "expired": 0}}
    for item in chunk:
        # Simulate sensor data processing time (0.0001s per item)
        # This makes the parallel speedup very visible.
        time.sleep(0.0001) 
        sec = item["section"]
        results[sec]["total"] += 1
        if item["expiry"] < today and item["consumed"] == "No":
            results[sec]["expired"] += 1
    return results

def merge_results(results_list):
    """Combines partial results from multiple processes/threads."""
    final = {"TOP": {"total": 0, "expired": 0}, "BOTTOM": {"total": 0, "expired": 0}}
    for res in results_list:
        for sec in final:
            final[sec]["total"] += res[sec]["total"]
            final[sec]["expired"] += res[sec]["expired"]
    return final

def draw_graph(times):
    """Renders a text-based bar graph to visualize speed differences."""
    labels = ["Sequential", "Threading ", "Parallel  "]
    max_t = max(times)
    print(f"\n{YELLOW}📊 PERFORMANCE GRAPH{RESET}")
    for i in range(3):
        # Scale bar length to 30 characters maximum
        bar = "█" * int((times[i] / max_t) * 30)
        print(f"{labels[i]}: {bar} {times[i]:.4f}s")
