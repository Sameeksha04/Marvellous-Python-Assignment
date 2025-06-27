import threading

def thread1():
    for i in range(1, 51):
        print("Thread 1:", i)

def thread2():
    for i in range(50, 0, -1):
        print("Thread 2:", i)

def main():
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t1.join()  

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
