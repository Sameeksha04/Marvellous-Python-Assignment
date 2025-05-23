from functools import reduce

product = lambda a,b:a*b
        
       
def main():
    print("enter number of elements...")
    size=int(input())

    data = list()

    print("enter the values...")
    for i in range(size):
        no=int(input())
        data.append(no)


    print("input data : ",data)

    rdata = reduce(product,data)
    print("reduce data: ", rdata)   




if __name__ == "__main__":
    main()    