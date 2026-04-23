# SARAH SALSABILA BINTI S. IRWAN
# 🧬 DNA SEQUENCE MATCHING SYSTEM 

---

## 📄 Article: Performance Analysis of Parallel Processing
In modern computational biology, analyzing DNA sequences requires massive processing power. This project demonstrates a **Parallel Computing** approach to compare **1,000,000 DNA sequences** against a target pattern. By utilizing the `multiprocessing` library in Python, we distribute the workload across multiple CPU cores to reduce execution time compared to traditional sequential processing.

### 📊 System Performance Results
The following results were obtained using a **GitHub Codespace (Dual-Core)** environment:

| Metric | Results |
| :--- | :--- |
| **Total Sequences Processed** | 1,000,000 |
| **CPU Cores Detected** | 2 |
| **Sequential Execution Time** | 6.74 seconds |
| **Parallel Execution Time** | 6.67 seconds |
| **Final Speedup Ratio** | **1.01x Speedup** |

---

## 📘 User Manual 

### 1. System Requirements
* **Python Version:** Python 3.8 or higher.
* **Libraries:** `random`, `time`, and `multiprocessing` (Standard built-in libraries).
* **Environment:** Windows, macOS, Linux, or GitHub Codespaces.

### 2. Installation & Running
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/justsyasyab/2603-ITT440.git](https://github.com/justsyasyab/2603-ITT440.git)
    ```
2.  **Navigate to the Folder:**
    ```bash
    cd "10% Individual Assignment/M3CS2554B/SARAH SALSABILA BINTI S. IRWAN"
    ```
3.  **Run the Program:**
    ```bash
    python3 main.py
    ```

### 3. Sample Input & Output
* **Input:** Automatically generated dataset of 1,000,000 random 100-base DNA strings.
* **Output:** A visual scan of DNA sequences followed by a performance comparison table.

---

## 📸 Demonstration
Below is the system execution in the GitHub Codespace terminal:

**DNA Visualization & Processing:**
![DNA Visualization](labassgnDNA.PNG)

**Final Performance Summary:**
![Performance Summary](labassgnDNA2.PNG)

---

## 💻 Source Code
### 1. main.py
### 1. dna_processor.py
```python
import random

def generate_dna_data(size, length=100):
    """Generates a list of random DNA sequences."""
    bases = ['A', 'T', 'C', 'G']
    return [''.join(random.choices(bases, k=length)) for _ in range(size)]

def calculate_mismatch(seq1, seq2):
    """Counts differences between two DNA strings."""
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

def process_chunk(sequences, target):
    """Processes a chunk of DNA for parallel execution."""
    return [calculate_mismatch(s, target) for s in sequences]

