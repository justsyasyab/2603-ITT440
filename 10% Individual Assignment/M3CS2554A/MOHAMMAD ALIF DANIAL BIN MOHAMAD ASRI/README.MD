
# 🚀 ADAPTIVE HYBRID PARALLEL SMART CITY TRAFFIC SIMULATOR
# NAME: MOHAMMAD ALIF DANIAL BIN MOHAMAD ASRI
# STUDENT ID: 2024237606
# CLASS: CS2554A
# COURSE: ITT440 - PARALLEL PROGRAMMING
# LECTURER: SHAHADAN BIN SAAD

"""
📌 INTRODUCTION

In today’s digital environment, urban infrastructure systems are required to 
handle large-scale data efficiently. Traditional sequential programming executes 
tasks one at a time, resulting in significant delays when processing vehicle 
physics updates. This project demonstrates optimization via parallel programming.

📊 PROJECT OVERVIEW

A high-performance traffic monitoring system checking physics logic for 5,000 
vehicle agents. Features classification logic and performance benchmarking.

🎯 OBJECTIVES

* Implement sequential, concurrent, and parallel techniques.
* Process large-scale vehicle datasets efficiently.
* Demonstrate workload distribution across multiple CPU cores.

🏗️ SYSTEM DESIGN

* Vehicle Loader: Generates 5,000 vehicle agent IDs.
* Physics Engine: Performs 10^5 mathematical iterations per agent.
* Flow Classifier: Categorizes results (OPTIMAL, HEAVY, CONGESTED).

▶️ HOW TO RUN

1. Save this code as 'main.py'.
2. Open terminal/command prompt.
3. Run the command: python main.py
4. Select options from the menu to see performance differences.

🖥️ PROGRAM MENU

1. Sequential Execution
2. Threading Execution (Concurrent)
3. Multiprocessing Execution (Parallel)
4. Run All & Compare Performance
5. Exit System

🧪 SAMPLE INPUT

Dataset: 5,000 Vehicle Agents (Internal ID List: 1 to 5,000).
Complexity: 100,000 math operations (sqrt, tan) per ID.

📝 SAMPLE OUTPUT

Vehicle ID: 1     | Status: SUCCESS  | Latency: 0.045s | Flow: OPTIMAL FLOW

Vehicle ID: 2     | Status: SUCCESS  | Latency: 0.125s | Flow: HEAVY TRAFFIC

[MULTIPROCESSING] Total Time: 12.30s

⚡ PERFORMANCE ANALYSIS

Method          | Time (seconds) | Performance
----------------|----------------|------------
Sequential      | ~45.00s        | Very Slow
Threading       | ~47.00s        | Slow
Multiprocessing | ~12.00s        | Fast (Winner)

🎥 DEMONSTRATION VIDEO

Link: https://youtu.be/nVDNVNwAD1U

🧩 CHALLENGES FACED

* GIL Limitations: Overcoming the Global Interpreter Lock that slows threading.
* Data Scale: Managing physics updates for 5,000 agents in real-time.
* System Overhead: Balancing the number of processes with available CPU cores.

💡 CONCLUSION

Multiprocessing is the superior choice for CPU-bound simulations, bypasses 
the GIL, and achieves maximum hardware utilization.

💡 CODE

import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import math
import random

# =========================================================
# GLOBAL CONFIGURATION
# =========================================================
TOTAL_VEHICLES = 5000
MATH_COMPLEXITY = 10**5 

# =========================================================
# DATA LOADER
# =========================================================
def load_traffic_data():
    print(f"✅ Generating/Loading {TOTAL_VEHICLES} Vehicle Agents...")
    return [i for i in range(1, TOTAL_VEHICLES + 1)]

# =========================================================
# PHYSICS ENGINE
# =========================================================
def check_vehicle_physics(v_id):
    start = time.perf_counter()
    try:
        # CPU-bound math task simulating heavy vehicle movement physics
        calc = 0
        for i in range(MATH_COMPLEXITY):
            calc += math.sqrt(i) * math.tan(i)
        duration = round(time.perf_counter() - start, 3)
        return (v_id, "SUCCESS", duration)
    except Exception:
        return (v_id, "FAILED", 0)

# =========================================================
# CLASSIFICATION
# =========================================================
def classify_flow(result):
    _, status, t = result
    if status == "FAILED": return "FAILED"
    elif t < 0.05: return "OPTIMAL FLOW"
    elif t < 0.15: return "HEAVY TRAFFIC"
    else: return "CONGESTED"

# =========================================================
# PRINT RESULTS
# =========================================================
def print_results(results):
    print("\n--- SIMULATION SAMPLE ---")
    print(f"{'Vehicle ID':<12} | {'Status':<10} | {'Latency':<10} | {'Flow'}")
    print("-" * 60)
    for r in results[:15]:
        print(f"{r[0]:<12} | {r[1]:<10} | {r[2]:<10}s | {classify_flow(r)}")
    print(f"... total: {len(results)} Vehicles Processed")

# =========================================================
# EXECUTION MODULES
# =========================================================
def sequential(vehicles):
    print("\n[SEQUENTIAL] Running...")
    start = time.perf_counter()
    results = [check_vehicle_physics(v) for v in vehicles]
    total = time.perf_counter() - start
    print_results(results)
    print(f"[SEQUENTIAL] Total Time: {total:.2f}s")
    return total

def threading_version(vehicles):
    print("\n[THREADING] Running...")
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=200) as executor:
        results = list(executor.map(check_vehicle_physics, vehicles))
    total = time.perf_counter() - start
    print_results(results)
    print(f"[THREADING] Total Time: {total:.2f}s")
    return total

def multiprocessing_version(vehicles):
    print("\n[MULTIPROCESSING] Running...")
    start = time.perf_counter()
    processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes) as pool:
        results = pool.map(check_vehicle_physics, vehicles)
    total = time.perf_counter() - start
    print_results(results)
    print(f"[MULTIPROCESSING] Total Time: {total:.2f}s")
    return total

# =========================================================
# MAIN INTERFACE
# =========================================================
def main():
    vehicles = load_traffic_data()
    
    while True:
        print("\n" + "="*45)
        print("     SMART CITY TRAFFIC CHECKER MENU")
        print("="*45)
        print("1. Sequential Execution")
        print("2. Threading Execution (Concurrent)")
        print("3. Multiprocessing Execution (Parallel)")
        print("4. Run All & Compare Performance")
        print("5. Exit System")

        choice = input("\nChoose Option (1-5): ")

        if choice == "1":
            sequential(vehicles)
        elif choice == "2":
            threading_version(vehicles)
        elif choice == "3":
            multiprocessing_version(vehicles)
        elif choice == "4":
            s = sequential(vehicles)
            t = threading_version(vehicles)
            m = multiprocessing_version(vehicles)
            print("\n" + "="*45)
            print("         PERFORMANCE COMPARISON")
            print("="*45)
            print(f"{'Method':<25} | {'Time':<15}")
            print("-" * 45)
            print(f"{'Sequential':<25} | {s:<15.2f}s")
            print(f"{'Threading':<25} | {t:<15.2f}s")
            print(f"{'Multiprocessing':<25} | {m:<15.2f}s")
            print("="*45)
            print(f"WINNER: MULTIPROCESSING ({s/m:.2f}x faster)")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("❌ Invalid Choice.")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
