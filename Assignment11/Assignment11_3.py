def fun(n):
    sum=0
    if n==0:
        return 0
    elif n<0:
        n=-n

    else:
       return ((n%10) + fun(n//10))    

    

def main():
    result = fun(1294)
   
    print("sum of digits: ", result)
  

if __name__ == "__main__":
    main()
