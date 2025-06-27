class BankAccount:
    ROI = 10.5  

    def __init__(self, name, ammount):
        self.name = name
        self.ammount = ammount

    def Display(self):
        print("Account name:", self.name)
        print("Account balance:", self.ammount)

    def deposit(self):
        value = int(input("Enter amount to deposit: "))
        self.ammount += value
        print("deposited successfully.")

    def withdraw(self):
        value = int(input("Enter amount to withdraw: "))
        if value > self.ammount:
            print("Insufficient balance.")
        else:
            self.ammount -= value
            print("withdrawn successfully.")

    def calculate_interest(self):
        interest = (self.ammount * BankAccount.ROI) / 100
        print("Interest on current balance is:", interest)

obj1 = BankAccount("HDFC", 5000)
obj1.deposit()
obj1.Display()
obj1.calculate_interest()

print()

obj2 = BankAccount("SBI", 1000)
obj2.withdraw()
obj2.Display()
obj2.calculate_interest()
