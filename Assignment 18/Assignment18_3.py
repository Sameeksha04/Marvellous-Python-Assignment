import sys
import shutil

if len(sys.argv) != 2:
    print("python script.py <source_file>")
    sys.exit(1)

source_file = sys.argv[1]
destination_file = "demo.txt"

try:
    shutil.copyfile(source_file, destination_file)
    print(f"Contents copied from '{source_file}' to '{destination_file}'.")
except FileNotFoundError:
    print(f"File '{source_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
