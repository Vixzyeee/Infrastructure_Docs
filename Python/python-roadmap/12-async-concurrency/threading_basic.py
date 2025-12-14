# threading_basic.py
# Basic threading example

import threading
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(1)
    print(f"Worker {name} finished")

threads = []

for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed")
