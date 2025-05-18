def Add(no1,no2):
    ans=0
    ans =no1 + no2
    return ans


def main():
    print("enter two numbers you want to add...")
    value1=int(input())
    value2= int(input())
    addition = Add(value1,value2)

    print("Addition is : ",addition)



if __name__=="__main__":
    main()    