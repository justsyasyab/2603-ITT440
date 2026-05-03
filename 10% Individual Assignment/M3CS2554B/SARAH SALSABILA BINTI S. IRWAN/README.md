# SARAH SALSABILA BINTI S. IRWAN
# Parallel Smart Fridge Consumption Analyzer  

---

## 📖 Project Overview
This project applies **Parallel Programming** to an IoT Smart Fridge simulation designed for high-inventory environments like industrial kitchens. The system is engineered to scan thousands of items to detect expiration while filtering out items already marked as "consumed."

By splitting the fridge into **TOP** and **BOTTOM** sections, the system demonstrates how multi-core processing handles heavy diagnostic tasks more efficiently than standard sequential methods.

---

## 🛠️ System Requirements
*   **Language:** Python 3.8+
*   **Hardware:** Multi-core CPU (Tested on 2+ Cores)
*   **Dependencies:** Standard Python Libraries (`multiprocessing`, `threading`, `random`)

---

## 🚀 Installation & Usage

1. **Clone the project:**
   ```bash
   git clone [https://github.com/justsyasyab/2603-ITT440.git](https://github.com/justsyasyab/2603-ITT440.git)
    """Processes a chunk of DNA for parallel execution."""
    return [calculate_mismatch(s, target) for s in sequences]

2. **Navigate to the directory:**
   ```bash
   cd "10% Individual Assignment/M3CS2554B/SARAH SALSABILA BINTI S. IRWAN"

 3. **Run the Diagnostic System:**
   ```bash
   python3 main.py
```
## 📁 Source Code Implementation

The following code snippets represent the core logic of the **Parallel Smart Fridge Analyzer**.

### 1. fridge_engine.py
This module handles data synthesis and defines the analytical algorithm.

```python
import random
import time
from datetime import datetime, timedelta

# ANSI Colors for a professional dashboard look
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

CATEGORIES = {
    "Dairy": ["Milk", "Cheese", "Yogurt"],
    "Meat": ["Chicken", "Beef", "Fish"],
    "Drink": ["Juice", "Soda", "Water"],
    "Veg": ["Carrot", "Spinach", "Broccoli"]
}

def generate_data(n):
    """Generates bulk inventory data with items, categories, and sections."""
    data = []
    today = datetime.now()
    cat_list = list(CATEGORIES.keys())
    for _ in range(n):
        cat = random.choice(cat_list)
        item_name = random.choice(CATEGORIES[cat])
        section = "TOP" if cat in ["Dairy", "Meat"] else "BOTTOM"
        expiry = today + timedelta(days=random.randint(-5, 10))
        consumed = random.choice(["Yes", "No"])
        data.append({
            "item": item_name, "category": cat, "section": section,
            "expiry": expiry, "consumed": consumed
        })
    return data

def analyze_chunk(chunk):
    """Core logic used for Sequence, Concurrent, and Parallel analysis."""
    today = datetime.now()
    results = {"TOP": {"total": 0, "expired": 0}, "BOTTOM": {"total": 0, "expired": 0}}
    for item in chunk:
        # Simulate sensor data processing time (0.0001s per item)
        # This makes the parallel speedup very visible.
        time.sleep(0.0001) 
        sec = item["section"]
        results[sec]["total"] += 1
        if item["expiry"] < today and item["consumed"] == "No":
            results[sec]["expired"] += 1
    return results

def merge_results(results_list):
    """Combines partial results from multiple processes/threads."""
    final = {"TOP": {"total": 0, "expired": 0}, "BOTTOM": {"total": 0, "expired": 0}}
    for res in results_list:
        for sec in final:
            final[sec]["total"] += res[sec]["total"]
            final[sec]["expired"] += res[sec]["expired"]
    return final

def draw_graph(times):
    """Renders a text-based bar graph to visualize speed differences."""
    labels = ["Sequential", "Threading ", "Parallel  "]
    max_t = max(times)
    print(f"\n{YELLOW}📊 PERFORMANCE GRAPH{RESET}")
    for i in range(3):
        # Scale bar length to 30 characters maximum
        bar = "█" * int((times[i] / max_t) * 30)
        print(f"{labels[i]}: {bar} {times[i]:.4f}s")
```
### 2. `main.py` (Execution Control & Benchmarking)
This file serves as the user interface and the execution controller. It manages the data flow and implements the logic to compare Sequential, Concurrent, and Parallel processing.

```python
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
```
## 📊 Performance Analysis

### 🏆 Results Summary (Actual Benchmark)
| Technique | Execution Time | Speedup | Status |
| :--- | :--- | :--- | :--- |
| **Sequential** | 0.1706s | 1.00x |Baseline|
| **Concurrent** | 0.1247s | 1.37x |Fastest|
| **Parallel** | **0.1614s** | **1.06x** |Efficient|

### 🔍 Execution Comparison
| Model | Core Usage | Mechanism |
| :--- | :--- | :--- |
| **Sequential** | 1 Core | Synchronous |
| **Concurrent** | 1 Core | Shared Memory |
| **Parallel** | **All Cores** | **True Parallelism** |
---

# ❄️ Smart Fridge Inventory Analyzer

## 📖 User Manual: Interactive Menu
Once the application is launched via `python3 main.py`, use the following menu options to interact with the system:

### **1. View FRIDGE Items (Dairy/Meat)**
* **Selection**: Enter `1`.
* **Function**: Scans the primary refrigeration section.
* **Display**: Shows a list of items like "Veg" or "Dairy," their expiry dates, and whether they have been consumed.

### **2. View FREEZER Items (Frozen)**
* **Selection**: Enter `2`.
* **Function**: Specifically monitors long-term storage items.
* **Display**: Lists items assigned to the "FREEZER" section, such as "Meat".

### **3. View EXPIRED Items**
* **Selection**: Enter `3`.
* **Function**: Filters the entire inventory for items that are past their expiry date and remain unconsumed.
* **Visual Aid**: Expired items are flagged in **RED** to help users prioritize food waste reduction.

### **4. Close Fridge & Run Benchmarks**
* **Selection**: Enter `4`.
* **Function**: Terminates the user interface and triggers the technical performance analysis.
* **Output**: Generates a **Performance Graph** and a detailed **Results Summary** comparing Sequential, Concurrent, and Parallel execution.

## 📺 Demonstration Video

The following video demonstrates the **Parallel Smart Fridge Analyzer** in action. It covers:
*   **System Initialization:** Generating 10,000+ items.
*   **Interactive Menu:** Navigating through Top/Bottom fridge sections.
*   **Real-time Analysis:** Scanning for expired inventory.
*   **Performance Benchmark:** A side-by-side comparison of **Sequential**, **Concurrent**, and **Parallel** execution times, featuring the generated bar graph.

[**▶️ Click here to watch the Demonstration Video**](https://youtu.be/NPh9RIhtkvI?si=hi1MtCGKyiYOVwIq)

---

### 🎓 Assignment Details
*   **Course:** ITT440 (Parallel Programming)
*   **Faculty:** Computer and Mathematical Sciences (FSKM)
*   **Submission Date:** 3 May 2026
