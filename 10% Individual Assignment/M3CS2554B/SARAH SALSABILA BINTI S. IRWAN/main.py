import time
import multiprocessing
from dna_processor import generate_dna_data, calculate_mismatch, process_chunk

def run_system():
    TOTAL_DATA = 1_000_000
    TARGET_DNA = "ATCG" * 25 
    
    print("--- 🧬 DNA PATTERN MATCHING SYSTEM ---")
    print(f"Generating {TOTAL_DATA} DNA sequences...")
    data = generate_dna_data(TOTAL_DATA)
    
    print("\n[VISUAL DNA SCAN - SAMPLE DATA]")
    for i in range(10):
        print(f"Sequence {i+1:02d}: {data[i][:60]}...")
        time.sleep(0.1)
    print("---------------------------------------\n")

    cores = multiprocessing.cpu_count()
    print(f"Detected {cores} CPU cores.")

    # --- SEQUENTIAL EXECUTION ---
    print(f"\nRunning Sequential Analysis (Single Process)...")
    start_time = time.time()
    seq_results = [calculate_mismatch(s, TARGET_DNA) for s in data]
    end_seq = time.time() - start_time
    print(f"Done. Time: {end_seq:.2f}s")

    # --- CONCURRENT EXECUTION ---
    print(f"\nRunning Concurrent Analysis (Using {cores} Processes)...")
    chunk_size = TOTAL_DATA // cores
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    start_time = time.time()
    with multiprocessing.Pool(processes=cores) as pool:
        # Utilizing Process-level Concurrency
        par_results = pool.starmap(process_chunk, [(c, TARGET_DNA) for c in chunks])
    end_con = time.time() - start_time
    print(f"Done. Time: {end_con:.2f}s")

    # --- FINAL PERFORMANCE REPORT ---
    speedup = end_seq / end_con
    print("\n" + "="*40)
    print("       CONCURRENCY PERFORMANCE REPORT")
    print("="*40)
    print(f"Sequential Execution Time : {end_seq:.2f}s")
    print(f"Concurrent Execution Time : {end_con:.2f}s")
    print(f"Final Speedup Factor      : {speedup:.2f}x")
    print("="*40)

if __name__ == "__main__":
    run_system()
