def chkPrime(data):
    prime_number = []

    for num in data:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_number.append(num)

    print("Prime numbers are:", prime_number)
    print("Sum of prime numbers is:", sum(prime_number))

