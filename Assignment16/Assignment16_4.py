
def main():
    with open("numbers.txt","w") as file:
        print("Enter 10 number..")


        for i in range(10):
            num = input(f"enter number {i+1}:")
            file.write(num+"\n")

    
    print("All numbers have been written to numbers.txt") 
   
    

if __name__=="__main__":
    main()    