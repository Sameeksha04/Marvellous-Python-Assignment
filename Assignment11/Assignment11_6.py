def fun(n):
    if n <= 0:
        return 0
    else:
        return n + fun(n - 1)

def main():
    result = fun(5)
    print("sum:", result)

if __name__ == "__main__":
    main()
