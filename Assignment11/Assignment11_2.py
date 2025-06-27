def fun(n):
    if n == 0:
        return 1
    elif n < 0:
        return False
    else:
        return n * fun(n - 1)

def main():
    result = fun(5)
    if result is not False:
        print("Factorial: ", result)
    else:
        print("No factorial")

if __name__ == "__main__":
    main()
