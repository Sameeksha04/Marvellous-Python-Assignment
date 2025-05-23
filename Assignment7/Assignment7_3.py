def even(data):
    return data %2 ==0
    
              


def main():
    print("enter number of elements...")
    size=int(input())

    data = list()

    print("enter the values...")
    for i in range(size):
        no=int(input())
        data.append(no)


    print("input data : ",data)

    fdata = list(filter(even,data))
    print("map data: ", fdata)   




if __name__ == "__main__":
    main()    