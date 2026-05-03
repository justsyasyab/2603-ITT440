from generator import generate_orders
from analyzer import run_sequential, run_concurrent, run_parallel
import matplotlib.pyplot as plt
 
if __name__ == "__main__":
 
    TOTAL_ORDERS = 20000
    CPU_CORES = 8
 
    print("[*] Generating orders...")
    orders = generate_orders(TOTAL_ORDERS)
 
    print("[SEQUENTIAL] Running...")
    seq_results, seq_time = run_sequential(orders)
 
    print("[CONCURRENT] Running threading...")
    con_results, con_time = run_concurrent(orders)
 
    print("[PARALLEL] Running multiprocessing...")
    par_results, par_time = run_parallel(orders, CPU_CORES)
 
    def summarize(results):
        success = sum(1 for r in results if r["status"] == "success")
        failed = len(results) - success
        total_amount = sum(r["amount"] for r in results)
        return success, failed, total_amount
 
    success, failed, total_amount = summarize(par_results)
 
    print("\n==============================================")
    print("     FOOD ORDERING SYSTEM ANALYSIS REPORT")
    print("==============================================")
    print(f"TOTAL ORDERS PROCESSED : {TOTAL_ORDERS}")
    print(f"SUCCESSFUL ORDERS      : {success}")
    print(f"FAILED ORDERS          : {failed}")
    print(f"TOTAL PAYMENT          : RM {total_amount:.2f}")
 
    print("\n==============================================")
    print("        PERFORMANCE COMPARISON")
    print("==============================================")
    print(f"Sequential Time : {seq_time:.2f}s")
    print(f"Concurrent Time : {con_time:.2f}s")
    print(f"Parallel Time   : {par_time:.2f}s")
 
    speedup = seq_time / par_time
    print(f"Speedup Factor  : {speedup:.2f}x Faster")
 
    labels = ['Sequential', 'Concurrent', 'Parallel']
    times = [seq_time, con_time, par_time]
 
    plt.bar(labels, times)
    plt.ylabel("Execution Time (seconds)")
    plt.title("Food Ordering Performance Benchmark")
 
    plt.show()
