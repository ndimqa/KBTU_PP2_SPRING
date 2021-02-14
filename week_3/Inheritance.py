class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def printname(self):
        print(self.name)

class student(person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.gradyear = year

    def welcome(self):
        print("Welcome ", self.name , " to the class of ",self.gradyear)

x = person("qwerty",12)
x1 = student("qaz",12,2019)
x.printname()
x1.welcome()




    