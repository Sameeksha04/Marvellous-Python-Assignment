def main():
    print("enter number of elements...")
    size=int(input())

    data = list()

    print("enter the values...")
    for i in range(size):
        no=int(input())
        data.append(no)

    max_num= data[0]

    for i in data:
        if i>max_num:
            max_num=i
    print("maximum elemnt is :",max_num)



if __name__=="__main__":
    main()

