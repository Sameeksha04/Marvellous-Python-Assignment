from MarvellousNum import chkPrime

def main():
    print("enter number of elements...")
    size=int(input())

    data = list()

    print("enter the values...")
    for i in range(size):
        no=int(input())
        data.append(no)
     

    prime= chkPrime(data) 
     



if __name__=="__main__":
    main()

