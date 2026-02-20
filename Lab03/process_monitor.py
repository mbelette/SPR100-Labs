import psutil
import time

def monitor_processes():
    print(f"{'PID':<10} {'Name':<25} {'CPU %':<10} {'Memory %':<10}")
    print("-" * 55)
    
    # Get processes and sort by CPU usage
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    
    # Sort by CPU usage and show top 10
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:10]
    
    for proc in processes:
        print(f"{proc['pid']:<10} {proc['name']:<25} {proc['cpu_percent']:<10} {proc['memory_percent']:<10.2f}")

if __name__ == "__main__":
    try:
        while True:
            print("\033c", end="") # Clear terminal screen
            monitor_processes()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
