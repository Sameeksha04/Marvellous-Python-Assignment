class Employee:
    def __init__(self, name, department, salary):
        self.name = name                    # Public
        self._department = department       # Protected
        self.__salary = salary              # Private

    def show_info(self):
        print("Name: ", self.name)
        print("Department: ", self._department)
        print("Salary: ", self.__salary)

emp = Employee("Samiksha", "IT", 60000)

print("Public name: ", emp.name)

print("Protected department: ", emp._department)

try:
    print("Private Salary: ", emp.__salary)
except AttributeError:
    print("Accessing Private Salary with name mangling: ", emp._Employee__salary)

emp.show_info()
