
def main():
    File_name = input("Enter the file name:")

    try:
        with open(File_name,'r') as file:
            line = file.readlines()


        line_count = len(line)
        word_count =0
        character_count =0

        for i in line:
            words=line.split()
            word_count=word_count+len(words)
            character_count =character_count+len(i)


        print("Total Lines: ",line_count)
        print("Total words: ",word_count)
        print("Total character: ",character_count)

    except FileNotFoundError:
        print("file not found..")
    except Exception as e:
        print(f"An error occured : {e}")        


    

if __name__=="__main__":
    main()    