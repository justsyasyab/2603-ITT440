import time
from threading import Thread
from multiprocessing import Pool
from fridge_engine import generate_data, analyze_chunk, merge_results

NUM_ITEMS = 100000
NUM_THREADS = 4
NUM_PROCESSES = 2


# -------------------------------
# DISPLAY (FRIDGE STYLE)
# -------------------------------
def display(title, result, duration):
    freezer, fridge = result

    print("\n" + "="*40)
    print(f"🧊 {title}")
    print("="*40)

    print("\n      ❄️ FREEZER (TOP)")
    print("      ----------------")
    print(f"      Items: {freezer['count']}")
    print(f"      Expired: {freezer['expired']}")

    print("\n      🥦 FRIDGE (BOTTOM)")
    print("      ------------------")
    print(f"      Items: {fridge['count']}")
    print(f"      Expired: {fridge['expired']}")

    print(f"\n⏱ Time: {duration:.2f} seconds")
    print("="*40)


# -------------------------------
# SEQUENTIAL
# -------------------------------
def run_sequential(data):
    start = time.time()
    result = analyze_chunk(data)
    return result, time.time() - start


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

    return merge_results(results), time.time() - start


# -------------------------------
# MULTIPROCESSING
# -------------------------------
def run_multiprocessing(data):
    start = time.time()

    chunk_size = len(data) // NUM_PROCESSES
    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(NUM_PROCESSES)]

    with Pool(processes=NUM_PROCESSES) as pool:
        results = pool.map(analyze_chunk, chunks)

    return merge_results(results), time.time() - start


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    print("Generating Smart Fridge Data...\n")
    data = generate_data(NUM_ITEMS)

    seq, t1 = run_sequential(data)
    display("SEQUENTIAL", seq, t1)

    thr, t2 = run_threading(data)
    display("THREADING", thr, t2)

    mp, t3 = run_multiprocessing(data)
    display("MULTIPROCESSING", mp, t3)
