class Demo:
    value=0

    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2


    def fun(self):
        print("inside fun: ",self.no2)

    def gun(self):
        print("inside gun: ",self.no1)   


obj1=Demo(11,21)
obj2=Demo(51,101)


obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()
        


 