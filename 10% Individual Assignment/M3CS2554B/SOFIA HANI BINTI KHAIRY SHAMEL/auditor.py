import socket, time, multiprocessing
from concurrent.futures import ThreadPoolExecutor

# --- CORE LOGIC ---
def get_risk_assessment(port):
    score = (port * 7 + 80) % 100
    risk = "CRITICAL" if score > 70 else ("MEDIUM" if score > 40 else "LOW")
    return {"score": score, "risk": risk}

def check_port(data):
    target, port = data
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        if s.connect_ex((target, port)) == 0:
            s.close()
            return (target, port)
        s.close()
        return None
    except: return None

def run_full_report():
    targets = ["127.0.0.1", "10.0.2.15", "google.com", "microsoft.com"]
    ports = range(1, 201)
    tasks = [(t, p) for t in targets for p in ports]
    
    print(f"\n{'='*80}\n{'FULL FORENSIC DISCOVERY REPORT & RISK ASSESSMENT':^80}\n{'='*80}")

    def execute_mode(mode_name, method):
        print(f"\n>> EXECUTING: {mode_name}")
        start = time.time()
        
        results = []
        if method == "sequential":
            for task in tasks:
                res = check_port(task)
                if res: results.append(res)
        elif method == "concurrent":
            with ThreadPoolExecutor(max_workers=50) as exe:
                results = [r for r in exe.map(check_port, tasks) if r]
        elif method == "parallel":
            with multiprocessing.Pool() as pool:
                results = [r for r in pool.map(check_port, tasks) if r]
                
        # Display findings
        for target, port in results:
            risk = get_risk_assessment(port)
            print(f"   [+] {target:<15} | Port {port:<3} | {risk['risk']:<8} (Score: {risk['score']})")
                
        duration = time.time() - start
        print(f"   [!] COMPLETE. {len(tasks)} TASKS/PORTS PROCESSED.")
        return duration

    t_seq = execute_mode("SEQUENTIAL DISCOVERY", "sequential")
    t_con = execute_mode("CONCURRENT DISCOVERY", "concurrent")
    t_par = execute_mode("PARALLEL DISCOVERY", "parallel")

    print(f"\n{'='*80}\n{'FINAL PERFORMANCE BENCHMARK':^80}\n{'='*80}")
    print(f"{'Strategy':<30} | {'Execution Time':<15}")
    print(f"{'-'*50}")
    print(f"{'Sequential (Discovery)':<30} | {t_seq:>10.4f}s")
    print(f"{'Concurrent (Discovery)':<30} | {t_con:>10.4f}s")
    print(f"{'Parallel (Discovery)':<30} | {t_par:>10.4f}s")
    print(f"{'='*80}")

if __name__ == "__main__":
    run_full_report()
