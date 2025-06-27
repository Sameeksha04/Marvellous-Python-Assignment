
def main():
    File_Name = input("Enter the file name: ")

    try:
        with open(File_Name ,'r') as file:
            print("\n lines with more then 5 words..\n")
            for line in file:
                words= line.strip().split()
                if len(words)>5:
                    print(line.strip())

    except FileNotFoundError:
        print("file not found...")

    except Exception as e:
        print(f"an error occured : {e}")
                            
   
    

if __name__=="__main__":
    main()    