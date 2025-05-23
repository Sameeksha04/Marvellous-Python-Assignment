
def prime(data):
    for i in range(2,data):
        if data%i == 0:
            return False
    return True    

    
        
def main():
    print("enter number of elements...")
    size=int(input())

    data = list()

    print("enter the values...")
    for i in range(size):
        no=int(input())
        data.append(no)


    print("input data : ",data)

    fdata = list(filter(prime,data))
    print("filter data: ", fdata)   




if __name__ == "__main__":
    main()    