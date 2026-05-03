import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
 
# HYBRID workload (IMPORTANT)
def process_order(order):
    time.sleep(0.0003)  # simulate I/O delay
 
    total = 0
    for _ in range(1000):  # small CPU work
        total += order["price"] * 1.06
 
    return {
        "status": order["status"],
        "amount": total
    }
 
# SEQUENTIAL
def run_sequential(orders):
    start = time.time()
    results = [process_order(o) for o in orders]
    end = time.time()
    return results, end - start
 
# CONCURRENT
def run_concurrent(orders):
    start = time.time()
 
    with ThreadPoolExecutor(max_workers=6) as executor:
        results = list(executor.map(process_order, orders))
 
    end = time.time()
    return results, end - start
 
# PARALLEL
def run_parallel(orders, cores=8):
    start = time.time()
 
    with Pool(processes=cores) as pool:
        results = pool.map(process_order, orders, chunksize=500)
 
    end = time.time()
    return results, end - start
