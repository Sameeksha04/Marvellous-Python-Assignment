#see again
file =open("marks.txt","w") 
file.write("Sam 98 \n")
file.write("anuskha 74\n")
file.write("Rohit 72\n")
file.write("Anjali 91\n")
file.write("Vikas 65\n")
file.write("Meena 78\n")
file.close()



print("students who scored more than 75: ")

file = open("marks.txt","r")
for line in file:
    name,marks = line.strip().split()
    if int(marks) > 75:
        print(name,"-",marks)
                
file.close()    


              


