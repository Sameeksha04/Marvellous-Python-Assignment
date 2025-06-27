class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width


    def area(self):
        result=self.length*self.width
        return result

    def perimeter(self):
        result=2*self.length+2*self.width
        return result



obj1=Rectangle(50,30)


print("Area: ",obj1.area())
print("Perimeter: ",obj1.perimeter())

    

        