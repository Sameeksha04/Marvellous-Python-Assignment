def fun(n):
    if n == 0:
        return
    fun(n - 1)        
    print("* " * n)      

def main():
    fun(4)

if __name__ == "__main__":
    main()
