def fun(n1,n2):
    if n2==0:
        return 1
    return n1*fun(n1,n2-1)
    
      

    

def main():
    result = fun(2,3)
   
    print("power function: ", result)
  

if __name__ == "__main__":
    main()
