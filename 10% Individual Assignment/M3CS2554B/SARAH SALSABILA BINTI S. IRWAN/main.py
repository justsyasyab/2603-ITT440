import time
import multiprocessing
import threading
from fridge_engine import generate_data, analyze_chunk, merge_results, RED, GREEN, CYAN, RESET

# Settings
NUM_ITEMS = 50000 
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

# --- CONCURRENT TECHNIQUE (THREADING) ---
def run_threading(data):
    start = time.time()
    chunk_size = len(data) // CORES
    threads, results = [], []
    
    def worker(chunk):
        results.append(analyze_chunk(chunk))
    
    for i in range(CORES):
        start_idx = i * chunk_size
        end_idx = None if i == CORES - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=worker, args=(data[start_idx:end_idx],))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    return merge_results(results), time.time() - start

# --- PARALLEL TECHNIQUE (MULTIPROCESSING) ---
def run_multiprocessing(data):
    start = time.time()
    chunk_size = len(data) // CORES
    chunks = [data[i*chunk_size : (None if i == CORES - 1 else (i + 1) * chunk_size)] for i in range(CORES)]
    
    with multiprocessing.Pool(processes=CORES) as pool:
        results = pool.map(analyze_chunk, chunks)
        
    return merge_results(results), time.time() - start

if __name__ == "__main__":
    print(f"{CYAN}--- SARAH'S SMART FRIDGE DIAGNOSTIC SYSTEM ---{RESET}")
    print(f"System: {CORES} Cores Detected | Task: Analyzing {NUM_ITEMS} items...")
    
    # Data Generation
    data = generate_data(NUM_ITEMS)

    # 1. Sequential Execution
    print_header("1. SEQUENTIAL SCAN (Single Core)")
    start_s = time.time()
    res_s = analyze_chunk(data)
    t_s = time.time() - start_s
    display_results(res_s, t_s)

    # 2. Threading Execution (Concurrent)
    print_header("2. THREADING SCAN (Concurrent)")
    res_t, t_t = run_threading(data)
    display_results(res_t, t_t)

    # 3. Multiprocessing Execution (Parallel)
    print_header("3. PARALLEL SCAN (Multi-Core)")
    res_m, t_m = run_multiprocessing(data)
    display_results(res_m, t_m)

    # Performance Summary
    print(f"\n{GREEN}🏆 WINNER: MULTIPROCESSING{RESET}")
    print(f"🚀 Speedup Ratio: {t_s/t_m:.2f}x faster than Sequential")