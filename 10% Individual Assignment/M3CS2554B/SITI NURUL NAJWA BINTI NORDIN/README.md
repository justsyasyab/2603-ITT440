# 📈 CUSTOMER FEEDBACK ANALYZER
NAME: SITI NURUL NAJWA BINTI NORDIN <br>
STUDENT ID: 2024423364 <br>
YOUTUBE LINK: https://youtu.be/lbxqbhHVkCk
# USER MANUAL & TECHNICAL DOCUMENTATION
Welcome to the Customer Feedback Analyzer. This tool is designed to process large-scale customer feedback data and provides a performance benchmarking suite to analyze how different Python concurrency models (Sequential, Threading, and Multiprocessing) handle CPU-bound workloads.
# SYSTEM REQUIREMENTS
* **Python Version:** 3.8 or higher
* **Operating System:** Windows, macOS, or Linux
* **Dependencies:**
    * **tkinter** (Standard Python library)
    * **matplotlib** (For data visualization)
    * **multiprocessing** (Standard library)
    * **threading** (Standard library)
# 📥 Installation Steps
1. **Clone or Download:** git clone https://github.com/kiddygo1up/gui_analyzer.git <br> _cd gui_analyzer_
2. **Install Dependencies:** Ensure matpotlib is installed in your environment <br> _pip install matpotlib_ <br>
# 🚀 How to Run 
Once installed, execute the script from your terminal: _python main.py_ <br> 
# 📖 User Manual
The application is divided into three distinct stages: <br> <br>
**Step 1: Data Management**
* **Generate Test Data:** Creates 1,000 synthetic feedback entries across three categories (Short, Detailed, Enterprise). <br> This is recommended for first-time users.
* **Browse for File:** Import your own .txt file. Each line in the file will be treated as an individual feedback entry.
* **Dropdown Selection:** Switch between data categories to observe how analysis time scales with text length. <br> <br>
**Step 2: Benchmarking**
* **Sequential (Baseline):** Runs the analysis on the main thread. Best for verifying accuracy before scaling.
* **Threading (GIL-Limited):** Attempts parallel execution. Note: You will likely observe slower performance than Sequential due to the Global Interpreter Lock (GIL).
* **Multiprocessing (True Parallel):** The performance mode. It spawns independent processes for every CPU core. This will be the fastest method for large datasets. <br> <br>
**Step 3: Export**
* **Export to CSV:** Save the calculated "Analysis Scores" and a snippet of the feedback to a CSV file for your reporting needs. <br> 
# 📝 Sample Input & Output 
**Input**  <br>
1. The application expects a .txt file where each line is a single feedback string. <br>
2. User are expected to run the "Generate Test Data" option. <br> <br>
**Output** <br>
<img width="1920" height="1080" alt="Screenshot 2026-05-03 084826" src="https://github.com/user-attachments/assets/19a3650e-531e-4b0e-a671-99c820203e0e" />  <br>
# 🖼️ Screenshots
Below is the representation of UI for feedback analyzer: 
<img width="1920" height="1080" alt="Screenshot 2026-05-03 084700" src="https://github.com/user-attachments/assets/b1236c16-2bf3-4101-864a-d61bdb0e635b" /> <br>
# 🏁 Conclusion
* **Multiprocessing** offers the highest potential for performance in large-scale data pipelines by enabling true parallel execution across multiple CPU cores; however, it involves a startup "overhead cost" that is only justified when the workload is sufficiently large. <br>
* **Sequential** execution serves as the most efficient approach for smaller datasets, as it avoids the administrative burden of inter-process communication and task distribution, outperforming parallel methods when the workload is light. <br>
* **Threading** performs poorly for CPU-bound tasks in this project due to Python’s Global Interpreter Lock (GIL), which restricts execution to a single core and prevents true parallelism. <br> <br>
The performance results demonstrate that choosing an execution model requires balancing task complexity against system overhead. While multiprocessing is the superior architecture for scaling to heavy, enterprise-level workloads, this project highlights that for smaller data volumes, the overhead of parallelization can exceed its benefits.
