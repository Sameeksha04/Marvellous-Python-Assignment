def main():
    print("enter number of elements...")
    size=int(input())

    data = list()

    print("enter the values...")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("enter the number")
    value1=int(input())
    count=0
    for i in data:
        if value1==i:
            count =count+1
    print("frequency of number is..",count)        



if __name__=="__main__":
    main()

