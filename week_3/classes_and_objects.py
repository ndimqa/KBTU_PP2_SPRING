class Person:
  def __init__(self, name = "NONE", age = 0):
    self.name = name
    self.age = age

p1 = Person(input('enter name '), input('enter age '))
print(p1.name)
print(p1.age)