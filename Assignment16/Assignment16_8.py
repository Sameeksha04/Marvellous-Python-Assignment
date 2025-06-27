
def main():

    with open("source.txt","r") as src:

        lines = src.readlines()

    with open("cleaned.txt","w") as destination:
        for line in lines:
            if line.strip() != "":
                destination.write(line)

    print("Blank lines removed and saved to cleaned text..")                



if __name__=="__main__":
    main() 
