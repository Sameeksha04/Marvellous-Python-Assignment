import threading


def evenlist(no):
    sum =0
    for i in no:
        if i%2==0:
            sum=sum+i


    print("Sum of even : ",sum,"\n")        


def oddlist(no):
    sum =0
    for i in no:
        if i%2!=0:
            sum=sum+i


    print("Sum of odd : ",sum)        


def main():
    data=[]
    print("enter number of elements:")
    no= int(input())

    print("Please enter numeric values: ")
    
    for i in range(no):
        value=int(input())
        data.append(value)


    print("Input data: ",data)


    #threads


    t1=threading.Thread(target=evenlist,args=(data,))

    t2=threading.Thread(target=oddlist,args=(data,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__=="__main__":
    main()    