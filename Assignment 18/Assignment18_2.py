File_Name = input("enter the file name to open file and read it...")

try:
    with open(File_Name,"r") as file:
        content = file.read()
        print("file contents......")
        print("-------------------------------")
        print(content)

except FileNotFoundError:
    print("file not found......")

except Exception as e:
    print(f"erroe occured :{e}")            

    