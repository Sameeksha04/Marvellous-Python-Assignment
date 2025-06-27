file_name = input("Enter the file name ")
search_string = input("Enter the string to search ")

try:
    with open(file_name, 'r') as file:
        content = file.read()

    frequency = content.count(search_string)

    print(f"The string '{search_string}' occurs {frequency} time(s) in '{file_name}'.")

except FileNotFoundError:
    print("File  not found.")
except Exception as e:
    print(f" An error occurred: {e}")
