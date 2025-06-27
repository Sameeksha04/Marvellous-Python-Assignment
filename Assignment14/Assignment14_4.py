class Student:
    school_name= "APPS"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display(self):
        print("student_name:",self.name)
        print("Student Roll_no: ",self.roll_no)
        print("School name: ",Student.school_name)

    def set_schooloname(self,new_name):
        Student.school_name=new_name
        


obj1=Student("samiksha",28)

obj1.display()

obj1.set_schooloname("Auxilliam")
obj1.display()

        