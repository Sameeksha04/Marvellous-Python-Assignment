def main():
    print("enter number of elements...")
    size=int(input())

    data = list()

    print("enter the values...")
    for i in range(size):
        no=int(input())
        data.append(no)

    addition=0
    for value in data:
        addition=addition+ value
    print("addition of entered elements are: ",addition)



if __name__=="__main__":
    main()

