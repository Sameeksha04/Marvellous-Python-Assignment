import threading  # create thread

def evenfactor(no):
    sum=0
    
    for i in range(1, no+1):
        if i%2==0:
            if no%i == 0:
                sum=sum+i

    print("sum of even number: ",sum)     


def oddfactor(no):
    sum=0
    for i in range(1, no+1):
        if i%2!=0:
            if no%i == 0:
                sum=sum+i


    print("Sum of odd numbers:",sum)            
               

def main():

    number=30

    t1 = threading.Thread(target=evenfactor,args=(number,))
    t2 = threading.Thread(target=oddfactor,args=(number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()



    print("exit from main")
if __name__ == "__main__":
    main()
