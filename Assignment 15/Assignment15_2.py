import os

def main():
    File_Name = input("enter file name: ")

    try:
        with open(File_Name,'r') as file:
            content=file.read()
            print("Content of file:")
            print(content)

    except FileNotFoundError:
        print("the file was not found")        


    if __name__=="__main__":
        main()



