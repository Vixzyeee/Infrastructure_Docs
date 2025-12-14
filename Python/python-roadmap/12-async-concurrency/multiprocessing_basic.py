# multiprocessing_basic.py
# Basic multiprocessing example

import multiprocessing
import time

def worker(name):
    print(f"Process {name} starting")
    time.sleep(1)
    print(f"Process {name} finished")

if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed")
