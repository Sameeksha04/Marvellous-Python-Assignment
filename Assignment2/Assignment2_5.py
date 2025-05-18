def main():
    print("Enter the number: ")
    size = int(input())

    if size >1 :
        for i in range(2,size):
            if size%i==0:
                print(size,"not a prime number..")
                break
        else:
            print(size,"is a prime number")  

    else:
        print("not a prime")         



if __name__ =="__main__":
    main()    


    