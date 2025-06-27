import os

def main():
    File_Name = input("enter file name: ")


    if os.path.isfile(File_Name):
        print("file exits in current directory..")

    else:
        print("File dose not exits in current directory..")    

if __name__=="__main__":
    main()



