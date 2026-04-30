import time
<<<<<<< HEAD
import multiprocessing
import threading
from fridge_engine import generate_data, analyze_chunk, merge_results, RED, GREEN, CYAN, RESET

NUM_ITEMS = 50000 # Enough to see a difference, not too long for a demo video
CORES = multiprocessing.cpu_count()

def print_header(title):
    print(f"\n{CYAN}╔" + "═"*48 + "╗")
    print(f"║ {title.center(46)} ║")
    print("╚" + "═"*48 + "╝" + RESET)

def display_results(result, duration):
    fz, fr = result
    print(f"  ❄️  {CYAN}FREEZER STATUS{RESET}")
    print(f"     Inventory: {fz['count']} | {RED}Expired: {fz['expired']}{RESET}")
    print(f"  🥦  {GREEN}FRIDGE STATUS{RESET}")
    print(f"     Inventory: {fr['count']} | {RED}Expired: {fr['expired']}{RESET}")
    print(f"  ⏱️  {GREEN}Execution Time: {duration:.4f} seconds{RESET}")

# --- THREADING (CONCURRENT) ---
def run_threading(data):
    start = time.time()
    chunk_size = len(data) // CORES
    threads, results = [], []
    def worker(chunk): results.append(analyze_chunk(chunk))
    
    for i in range(CORES):
        t = threading.Thread(target=worker, args=(data[i*chunk_size:(i+1)*chunk_size],))
        threads.append(t); t.start()
    for t in threads: t.join()
    
    return merge_results(results), time.time() - start

# --- MULTIPROCESSING (PARALLEL) ---
def run_multiprocessing(data):
    start = time.time()
    chunk_size = len(data) // CORES
    chunks = [data[i*chunk_size:(i+1)*chunk_size] for i in range(CORES)]
    with multiprocessing.Pool(processes=CORES) as pool:
        results = pool.map(analyze_chunk, chunks)
    return merge_results(results), time.time() - start
=======
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
>>>>>>> c25b537f3538f1038d370eef21086cd609b8bdd9

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
<<<<<<< HEAD
    print(f"{CYAN}--- SARAH'S SMART FRIDGE DIAGNOSTIC SYSTEM ---{RESET}")
    print(f"System: {CORES} Cores Detected | Task: Analyzing {NUM_ITEMS} items...")
    
    data = generate_data(NUM_ITEMS)

    # 1. Sequential Race
    print_header("1. SEQUENTIAL SCAN (Single Core)")
    res_s, t_s = analyze_chunk(data), 0 # Baseline placeholder logic
    start_s = time.time()
    res_s = analyze_chunk(data)
    t_s = time.time() - start_s
    display_results(res_s, t_s)

    # 2. Threading Race
    print_header("2. THREADING SCAN (Concurrent)")
    res_t, t_t = run_threading(data)
    display_results(res_t, t_t)

    # 3. Multiprocessing Race
    print_header("3. PARALLEL SCAN (Multi-Core)")
    res_m, t_m = run_multiprocessing(data)
    display_results(res_m, t_m)

    # Final Comparison
    print(f"\n{GREEN}🏆 WINNER: MULTIPROCESSING{RESET}")
    print(f"🚀 Speedup Ratio: {t_s/t_m:.2f}x faster than Sequential")
=======
    print("Generating Smart Fridge Data...\n")
    data = generate_data(NUM_ITEMS)

    seq, t1 = run_sequential(data)
    display("SEQUENTIAL", seq, t1)

    thr, t2 = run_threading(data)
    display("THREADING", thr, t2)

    mp, t3 = run_multiprocessing(data)
    display("MULTIPROCESSING", mp, t3)
>>>>>>> c25b537f3538f1038d370eef21086cd609b8bdd9
