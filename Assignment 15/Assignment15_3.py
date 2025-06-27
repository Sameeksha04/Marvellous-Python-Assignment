import sys

if len(sys.argv)!=2:
    print("python script.py <source_file>")


file_name = sys.argv[1]

try:
    with open(file_name,'r') as f1:
        data = f1.read()


    with open("demo.txt",'w') as f2:
        f2.write(data) 

    print("File copied to demo.text successfully...")

except FileNotFoundError:
    print("File not found..")           


