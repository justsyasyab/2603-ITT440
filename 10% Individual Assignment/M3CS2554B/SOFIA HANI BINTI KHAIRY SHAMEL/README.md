# ᯤ Parallelized Network Service Auditor and Vulnerability Scoring Engine

**Name:** Sofia Hani Binti Khairy Shamel

**Student ID:** 2024443178

**Group:** M3CDCS2554B

---

## 1. Introduction ✎

Network auditing is a fundamental pillar of cybersecurity, essential for identifying infrastructure vulnerabilities. However, traditional sequential scanning methods are fundamentally limited by their inability to handle massive datasets efficiently, often resulting in severe performance bottlenecks. This project develops a high-performance Network Service Auditor and Vulnerability Scoring Engine. By implementing and evaluating three distinct execution paradigms; Sequential, Concurrent, and Parallel. This research quantifies the architectural efficiency required for large-scale forensic discovery against a 2,000,000-task workload.

<br>

## 2. Problem Statement ⌕

The primary challenge in high-volume network auditing is the "bottleneck of scale." Conventional sequential discovery tools process tasks linearly, leading to an exponential increase in execution time as the target scope expands to millions of data points. Furthermore, naive attempts to accelerate scanning often lead to system-level instability, memory exhaustion, and process termination (zsh: killed). This project addresses the need for a scalable, memory-efficient auditor capable of processing 2,000,000 tasks without compromising the stability of the host environment.

<br>

## 3. Objectives 𖣠

* **Implement Multi-Paradigm Auditing:** Develop a unified engine capable of executing Sequential, Concurrent, and Parallel workloads.

* **Scalability Engineering:** Utilize batch-processing to handle 2,000,000 data points without exceeding system memory limits.

* **Architectural Analysis:** Quantify the performance trade-offs between I/O-bound (threading) and CPU-bound (multiprocessing) execution models.

* **Forensic Integrity:** Maintain an immutable file-based audit trail (`audit_results.txt`) for all findings.

<br>

## 4. Setup & Environment ⏻

**Table 4.1: Technical Specification of Audit Environment**

| Category | Details |
| :--- | :--- |
| **Attacker OS** | Kali Linux (Virtual Machine) |
| **Target Environment** | Localhost (127.0.0.1) - High-volume simulation |
| **Processor** | Intel Core i5 |
| **Memory (RAM)** | 8GB |
| **Language** | Python 3.10 |
| **Network** | VirtualBox NAT |

<br>

## 5. Technical Methodology ⌨︎︎ 

### 5.1 Batch-Processing Architecture
To prevent system-level process termination (`zsh: killed`), the engine segments 2,000,000 tasks into 50,000-task batches. This architectural choice ensures memory stability by maintaining a constant memory footprint regardless of total task volume.

### 5.2 Execution Paradigms
* **Sequential:** Baseline linear iteration for performance comparison.
* **Concurrent (ThreadPoolExecutor):** Utilizes lightweight threads for I/O multiplexing, ideal for masking network latency.
* **Parallel (multiprocessing.Pool):** Distributes audit logic across multiple CPU cores to bypass the Global Interpreter Lock (GIL) and maximize throughput.

<br>

## 6. Vulnerability Scoring Logic ⚑
The engine implements a quantitative risk assessment model to evaluate the security posture of the audited infrastructure. Following the completion of service discovery, the engine calculates a Risk Exposure Score on a scale of 0 to 100, where 100 represents maximum vulnerability.

### 6.1 Assessment Methodology

The scoring is based on a simple Presence-Based Weighting system. The engine checks each open port against a registry of known attack surfaces (such as SSH, FTP, and RDP).

**The Scoring Rule:**

**High-Risk Port:** Assigned a value of 1 (Critical)

**Other Port:** Assigned a value of 0 (Negligible)

### 6.2 Metric Calculation
The final score is a ratio of high-risk services to the total number of services discovered. This is expressed as a percentage:

<br>

$$\text{Risk Exposure Score} = \left( \frac{\text{Total High-Risk Ports Found}}{\text{Total Open Ports Found}} \right) \times 100$$

<br>

### 6.3 Interpretation of Results
By normalizing the data to a 0–100 scale, the auditor provides an immediate "Danger Rating" for the network:

- **Current Audit Result: 51.10 / 100**

- **Analysis:** This indicates that **51.10%** of the detected services are high-value targets. Since more than half of the accessible network surface is high-risk, immediate administrative review is recommended.

<br>

## 7. Program 𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃

<p align="center">
<img width="568" height="538" alt="Screenshot 2026-05-01 150257" src="https://github.com/user-attachments/assets/7c1777f6-1413-4203-ac45-e4d503368ef9" />
  <br>
  <b>Figure 7.1: Implementation of Heuristic Risk Assessment and Socket Discovery Logic</b>
</p>

<p>&nbsp;</p>

<p align="center">
<img width="569" height="287" alt="Screenshot 2026-05-01 150322" src="https://github.com/user-attachments/assets/89b1523d-b81d-40ba-8822-be29bf8e4777" />
  <br>
  <b>Figure 7.2: Implementation of Multi-Paradigm Execution Logic and Batch-Processing Architecture</b>
</p>

<p>&nbsp;</p>


## 8. Key Findings and Result Analysis 📊
### 8.1 Performance Benchmark Data

<br> 

**Table 8.1: Performance Benchmark Data**

| Security Metric | Value |
| :--- | :--- |
| **Total Task Volume** | 2,000,000 (Per Paradigm) |
| **Batch Processing Size** | 50,000 Tasks |
| **Sequential Execution Time** | 14.81 Seconds |
| **Concurrent Execution Time** | 63.70 Seconds |
| **Parallel Execution Time** | 14.29 Seconds |

*Note: The test volume of 2,000,000 tasks was applied identically across all three execution paradigms to establish a rigorous performance baseline.*

<p>&nbsp;</p>

<p align="center">
<img width="600" height="400" alt="Code_Bar_Image" src="https://github.com/user-attachments/assets/b0fc64b1-5b5c-4f91-8d8b-d2382463706a" />
  <br>
  <b>Figure 8.1: Performance Benchmark Comparison by Execution Paradigm</b>
</p>

<p>&nbsp;</p>

<p align="center">
<img width="400" height="300" alt="Screenshot 2026-04-25 165820" src="https://github.com/user-attachments/assets/24020ae1-a19a-432a-82fd-b9efebbaa6a7" />
  <br>
  <b>Figure 8.2: Terminal Execution Output showing comparative paradigm benchmarks</b>
</p>

<p>&nbsp;</p>

<p align="center">
<img width="259" height="255" alt="Screenshot 2026-05-01 152238" src="https://github.com/user-attachments/assets/e97a9543-2a5a-4df2-824f-26b968581d31" />
  <br>
  <b>Figure 8.3: Forensic Audit Trail ( `audit_results.txt` )</b>
</p>

<p>&nbsp;</p>

**Paradigm Efficiency:** The Parallel paradigm achieved the fastest execution time (14.29s), effectively utilizing CPU multi-core architecture to outperform the Sequential baseline.

**Concurrent Bottleneck:** The Concurrent (threading) paradigm recorded the longest execution time (63.70s). In this high-speed, local-loopback environment, the overhead of context switching between threads and managing a high volume of near-simultaneous socket requests significantly degraded performance compared to the other models.

**Scalability:** The batch-processing model successfully handled 2 million tasks with a stable memory footprint, preventing system-level "zsh: killed" errors and proving the engine's reliability for large-scale forensic simulations.

<br>

## 9. Discussion 🗪
The experimental results demonstrate that architectural selection is highly context-dependent, particularly in high-volume, local-loopback environments.

While the **Concurrent (threading)** paradigm is industry-standard for I/O-bound tasks in high-latency network environments (such as scanning over WAN), it introduced significant management overhead in this local simulation, resulting in a 63.70s execution time. This overhead is primarily attributed to kernel-level thread contention and context-switching latency when processing 2,000,000 tasks in rapid succession on a single process.

Conversely, the **Parallel (multiprocessing)** paradigm successfully utilized multiple CPU cores to bypass the Global Interpreter Lock (GIL), achieving the most efficient execution time of 14.29s. This confirms that for compute-intensive local audit tasks, distributing logic across separate memory spaces is superior to shared-memory threading.

The **Sequential** paradigm provided a highly stable baseline at 14.81s. Its performance relative to the concurrent model proves that for low-latency tasks, the simplicity of linear iteration can outperform a concurrent architecture burdened by excessive orchestration overhead. Ultimately, this research validates that a robust security auditor must be Adaptive—dynamically selecting the execution paradigm based on the target environment’s latency profile and the available hardware resources.

<br>

## 10. Conclusion 🏁
This project successfully architected a scalable, high-volume auditor capable of processing 2 million audit tasks. By demonstrating the trade-offs between Sequential, Concurrent, and Parallel architectures, this assignment confirms that modern forensic tools must prioritize memory efficiency and architectural flexibility to be effective in high-throughput environments. 

<br>

## 11. User Guide ጸ

### 11.1 Installation Steps

Follow these steps to prepare your Kali Linux environment for the audit engine:

1. **Initialize Project Directory:** Create a dedicated workspace to manage your files.
   ```bash
   mkdir ITT440_Auditor && cd ITT440_Auditor

2. **Environment Setup:** Create a virtual environment to isolate dependencies.
   ```bash
   python3 -m venv venv

3. **Activation:** Activate the environment to ensure the engine runs in the correct configuration.
   ```bash
   source venv/bin/activate

4. **File Preparation:** Create a new file named `auditor.py` in the project directory, paste the source code provided in the "Program" section into this file, and save it. Ensure the directory has write permissions so the script can generate the `audit_results.txt` file during execution.

### 11.2 How to Run

Once your environment is prepared, execute the audit process as follows:

1. **Execution:** Launch the audit engine using the Python interpreter.
   ```bash
   python3 auditor.py

2. **Monitoring:** The engine will display the status of each execution paradigm (Sequential, Concurrent, and Parallel) in the terminal. Please allow the process to finish all three phases before interacting with the system.

3. **Data Verification:** After execution, a file named `audit_results.txt` will appear in your directory. You can inspect the findings using the tail command.
   ```bash
   tail -n 20 audit_results.txt

4. **Deactivation:** Once you have completed your analysis, exit the virtual environment.
   ```bash
   deactivate

<br>

## 12. Demonstration Link \\(*ˊᗜˋ*)/ 
https://youtu.be/Yk1Gv9pi0So
