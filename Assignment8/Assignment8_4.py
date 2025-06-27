import threading


capital_count = 0
small_count = 0
digit_count = 0

# Lock for thread-safe updates
lock = threading.Lock()

def capital(strings):
    global capital_count
    for char in strings:
        if char.isupper():
            with lock:
                capital_count =capital_count+ 1

def small(strings):
    global small_count
    for char in strings:
        if char.islower():
            with lock:
                small_count =small_count+ 1

def digits(strings):
    global digit_count
    for char in strings:
        if char.isdigit():
            with lock:
                digit_count =digit_count+ 1

def main():
    global capital_count, small_count, digit_count

    print("Enter an alphanumeric string:")
    strings = input()

    
    t1 = threading.Thread(target=capital, args=(strings,))
    t2 = threading.Thread(target=small, args=(strings,))
    t3 = threading.Thread(target=digits, args=(strings,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Number of capital letters:", capital_count)
    print("Number of small letters:", small_count)
    print("Number of digits:", digit_count)

if __name__ == "__main__":
    main()
