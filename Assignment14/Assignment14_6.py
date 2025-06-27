class Calculator:
    def __init__(self):
        pass
        
    def add(self):
        num1 = float(input("Enter first number for addition: "))
        num2 = float(input("Enter second number for addition: "))
        result=num1+num2
        print("Addition: ",result)


    def sub(self):
        num1 = float(input("Enter first number for substraction: "))
        num2 = float(input("Enter second number for substraction: "))
        result=num1-num2
        print("substraction: ",result)


    def mul(self):
        num1 = float(input("Enter first number for multiplication: "))
        num2 = float(input("Enter second number for multiplication: "))
        result= num1*num2
        print("Multiplication: ",result)



    def division(self):
        num1 = float(input("Enter first number for division: "))
        num2 = float(input("Enter second number for division:" ))
        result=num1/num2
        print("Division: ",result)


obj1= Calculator()

obj1.sub()
obj1.add()
obj1.mul()
obj1.division()