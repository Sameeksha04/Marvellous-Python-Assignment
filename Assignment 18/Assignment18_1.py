import os

File_Name = input("Enter the file name...")


if os.path.isfile(File_Name):
    print(f"the file {File_Name} exists in directory.....")

else:
    print(f"the file {File_Name} does not exists in directory.....")
