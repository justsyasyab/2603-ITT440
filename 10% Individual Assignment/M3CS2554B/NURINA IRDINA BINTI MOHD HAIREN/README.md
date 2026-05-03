# ⁶⁹📐𓈒𖹭🔢𓈒»〽⭑🖇๋࣭  PRIME NUMBER FINDER  ⭑⚝📈⊹₊ ⋆📑⚛ྀ

#### STUDENT NAME: NURINA IRDINA BINTI MOHD HAIREN
#### STUDENT ID: 2024239814
#### CLASS: CDCS2554B



## ⋆. 𐙚 ˚ Introduction

This project is a Python-based utility designed to find prime numbers within a specified range. The core objective is to compare three different execution models:

1. Sequential: Standard single-threaded execution.

2. Threading (Concurrent): Splitting the range into chunks handled by different threads.

3. Multiprocessing (Parallel): Distributing the workload across multiple CPU cores.

## ⋆. 𐙚 ˚ Problem Statement

1. The Mathematical Challenge
   
Finding prime numbers is a computationally intensive task. As the range of numbers increases, the 
time required to check each number for primality grows significantly. A standard sequential (one-by-
one) approach becomes inefficient for very large ranges, leading to long execution times.

2. The Technical Bottleneck

Python’s execution is typically single-threaded due to the Global Interpreter Lock (GIL). While this ensures safety, it prevents the program from fully utilizing the power of modern multi-core processors when performing mathematical calculations.

## ⋆. 𐙚 ˚ System Requirements

-Operating System: Windows, macOS, or Linux.

-Python Version: Python 3.7 or higher.

-Hardware: Multi-core processor (recommended to see the benefits of Parallelism).

-Software: Visual Studio Code with the Python Extension installed.

## ⋆. 𐙚 ˚ Installation Steps

1. Install Python: Download and install Python from the official website if you haven't already.

2. Install VS Code Extension: Open VS Code, go to the Extensions view (Ctrl+Shift+X), and install the "Python" extension by Microsoft.

3. Create File: Create a new file in VS Code named prime_finder.py.

4. Paste Code: Copy the provided source code and paste it into this new file.
   
## ⋆. 𐙚 ˚ How to Run

1. Open Terminal: In VS Code, open the integrated terminal by pressing Ctrl+`  (backtick).

2. Execute Script: Type the following command and press Enter:

python prime_finder.py

3. Input Data: Enter the start and end of the range when prompted by the terminal (e.g., 1 to 100,000).

4. View Analysis: The program will execute all three methods sequentially and display a terminal-based bar chart comparing their speeds.

5. Check Output: A file named primes_output.txt will be generated in your VS Code explorer sidebar containing the full list of discovered primes.

 ## ⋆. 𐙚 ˚ Sample Input/Output

 Input:

<img width="770" height="150" alt="Screenshot 2026-04-29 003727" src="https://github.com/user-attachments/assets/5ef099bf-33e6-416f-a984-cd8b64bc2f7c" />

 Output:
 
<img width="1108" height="606" alt="Screenshot 2026-04-29 003740" src="https://github.com/user-attachments/assets/ae09036b-c577-4f04-8e51-627b632a6a2d" />

primes_output.txt:

<img width="1243" height="912" alt="Screenshot 2026-04-29 003804" src="https://github.com/user-attachments/assets/7dc51777-fbfd-4c20-a43b-3852c78d6804" />


## ⋆. 𐙚 ˚ Source code

<img width="989" height="902" alt="Screenshot 2026-04-29 004240" src="https://github.com/user-attachments/assets/fc93cb5b-7148-44a7-8ec2-3346b0feac8e" />

/
<img width="983" height="909" alt="Screenshot 2026-04-29 004305" src="https://github.com/user-attachments/assets/24c2421c-f6d3-49a1-a2ae-643a593e24d0" />

/
<img width="978" height="302" alt="image" src="https://github.com/user-attachments/assets/42b3c8fb-ae8d-4c84-a2ca-85cbdbd7f813" />



## ⋆. 𐙚 ˚ Conclusion

This project successfully demonstrated the practical differences between concurrency and parallelism in Python. By benchmarking three execution models, several key conclusions were reached:

-Sequential Execution: Proved inefficient for large-scale calculations as it utilizes only a single CPU core.

-Threading (Concurrency): Provided minimal performance gains. Due to Python’s Global Interpreter Lock (GIL), threads cannot perform CPU-intensive math simultaneously, making this method better suited for tasks that involve "waiting" (like network requests) rather than "calculating."

-Multiprocessing (Parallelism): This was the most effective approach. By creating separate processes, the program bypassed the GIL and utilized the full power of a multi-core processor, significantly reducing the time required to find primes.

##  🎞️✮⋆˙Video Demonstration:

https://youtu.be/1EEQNmCRh14?feature=shared








 

