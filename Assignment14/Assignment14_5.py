class BankAccount:
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance

    def deposit(self,new_add):
        self.balance=self.balance+new_add


    def withdraw(self,remove_money):
        self.balance=self.balance-remove_money


    def display(self):
        print("Updated Money: ",self.balance)


obj1=BankAccount(45,"samiksha",5000)

obj1.withdraw(500)
obj1.display()

obj1.deposit(1000)
obj1.display()






        





















