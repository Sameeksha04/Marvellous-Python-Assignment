def main():
    print("Enter the number: ")
    size = int(input())

    for i in range(size):
        for j in range(size):
            print("*",end=" ")
        size=size-1
        print()    



if __name__ =="__main__":
    main()    