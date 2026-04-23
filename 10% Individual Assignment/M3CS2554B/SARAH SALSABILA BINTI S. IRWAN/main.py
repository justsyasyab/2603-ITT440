import time
import multiprocessing
from dna_processor import generate_dna_data, calculate_mismatch, process_chunk

def run_system():
    # --- CONFIGURATION ---
    TOTAL_DATA = 1_000_000
    TARGET_DNA = "ATCG" * 25  # The 100-base sequence to match against
    
    print("--- 🧬 DNA PATTERN MATCHING SYSTEM ---")
    print(f"Generating {TOTAL_DATA} DNA sequences...")
    data = generate_dna_data(TOTAL_DATA)
    
    # --- VISUAL SCAN (For the Video Demo) ---
    print("\n[VISUAL DNA SCAN - SAMPLE DATA]")
    for i in range(10):
        print(f"Sequence {i+1:02d}: {data[i][:60]}...")
        time.sleep(0.1)
    print("---------------------------------------\n")

    cores = multiprocessing.cpu_count()
    print(f"Detected {cores} CPU cores.")

    # --- SEQUENTIAL EXECUTION ---
    print(f"\nRunning Sequential Analysis (Using 1 Core)...")
    start_time = time.time()
    seq_results = [calculate_mismatch(s, TARGET_DNA) for s in data]
    end_seq = time.time() - start_time
    print(f"Done. Time: {end_seq:.2f}s")

    # --- PARALLEL EXECUTION ---
    print(f"\nRunning Parallel Analysis (Using {cores} Cores)...")
    chunk_size = TOTAL_DATA // cores
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    start_time = time.time()
    with multiprocessing.Pool(processes=cores) as pool:
        # Mapping the chunks to different CPU cores
        par_results = pool.starmap(process_chunk, [(c, TARGET_DNA) for c in chunks])
    end_par = time.time() - start_time
    print(f"Done. Time: {end_par:.2f}s")

    # --- FINAL REPORT ---
    speedup = end_seq / end_par
    print("\n" + "="*30)
    print("       FINAL PERFORMANCE")
    print("="*30)
    print(f"Sequential Time : {end_seq:.2f}s")
    print(f"Parallel Time   : {end_par:.2f}s")
    print(f"Speedup Factor  : {speedup:.2f}x")
    print("="*30)

if __name__ == "__main__":
    run_system()
