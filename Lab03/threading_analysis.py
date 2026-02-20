import threading
import os
import time

def task(name):
    print(f"Task {name} is running in Process ID: {os.getpid()} on Thread: {threading.current_thread().name}")
    time.sleep(2)

threads = []
for i in range(4):
    t = threading.Thread(target=task, args=(f"Thread-{i}",), name=f"Thread-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished.")
