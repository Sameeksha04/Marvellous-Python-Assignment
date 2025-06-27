
def main():


    try:
        with open("data.txt","r") as file:
            content = file.read()
            print("Contents of file data.txt..")
            print(content)
   
    except FileNotFoundError:
        print("File does not exists..")

    except Exception as e:
        print(f"An error occured is {e}")    
 


if __name__=="__main__":
    main()    