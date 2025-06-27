import multiprocessing
import math

def factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")

if __name__ == '__main__':
    numbers = [5, 7, 10, 12, 15]

    processes = []

    for num in numbers:
        process = multiprocessing.Process(target=factorial, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
