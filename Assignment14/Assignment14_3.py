class Book:
    def __init__(self,price):
        self.__price=price

    
    def get_price(self):
        return self.__price
    
    def set_price(self,new_price):
        if new_price>0:
            self.__price=new_price

        else:
            print("price must be positive..")

obj1=Book(250)

print("Initial price: ",obj1.get_price())

obj1.set_price(600)
print("Updated price: ",obj1.get_price())

obj1.set_price(-100)
