# Online Order Processing System

# Introduction
This project focuses on demostrating the concept of parallel programming using an online order processing system. In real-world applications, systems often need to handle multiple tasks simultaneously to improve efficiency. Therefore, this project compares sequential and parallel processing methods to analyze their performance in handling multiple orders.

# Problem Statement
Modern systems often need to handle a large number of tasks efficiently. When tasks are process sequentially, the system becomes slower and less efficient, especially under heavy workload. This creates delays and reduces overall performance. Therefore, there is a need to implement parallel processing techniques such as threading and multiprocessing to improve efficiency and reduce execution time.

# Objective
- To implement sequential processing in handling orders.
- To implement parallel processing using threading.
- To implement parallel processing using multiprocessing.
- To compare execution time between all approaches.
- To track total processes (payment, packaging, delivery)

# Methodology
The system simulates a number of customer orders. Each order goes through three main process:
- Payment 💳
- Packaging 📦
- Delivery 🚚

Three approaches are used :
- **Sequential Processing** : Each order is processed one by one. Each order must complete before the next begins.
- **Parallel Processing (Threading)** : Multiple orders are processed at the same time using threads. Each thread handles one order.
- **Parallel Processing (Multiprocessing)** : Multiple processes are created, where each process handles one order independently. This allows better CPU utilization.

# 💻 Code
```python 
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor


# =========================
# PROCESS FUNCTION
# =========================
def process_order(order_id):

    return (1, 1, 1)


# =========================
# SEQUENTIAL
# =========================
def sequential_orders(orders):
    start = time.time()

    payment = packaging = delivery = 0

    for order in orders:
        p, pack, d = process_order(order)
        payment += p
        packaging += pack
        delivery += d

    end = time.time()

    print("\n--- SEQUENTIAL ---")
    print("Time:", round(end - start, 4), "seconds")
    print("Payment:", payment)
    print("Packaging:", packaging)
    print("Delivery:", delivery)


# =========================
# THREADING (CONCURRENT)
# =========================
def threading_orders(orders):
    start = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_order, orders))

    payment = sum(r[0] for r in results)
    packaging = sum(r[1] for r in results)
    delivery = sum(r[2] for r in results)

    end = time.time()

    print("\n--- THREADING ---")
    print("Time:", round(end - start, 4), "seconds")
    print("Payment:", payment)
    print("Packaging:", packaging)
    print("Delivery:", delivery)


# =========================
# MULTIPROCESSING (PARALLEL)
# =========================
def multiprocessing_orders(orders):
    start = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(process_order, orders, chunksize=100)

    payment = sum(r[0] for r in results)
    packaging = sum(r[1] for r in results)
    delivery = sum(r[2] for r in results)

    end = time.time()

    print("\n--- MULTIPROCESSING ---")
    print("Time:", round(end - start, 4), "seconds")
    print("Payment:", payment)
    print("Packaging:", packaging)
    print("Delivery:", delivery)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    orders = list(range(1, 2500001))  

    print("Processing", len(orders), "orders")

    sequential_orders(orders)
    threading_orders(orders)
    multiprocessing_orders(orders)    
```
# 💻 Code Explanation
- **process_order(order_id)** : This function simulates an order process (payment, packaging, delivery) using time.sleep(1) to represent processing time.
- **sequential_orders(orders)** : Process orders one by one using a loop. It records the total execution time, which is slower because tasks are done sequentially.
- **threading_orders(orders)** : Use threading to process multiple orders at the same time. Each order runs in a separate thread and making the process faster.
- **multiprocessing_orders(orders)** : Use multiprocessing to run separate process, improving performance.
- **multiprocessing.Pool()** : Distributes tasks across multiple processes.
- **time.time()** : Use to measure execution time for comparison.

# Results & Output
| Method | Execution Time | Payment | Packaging | Delivery |
|----------|----------|----------|----------|----------|
| Sequential   |  1.7081 seconds  | 2 500 000 | 2 500 000 | 2 500 000 |
| Threading (Concurrent) | 317.3484 seconds  | 2 500 000 | 2 500 000 | 2 500 000 |
| Multiprocessing (Parallel) |  6.9126 seconds | 2 500 000 | 2 500 000 | 2 500 000 |

- Sequential Processing :
<img width="378" height="185" alt="image" src="https://github.com/user-attachments/assets/cb8c7933-56f4-4f07-8284-27f0bd66dac1" />


- Threading :
<img width="358" height="142" alt="image" src="https://github.com/user-attachments/assets/4fb8416c-0c63-4f7c-a25e-30c21245ac76" />


- Multiprocessing :
<img width="330" height="127" alt="image" src="https://github.com/user-attachments/assets/6cd29f20-4c7a-42f0-b59a-bff90616005b" />


# Conclusion
Sequential processing performed faster than threading and multiprocessing because the task is simple, causing the overhead of parallel processing to reduce performance. Threading is limited by the Global Interpreter Lock (GIL), when multiprocessing introduces additional overhead from process management. This shows that parallel processing does not always guarantee better performance, especially for simple tasks, and the choice of method depends on the workload.


