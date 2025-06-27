File_name = input("enter the file name: ")
search_string = input("enter the string to search: ")

try:
    with open(File_name,'r') as file:
        content = file.read()

    frequency = content.count(search_string)
    print(f"string {search_string} appears {frequency} times in the file..")


except FileNotFoundError:
    print("not found")

except Exception as e:
    print(f"An error occured: {e}")    



