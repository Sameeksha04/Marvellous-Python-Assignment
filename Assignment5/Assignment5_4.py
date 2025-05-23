def main():


    print("Enter three Number: ")

    no1 = int(input())
    no2 = int(input())
    no3 = int(input())
   

    if no1>no2:
        if no1>no3:
            print(no1,"is largest..")

        else:
            print(no3,"is the largest..")   
    
    elif(no2>no1):
        if(no2>no3):
            print(no2,"is the laegest..")

        else:
            print(no3,"is the largest..")    
        




if __name__ =="__main__":
    main()    