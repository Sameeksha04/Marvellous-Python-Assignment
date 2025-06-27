import threading
import time

def thread1():
    for i in range(1,6,1):
        print(i)



def thread2():
    for i in range(1,6,1):
        print(i)


def thread3():
    for i in range(1,6,1):
        print(i)



def main():
    t1=threading.Thread(target=thread1)
    t2=threading.Thread(target=thread2)
    t3=threading.Thread(target=thread3)


    t1.start()
    t1.join()
    time.sleep(1)

    t2.start()
    t2.join()
    time.sleep(1)

    t3.start()
    t3.join()




    



if __name__=="__main__":
    main()        

