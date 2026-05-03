# NUR AMNA INSYIRAH BINTI AMIN
# STUDENT ID: 2024230024
# ITT440-INDIVIDUAL ASSIGNMENT 
# CLASSIFICATION OF LARGE-SCALE NUMERIC DATASET 

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/24d630db-f607-42e2-b653-a0e775b89188" />

# INTRODUCTION 
This project focuses on the implementation and performance evaluation of parallel programming techniques using Python. The task involves classifying a massive dataset of **5,000,000 numeric records** into three distinct categories (Category A, B, and C) based on CPU-bound mathematical logic. This project demonstrates how hardware resources can be optimized to reduce execution time in data-heavy environments. 

Three distinct categories:

**Category A:** Result of calculation > 500

**Category B:** Result of calculation > 200

**Category C:** Result of calculation ≤ 200

# PROBLEM STATEMENT 
In traditional sequential programming, tasks are processed one after another using only a single CPU core. When dealing with millions of data points, this creates a significant performance bottleneck, leaving modern multi-core processors underutilized. This project addresses the inefficiency of single-threaded execution by implementing **Multiprocessing** allowing the workload to be distributed across all available logical processors. 

# SYSTEM SPECIFICATIONS 
The analysis was conducted on a high-performance laptop with the following specifications:

-**Processor:** AMD Ryzen 5 7535HS 

-**Architecture:** 6 Physical Cores, 12 Logical Processors

-**Base Speed:** 3.30 GHz

-**Memory (RAM):** 8.0 GB 

-**Operating System:** Windows 11

# METHODOLOGY 
The classification logic involves complex mathematical operations to simulate a heavy CPU-bound workload. Three approaches were compared:

1. **Sequential:** Using a standard 'for' loop (Single core).
2. **Threading:** Using 'ThreadPoolExecutor' (Concurrency).
3. **Multiprocessing:** Using 'ProcessPoolExecutor' (True Parallelism).

# INSTALLATION & SETUP GUIDE 

1. Install VSCode
2. Install Python 3.13
3. Install libraries in VSCode
   ```bash
   pip install numpy pandas matplotlib
   ```
4. Run the script
   ```bash
   python main_script.py
   ```

# IMPLEMENTATION CODE
```python
   import time
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# --- 1. CLASSIFICATION LOGIC WITH WATERFALL EFFECT ---
def classify_data(data_chunk, worker_type="Worker"):
    """
    Performs heavy math calculations and prints status updates 
    to create a 'waterfall' effect in the terminal.
    """
    process_id = os.getpid()
    results = []
    
    # We use enumerate to print progress every 500 rows
    for i, val in enumerate(data_chunk):
        # Heavy CPU workload (Trigonometry + Logarithms)
        calc = np.sqrt(val**2 + np.log1p(val)) * np.sin(val)
        
        # WATERFALL EFFECT: Print status every 500 items
        if i % 500 == 0:
            print(f"[{worker_type}] PID:{process_id} | Index:{i} | Value:{val:.2f} | Status: OK")
            
        if calc > 500:
            results.append("Category A")
        elif calc > 200:
            results.append("Category B")
        else:
            results.append("Category C")
            
    return results

# --- 2. HELPER FUNCTIONS (REQUIRED FOR WINDOWS MULTIPROCESSING) ---
# Windows Multiprocessing does not support 'lambda' functions.
# These named functions allow the ProcessPool to 'pickle' the tasks correctly.
def classify_process_helper(chunk):
    return classify_data(chunk, "Process")

def classify_thread_helper(chunk):
    return classify_data(chunk, "Thread")

def main():
    # --- 3. GENERATING DATA ---
    print("="*60)
    print("PROJECT: PARALLEL COMPUTING - 5 MILLION DATA CLASSIFICATION")
    print("="*60)
    
    data_size = 5_000_000  
    print(f"Status: Generating {data_size:,} random numeric data points...")
    data = np.random.uniform(1, 1000, data_size)
    
    cpu_cores = os.cpu_count()
    data_chunks = np.array_split(data, cpu_cores)
    print(f"System Info: Detected {cpu_cores} Logical Processors.\n")

    # --- 4. SEQUENTIAL EXECUTION (BASELINE) ---
    print("--- Running Sequential Approach ---")
    start_time = time.perf_counter()
    # We process a 100k sample to avoid waiting minutes for the baseline
    classify_data(data[:100000], "Sequential") 
    # Calculate estimated duration for the full 5 million
    sequential_duration = (time.perf_counter() - start_time) * (data_size/100000)
    print(f"Sequential Execution Time (Estimated): {sequential_duration:.4f} seconds\n")

    # --- 5. CONCURRENT EXECUTION (THREADING) ---
    print("--- Running Concurrent Approach (Threading) ---")
    start_time = time.perf_counter()
    with ThreadPoolExecutor(max_workers=cpu_cores) as executor:
        list(executor.map(classify_thread_helper, data_chunks))
    threading_duration = time.perf_counter() - start_time
    print(f"Threading Execution Time: {threading_duration:.4f} seconds\n")

    # --- 6. PARALLEL EXECUTION (MULTIPROCESSING) ---
    print("--- Running Parallel Approach (Multiprocessing) ---")
    start_time = time.perf_counter()
    final_results = []
    with ProcessPoolExecutor(max_workers=cpu_cores) as executor:
        # Collecting results for the CSV output
        for res in executor.map(classify_process_helper, data_chunks):
            final_results.extend(res)
            
    multiprocessing_duration = time.perf_counter() - start_time
    print(f"Multiprocessing Execution Time: {multiprocessing_duration:.4f} seconds\n")

    # --- 7. SAVE RESULTS TO CSV (10,000 SAMPLE ROWS) ---
    print("Saving sample results to 'output_results.csv'...")
    # Saving only a sample to keep the file size manageable for GitHub
    df = pd.DataFrame({'Input_Value': data[:10000], 'Category': final_results[:10000]})
    df.to_csv('output_results.csv', index=False)
    print("[✓] CSV Saved.\n")

    # --- 8. PERFORMANCE SUMMARY & VISUALIZATION ---
    print("="*60)
    speedup_ratio = sequential_duration / multiprocessing_duration
    print(f"RESULTS: Parallelism is {speedup_ratio:.2f}x faster than Sequential!")
    print("="*60)

    # Plotting the Performance Graph
    methods = ['Sequential', 'Threading', 'Multiprocessing']
    times = [sequential_duration, threading_duration, multiprocessing_duration]
    
    plt.figure(figsize=(10, 6))
    plt.bar(methods, times, color=['#ff79c6', '#bd93f9', '#8be9fd'])
    plt.ylabel('Time (Seconds)')
    plt.title('Performance Analysis: Sequential vs Threading vs Multiprocessing')
    
    # Save the graph as an image for your GitHub README
    plt.savefig('performance_graph.png')
    print("Graph saved as 'performance_graph.png'. Displaying plot...")
    plt.show()

  if __name__ == "__main__":
    main()
   ```
# PERFORMANCE RESULT & OBSERVATION 
<img width="752" height="442" alt="image" src="https://github.com/user-attachments/assets/38a3612a-c5d9-462a-8f39-23eb865ee38c" />

RESULTS: Parallelism is 1.60x faster than Sequential


# CONCLUSION 
The results clearly indicate that Multiprocessing is the superior approach for CPU-bound tasks in Python. While Threading offers slight improvements, it is still hindered by the GIL. Multiprocessing effectively distributed the 5 million data points across all 12 logical processors, proving that hardware-aware programming is essential for large-scale data science and engineering tasks.

# VIDEO DEMONSTRATION 
https://youtu.be/B2L96EpZjDE
