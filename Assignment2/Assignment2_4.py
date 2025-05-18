def main():
    print("Enter the number: ")
    size = int(input())
    add=0
    for i in range(1,size+1):
        if (size%i==0):
            add =i+add
    print("sum :",add)       




if __name__ =="__main__":
    main()    


    