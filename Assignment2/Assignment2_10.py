def main():
    num = int(input("Enter the number: "))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    print("The total sum of digits is:", total)

if __name__ == "__main__":
    main()
