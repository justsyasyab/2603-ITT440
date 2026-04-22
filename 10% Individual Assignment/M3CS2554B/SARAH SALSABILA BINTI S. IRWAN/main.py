import multiprocessing
import time
from dna_processor import generate_sequences, dna_alignment_task

def run_experiment():
    TOTAL_DATA = 1_000_000 
    target = "ACGT" * 125
    
    print(f"--- DNA Pattern Matching System ---")
    print(f"Generating {TOTAL_DATA} DNA sequences...")
    database = generate_sequences(TOTAL_DATA)
    num_cores = multiprocessing.cpu_count()
    print(f"Detected {num_cores} CPU cores.\n")

    # SEQUENTIAL
    print("Running Sequential Analysis...")
    start_s = time.time()
    dna_alignment_task(target, database)
    seq_time = time.time() - start_s
    print(f"Sequential Time: {seq_time:.2f} seconds")

    # PARALLEL
    print("\nRunning Parallel Analysis...")
    start_p = time.time()
    chunks = [database[i::num_cores] for i in range(num_cores)]
    with multiprocessing.Pool(processes=num_cores) as pool:
        pool.starmap(dna_alignment_task, [(target, chunk) for chunk in chunks])
    
    par_time = time.time() - start_p
    print(f"Parallel Time: {par_time:.2f} seconds")
    print(f"\nResult: Parallel mode is {seq_time / par_time:.2f}x faster!")

if __name__ == "__main__":
    run_experiment()
