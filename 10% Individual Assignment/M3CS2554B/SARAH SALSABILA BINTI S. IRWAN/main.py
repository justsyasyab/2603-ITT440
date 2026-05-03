import time
import multiprocessing
import threading
from datetime import datetime
from fridge_engine import generate_data, analyze_chunk, merge_results, draw_graph, RED, GREEN, CYAN, YELLOW, RESET

# Settings for the test
NUM_ITEMS = 10000 
CORES = multiprocessing.cpu_count()

def scan_display(data, filter_type):
    """Displays a sample of items based on user choice."""
    today = datetime.now()
    print(f"\n{YELLOW}--- 📋 SCANNING {filter_type} SECTION ---{RESET}")
    count = 0
    for item in data:
        is_expired = item['expiry'] < today and item['consumed'] == "No"
        show = False
        if filter_type == "TOP" and item['section'] == "TOP": show = True
        elif filter_type == "BOTTOM" and item['section'] == "BOTTOM": show = True
        elif filter_type == "EXPIRED" and is_expired: show = True
        
        if show:
            color = RED if is_expired else GREEN
            print(f"{color}Item: {item['item']:<8} | Category: {item['category']:<6} | "
                  f"Expiry: {item['expiry'].strftime('%Y-%m-%d')} | Consumed: {item['consumed']}{RESET}")
            count += 1
            if count >= 10: break

def run_benchmarks(data):
    """Executes and compares Sequential, Concurrent, and Parallel techniques."""
    print(f"\n{YELLOW}--- 🚀 STARTING TRIPLE-TECHNIQUE COMPARISON ---{RESET}")

    # 1. SEQUENTIAL
    print(f"{CYAN}Running Sequential Baseline...{RESET}")
    s_start = time.time()
    res_s = analyze_chunk(data)
    t_seq = time.time() - s_start

    # 2. CONCURRENT (THREADING)
    print(f"{CYAN}Running Concurrent (Threading)...{RESET}")
    t_start = time.time()
    results_t = []
    chunk_size = len(data) // CORES
    def worker(chunk):
        results_t.append(analyze_chunk(chunk))
    
    threads = []
    for i in range(CORES):
        start_idx = i * chunk_size
        end_idx = None if i == CORES - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=worker, args=(data[start_idx:end_idx],))
        threads.append(t); t.start()
    for t in threads: t.join()
    t_thr = time.time() - t_start

    # 3. PARALLEL (MULTIPROCESSING)
    print(f"{CYAN}Running Parallel (Multiprocessing)...{RESET}")
    m_start = time.time()
    chunks = [data[i*chunk_size : (None if i == CORES - 1 else (i + 1) * chunk_size)] for i in range(CORES)]
    with multiprocessing.Pool(processes=CORES) as pool:
        results_m = pool.map(analyze_chunk, chunks)
    t_mp = time.time() - m_start

    # OUTPUT FINAL PERFORMANCE COMPARISON
    draw_graph([t_seq, t_thr, t_mp])
    print(f"\n{GREEN}🏆 RESULTS SUMMARY{RESET}")
    print(f"Sequence Time     : {t_seq:.4f}s")
    print(f"Concurrent Time   : {t_thr:.4f}s")
    print(f"Parallel Time     : {t_mp:.4f}s ")
    print(f"\n{YELLOW}Final Speedup Ratio (Parallel vs Seq): {t_seq/t_mp:.2f}x{RESET}")

if __name__ == "__main__":
    # Generate the large dataset once
    data = generate_data(NUM_ITEMS)
    
    while True:
        print(f"\n{YELLOW}主 SMART FRIDGE MENU{RESET}")
        print("1. View TOP Section (Dairy/Meat)")
        print("2. View BOTTOM Section (Drink/Veg)")
        print("3. View EXPIRED Items")
        print("4. Close Fridge & Run Benchmarks (Sequence, Concurrent, Parallel)")
        
        choice = input(f"{CYAN}Enter Choice: {RESET}")
        
        if choice == '1': scan_display(data, "TOP")
        elif choice == '2': scan_display(data, "BOTTOM")
        elif choice == '3': scan_display(data, "EXPIRED")
        elif choice == '4':
            run_benchmarks(data)
            break
        
        cont = input(f"\nKeep fridge open? (y/n): ").lower()
        if cont == 'n':
            run_benchmarks(data)
            break
