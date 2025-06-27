# def fun(n):
#     number_str = str(n)
#     count=0
#     if n=='0':
#         return 1
#     else:
#         for i in number_str:
#             if i=='0':
#                 count=count+1
#         return count           

def zero(n):
 
    if n == 0:
        return 1
    

    if n < 10:
        return 0
    
    if (n % 10) == 0:
        count_zero = 1
    else:
        count_zero=0
    return count_zero + zero(n // 10)


def main():
    result = zero(1020300)
   
    print("Number of zeros: ", result)
  

if __name__ == "__main__":
    main()
