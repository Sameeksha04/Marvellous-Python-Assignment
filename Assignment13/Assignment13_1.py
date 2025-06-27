class BookStore:
    NoOfBooks=0
    def __init__(self,name,author):
        self.name=name
        self.author=author
        BookStore.NoOfBooks+=1

          
    def Display(self):
        print("name :",self.name)
        print("name of author:",self.author)
        print("number of books:",BookStore.NoOfBooks)

obj1=BookStore("linux system","robertlove")
obj1.Display()


obj2=BookStore("c programming ","dennis ritchie")

obj2.Display()


                

               