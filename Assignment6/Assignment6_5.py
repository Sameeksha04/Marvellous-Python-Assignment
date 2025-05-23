def main():
    print("enter a number: ")
    no = int(input())
    
    for i in range(2,no):
        if no%i==0:
            print("not Prime")
            return

    
    print("it is prime ")   




if __name__ == "__main__":
    main()    