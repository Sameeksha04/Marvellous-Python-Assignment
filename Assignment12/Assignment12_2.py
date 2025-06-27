class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def accept(self):
        self.radius = float(input("Enter radius: "))

    def calculate_area(self):
        self.area = Circle.PI * self.radius * self.radius

    def calculate_circumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def display(self):
        print("Radius:", self.radius)
        print("Area:", self.area)
        print("Circumference:", self.circumference)

# Create object and use methods
obj1 = Circle()
obj1.accept()
obj1.calculate_area()
obj1.calculate_circumference()
obj1.display()
