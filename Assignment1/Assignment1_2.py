def chkeven(no):
    if no%2==0:
        print("The number entered is even..")
    else:
        print("The number entered is odd...")    



def main():
    print("enter the number to check whether even or odd")
    value = int(input())
    chkeven(value)



if __name__ =="__main__":
    main()
