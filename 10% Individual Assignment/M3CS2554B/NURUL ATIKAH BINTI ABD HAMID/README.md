# NURUL ATIKAH BINTI ABD HAMID
## STUDENT ID:2024428684
## CLASS: M3CS2554B
## WEATHER DATA SIMULATOR
---
## Introduction

This project is a weather data simulation and analysis system developed using Python. The system is focus on Malaysia. The system simulates large-scale weather records for Malaysian state capitals and compares three different programming techniques: sequential programming, concurrent programming using threading, and parallel using multiprocessing.

The purpose of this project is to demonstrate how large data processing can be improved using cuncorrent and parallel programming techniques. The dataset contains simulated weather information such as:
 - Temperature
 - Humidity
 - Wind speed
 - Rainfall

## Problem Statement
Processing large datasets using sequential programming is slow and inefficient. This project demonstrates how concurrency and parallelism can improve executiontime and system performance.

## Objective
- Generate up to 10 million weather records.
- To process weather data using sequential programming.
- To process weather data using concurent programming using threading.
- To process weather data using parallel programming using multiproccesing.
- To compare execution time between the three techniques.
- To generate CSV output, summary report, and performance graph.

## Tools / Libraries
| Tool                 | Description               |
|----------------------|---------------------------|
| Python               | Main programming language |
| Pandas               | Data processing           |
| Matplotlib           | Graph generation          |
| ThreadPoolExecuter   | Concurrent processing     |
| Multiprocessing Pool | Parallel processing       |
| CSV                  | Data storage              |

---

## How It Works

### Data Generation
The system generates weather data including:
 - Temperature
 - Humidity
 - Wind speed
 - Rainfall

### Region Division
The workload is divided into 4 regions:
- Northern
- Southern
- East Coast
- Sabah Sarawak

Each region is processed separately to simulate distributed workload.

### Sequential Processing
Processes one region at a time (slowest) because it does not utilize concurrency or parallelism.

### Threading
Threading uses 'ThreadPoolExecuter' to runs multiple regions concurrently.

### Multiprocessing 
Uses 4 CPU cores to process regions in parallel (fastest).

---

## System Features

- Menu-driven application
- Large-scale data simulation (10 million records)
- Sequential vs Threading vs Multiprocessing comparison
- CSV file generation
- Performance graph visualization

---

## Installation

```
python -m pip install pandas numpy matplotlib
```

---

## Source Code

The full source code can be found in:
- main.py

---

## Sample Output

The system generates:
- weather_data/malaysia_weather_data.csv
- output/result_summary.txt
- output/performance_graph.png

---

## Performance Result

Expected result:
Sequential      - Slowest
Threading       - Faster
Multiprocessing - Fatest

Multiprocessing is the fastest because it utilizes multiple CPU cores to process data in parallel.

---

## Output

Menu-driven 
<img width="639" height="341" alt="image" src="https://github.com/user-attachments/assets/ee157729-7f9d-4872-aabb-0c038c56c29e" />

Processing Output
<img width="862" height="860" alt="image" src="https://github.com/user-attachments/assets/0a3b5233-847e-4118-bb12-e8d262f975b4" />

Sample data (malaysia_weather_data.csv)
<img width="571" height="697" alt="image" src="https://github.com/user-attachments/assets/b0b4fd1e-86d2-4e7b-b013-3c528edc28e0" />


Performance Graph
<img width="900" height="600" alt="performance_graph" src="https://github.com/user-attachments/assets/bf4cf324-d415-439e-988c-7ccde38985a4" />

---

## Demo Video

Youtube Link: https://youtu.be/mCGPTyW7O7M?si=rVDwcvbT00qlhna3

---

## Conclusion

This project demonstrates how parallel programming technique can significantly improve the performance of large-scale data processing. Sequential programming is simple but inefficient for large datasets. Threading improves concurrency, while multiprocessing provides the best performance by utilizing multiple CPU cores.

  This system shows that dividing workload across multiple processes is an effective solution for handling big data.




