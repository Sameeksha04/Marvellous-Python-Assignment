
def main():

    with open("student.txt","w") as file:
        students = ["Aniket\n","samiksha\n","prerna\n","raj\n","Tejas\n"]

        file.writelines(students)



    print("Student.txt has been created with 5 students names...")    

if __name__=="__main__":
    main()    