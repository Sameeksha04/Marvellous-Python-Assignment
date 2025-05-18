def chk_divisible(no):
    ans=0
    if (no%5==0):
        return True
    else:
        return False
    



def main():
    print("enter the number...")
    value1=int(input())
    result =chk_divisible(value1)
    if (result==True):
        print("True")
    else:
        print("False")    
    






if __name__== "__main__":
    main()    
