def fun(n):
    if n>0:
        fun(n-1)
        print(n)
  



def main():

    fun(5)


if __name__=="__main__":
    main()    

