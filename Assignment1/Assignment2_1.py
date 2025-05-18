import Arithmetic


def main():

    print("enter two numbers : ")
    value1=int(input())
    value2=int(input())

    addition = Arithmetic.add(value1,value2)
    print("Addition is :", addition)

    substraction = Arithmetic.sub(value1,value2)
    print("Subraction is : ",substraction)

    multiplication= Arithmetic.mul(value1,value2)
    print("Multiplication is : ", multiplication)

    division = Arithmetic.div(value1,value2)
    print("Division is : ",division)




if __name__ == "__main__":
    main()


