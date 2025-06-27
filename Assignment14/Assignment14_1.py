class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary

    def display(self):
        print("Employe name: ",self.name)
        print("Emp_ID:",self.emp_id)
        print("EMP_Salary: ",self.salary)


obj1=Employee("Rohit",101,50000) 
obj2=Employee("Kiran",98,80000)

obj1.display()
obj2.display()
       
