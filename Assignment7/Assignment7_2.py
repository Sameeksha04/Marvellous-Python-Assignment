double = lambda a : 2*a


def main():
    print("enter number of elements...")
    size=int(input())

    data = list()

    print("enter the values...")
    for i in range(size):
        no=int(input())
        data.append(no)


    print("input data : ",data)

    mdata = list(map(double,data))
    print("map data: ", mdata)   




if __name__ == "__main__":
    main()    