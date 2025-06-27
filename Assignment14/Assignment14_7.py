class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def display(self):
        print("Name: ",self.name)
        print("age: ",self.age
              )    
        

class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age) 
        self.subject=subject
        self.salary=salary

    def display(self):
        super().display()
        print("subject: ",self.subject)
        print("Salary: ",self.salary)


t1=Teacher("samiksha",23,"Math",5000)
t1.display() 





                  