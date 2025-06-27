class Numbers:
    def __init__(self):
        print("Enter value: ")
        self.value = int(input())  

    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                sum += i
        return sum == self.value

    def Factors(self):
        print(f"Factors of {self.value}:")
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                sum += i
        return sum


obj = Numbers()

obj.Factors()
print("Sum of factors:", obj.SumFactors())

if obj.ChkPerfect():
    print(f"{obj.value} is a Perfect Number")
else:
    print(f"{obj.value} is not a Perfect Number")

if obj.ChkPrime():
    print(f"{obj.value} is a Prime Number")
else:
    print(f"{obj.value} is not a Prime Number")
