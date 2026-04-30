import random
import time
from datetime import datetime, timedelta
from threading import Thread
from multiprocessing import Pool

# -------------------------------
# CONFIGURATION
# -------------------------------
NUM_ITEMS = 100000  # Large dataset
NUM_THREADS = 4     # For threading
NUM_PROCESSES = 2   # You have 2 CPUs

CATEGORIES = ["Dairy", "Meat", "Drinks", "Vegetables"]

ITEM_NAMES = {
    "Dairy": ["Milk", "Cheese", "Yogurt"],
    "Meat": ["Chicken", "Beef", "Fish"],
    "Drinks": ["Juice", "Soda", "Water"],
    "Vegetables": ["Carrot", "Broccoli", "Spinach"]
}

# -------------------------------
# DATA GENERATION
# -------------------------------
def generate_data(n):
    data = []
    today = datetime.now()

    for _ in range(n):
        category = random.choice(CATEGORIES)
        item = random.choice(ITEM_NAMES[category])

        expiry = today + timedelta(days=random.randint(-5, 10))
        consumed = random.choice([True, False])

        data.append({
            "item": item,
            "category": category,
            "expiry": expiry,
            "consumed": consumed
        })

    return data

# -------------------------------
# ANALYSIS FUNCTION
# -------------------------------
def analyze_chunk(chunk):
    today = datetime.now()

    expired = 0
    consumed = 0
    wasted = 0
    category_count = {cat: 0 for cat in CATEGORIES}

    for item in chunk:
        category_count[item["category"]] += 1

        if item["expiry"] < today:
            expired += 1

        if item["consumed"]:
            consumed += 1
        else:
            wasted += 1

    return expired, consumed, wasted, category_count

# -------------------------------
# HELPER TO MERGE RESULTS
# -------------------------------
def merge_results(results):
    total_expired = total_consumed = total_wasted = 0
    final_category = {cat: 0 for cat in CATEGORIES}

    for expired, consumed, wasted, category in results:
        total_expired += expired
        total_consumed += consumed
        total_wasted += wasted

        for cat in CATEGORIES:
            final_category[cat] += category[cat]

    return total_expired, total_consumed, total_wasted, final_category

# -------------------------------
# SEQUENTIAL
# -------------------------------
def run_sequential(data):
    start = time.time()
    result = analyze_chunk(data)
    end = time.time()

    return result, end - start

# -------------------------------
# THREADING
# -------------------------------
def run_threading(data):
    start = time.time()

    chunk_size = len(data) // NUM_THREADS
    threads = []
    results = []

    def worker(chunk):
        results.append(analyze_chunk(chunk))

    for i in range(NUM_THREADS):
        chunk = data[i * chunk_size:(i + 1) * chunk_size]
        t = Thread(target=worker, args=(chunk,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    final_result = merge_results(results)
    end = time.time()

    return final_result, end - start

# -------------------------------
# MULTIPROCESSING
# -------------------------------
def run_multiprocessing(data):
    start = time.time()

    chunk_size = len(data) // NUM_PROCESSES
    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(NUM_PROCESSES)]

    with Pool(processes=NUM_PROCESSES) as pool:
        results = pool.map(analyze_chunk, chunks)

    final_result = merge_results(results)
    end = time.time()

    return final_result, end - start

# -------------------------------
# DISPLAY RESULTS
# -------------------------------
def display(name, result, duration):
    expired, consumed, wasted, category = result

    print(f"\n{name} RESULTS")
    print("-" * 30)
    print(f"Expired Items: {expired}")
    print(f"Consumed Items: {consumed}")
    print(f"Wasted Items: {wasted}")

    print("\nCategory Count:")
    for cat, count in category.items():
        print(f"{cat}: {count}")

    print(f"\nTime Taken: {duration:.2f} seconds")

# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    print("Generating data...")
    data = generate_data(NUM_ITEMS)

    # Sequential
    seq_result, seq_time = run_sequential(data)
    display("SEQUENTIAL", seq_result, seq_time)

    # Threading
    thread_result, thread_time = run_threading(data)
    display("THREADING", thread_result, thread_time)

    # Multiprocessing
    mp_result, mp_time = run_multiprocessing(data)
    display("MULTIPROCESSING", mp_result, mp_time)
