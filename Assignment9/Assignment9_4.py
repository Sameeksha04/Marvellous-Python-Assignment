import time
import threading
import multiprocessing

def sum():
    total = 0
    for i in range(1, 10_000_001):
        total += i
    return total

def run_sum():
    sum()

if __name__ == '__main__':
    print("Comparing execution time for summing numbers from 1 to 10 million:\n")

    start = time.time()
    sum()
    end = time.time()
    print(f"Normal function time:        {end - start:.4f} seconds")

# :.4f = format specifier:

# : =starts format specification.

# .4 = 4 digits after the decimal point.

# f =fixed-point

#threading

    thread = threading.Thread(target=run_sum)
    start = time.time()
    thread.start()
    thread.join()
    end = time.time()
    print(f"Threading execution time:    {end - start:.4f} seconds")

#Multiprocessing execution

    process = multiprocessing.Process(target=run_sum)
    start = time.time()
    process.start()
    process.join()
    end = time.time()
    print(f"Multiprocessing execution time: {end - start:.4f} seconds")
