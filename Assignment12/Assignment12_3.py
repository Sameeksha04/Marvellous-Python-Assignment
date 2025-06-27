class Arithmetic:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def Accept(self):
        print("Enter the value 1 and value 2 : ")
        self.value1 = int(input())
        self.value2 = int(input())
        

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self): 
        return self.value1 - self.value2  

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self): 
        if self.value2 != 0:
            return self.value1 / self.value2
        else:
            return "Division not possible"


obj1 = Arithmetic(5, 7)
obj2 = Arithmetic(7, 3)
obj3 = Arithmetic(6, 2)
obj4 = Arithmetic(3, 1)


print("Addition:", obj1.Addition())
print("Multiplication:", obj2.Multiplication())
print("Division:", obj3.Division())
print("Subtraction:", obj4.Subtraction())
