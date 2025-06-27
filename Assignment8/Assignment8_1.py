import threading  # create thread

def even():
    print("Even numbers:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)

def odd():
    print("Odd numbers:")
    for i in range(1, 11):
        if i % 2 != 0:
            print(i)

def main():
    
    t1 = threading.Thread(target=even)
    t2 = threading.Thread(target=odd)

    # Start thread
    t1.start()
    t2.start()

    # Waiting for both threads to finish
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
