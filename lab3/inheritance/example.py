#1
class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()

#2
class Student(Person):
  pass

#3
x = Student("Mike", "Olsen")
x.printname()

#4
class Student(Person):
  def _init_(self, fname, lname):
    Person._init_(self, fname, lname)

#5
class Student(Person):
  def _init_(self, fname, lname):
    super()._init_(fname, lname)
    self.graduationyear = 2019

#6
class Student(Person):
  def _init_(self, fname, lname, year):
    super()._init_(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)

#7
class Student(Person):
  def _init_(self, fname, lname, year):
    super()._init_(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyea)