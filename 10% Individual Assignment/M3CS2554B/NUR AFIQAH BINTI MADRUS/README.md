# Even and Odd Number Counter: A Performance Analysis of Sequential vs Concurrent vs Parallel Processing
## Processing 10 Million Numbers Using Python

**NAME:** NUR AFIQAH BINTI MADRUS

**STUDENT ID:** 2024236602

**CLASS**: M3CS2554B

**COURSE CODE:** ITT440 NETWORK PROGRAMMING

**PREPARED FOR:** SIR SHAHADAN BIN SAAD

**YOUTUBE LINK:** https://youtu.be/WxdMk3FbTWE?si=fQ8cyef61xSS9wqB

## 1. Introduction
### 1.1 Problem Statement
<p align="justify">
Processing large datasets efficiently is a common challenge in computing. When working with millions of numbers, the choice of processing approach can significantly impact execution time. This project investigates three different processing approaches, sequential, concurrent (threading), and parallel (multiprocessing) to determine which method performs best for a CPU-intensive counting and statistics task on 10 million random numbers.
    
### 1.2 Project Objectives
The main objectives of this project are:

1) To develop a Python program that counts even and odd numbers from a large dataset
2) To compute 8 statistical metrics from the processed numbers
3) To compare the performance of sequential, concurrent, and parallel processing approaches
## 2. Program Design
### 2.1 Overview of the Application
The application generates 10 million random numbers between 1 and 1,000,000, then processes them using three different approaches to compute the following 8 output metrics:
| No. | Metric                   |
|-----|--------------------------|
| 1   | Total Even Numbers       |
| 2   | Total Odd Numbers        |
| 3   | Sum of Even Numbers      |
| 4   | Sum of Odd Numbers       |
| 5   | Minimum Even Number      |
| 6   | Maximum Even Number      |
| 7   | Minimum Odd Number       |
| 8   | Maximum Odd Number       |
### 2.2 Three Processing Approaches
**Approach 1: Sequential Processing**

The baseline approach where numbers are processed one at a time in a single loop. This serves as the reference point for measuring speedup in other approaches.

**Approach 2: Concurrent Processing (Threading)**

Numbers are split into 8 equal chunks, and each chunk is processed by a separate thread. Python threads share the same memory space but are limited by the Global Interpreter Lock (GIL), which allows only one thread to execute Python code at a time.

**Approach 3: Parallel Processing (Multiprocessing)**

Numbers are split into 8 equal chunks, and each chunk is processed by a separate process. Each process has its own Python interpreter and memory space, allowing true parallel execution across multiple CPU cores.
### 2.3 System Configuration
| Parameter            | Value        |
|----------------------|--------------|
| Total Numbers        | 10,000,000   |
| Number Range         | 1 - 1,000,000|
| Number of Workers    | 8            |
## 3. Implementation Details
### 3.1 Data Structures Used
The program uses a ```Statistics``` dataclass to hold all 8 output metrics for each processing chunk:

```
@dataclass
class Statistics:
    total_even: int = 0
    total_odd: int = 0
    sum_even: int = 0
    sum_odd: int = 0
    min_even: int = float('inf')
    max_even: int = 0
    min_odd: int = float('inf')
    max_odd: int = 0
```
### 3.2 Data Generation
Random numbers are generated using Python's ```random.randint()``` function and stored in a list. A sample of the first 10,000 numbers is saved to a CSV file for verification purposes.
### 3.3 Chunk Division Strategy
For concurrent and parallel processing, the data is divided equally:

```
def split_data(data, num_chunks):
    chunk_size = len(data) // num_chunks
    # Create equal-sized chunks
```
With 10 million numbers and 8 workers, each chunk contains approximately 1,250,000 numbers.
### 3.4 Merging Results
After all chunks are processed, individual statistics are merged using a dedicated function that combines counts, sums, and finds global minimums and maximums.
### 3.5 Threading Implementation
The concurrent approach uses Python's ```threading``` module:

- Creates 8 threads, each processing one chunk
- Uses a lock to safely append results to a shared list
- Threads run concurrently but not truly in parallel due to the GIL
### 3.6 Multiprocessing Implementation
The parallel approach uses ```ProcessPoolExecutor``` from ```concurrent.futures```:

- Creates a pool of 8 worker processes
- Maps the processing function to each chunk
- Each process runs independently with its own memory space
- Results are collected and merged after all processes complete
## 4. Results and Analysis
### 4.1 Output Files Generated
The program generates several output files:

| File Name                      | Description                                      |
|-------------------------------|--------------------------------------------------|
| generated_numbers.csv         | Sample of 10,000 generated numbers              |
| results_output.csv            | All 8 metrics for each approach                 |
| performance_comparison.csv    | Execution times and speedup factors             |
| performance_graph.png         | Bar chart visualization                         |

**Generated Numbers**
<img width="198" height="147" alt="image" src="https://github.com/user-attachments/assets/ca163965-a463-4175-9cfe-a6285ef765f4" />

**Result Output**
<img width="680" height="286" alt="image" src="https://github.com/user-attachments/assets/cf857f20-8426-4224-9059-6d41cdd94d74" />

**Performance Comparison**
<img width="438" height="113" alt="image" src="https://github.com/user-attachments/assets/70fd2622-725c-4eb1-afb5-61e0982c60b5" />

**Performance Graph**
<img width="1461" height="650" alt="image" src="https://github.com/user-attachments/assets/1e2e868e-13ca-4181-ba6b-39f9351f3549" />

## 5. Conclusion
<p align="justify">
This project successfully demonstrated the differences between sequential, concurrent, and parallel processing in Python by processing 10 million numbers and computing 8 statistical metrics. The sequential approach served as a reliable baseline, completing the task in a straightforward manner without any additional overhead. The threading approach performed poorly due to Python's Global Interpreter Lock (GIL), which prevents true parallel execution by allowing only one thread to run at a time, adding unnecessary overhead without any speed benefit for CPU-intensive tasks. In contrast, the multiprocessing approach achieved the best performance by bypassing the GIL completely, as each process runs independently on separate CPU cores with its own Python interpreter, enabling true parallel execution. These findings clearly show that for CPU-bound tasks like large-scale number processing, multiprocessing is the optimal choice, while threading is better reserved for I/O-bound operations, and sequential processing remains suitable for simpler tasks where code simplicity matters more than performance.
