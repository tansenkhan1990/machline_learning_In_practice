class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,name , age, year):
        self.name = name
        self.age = age
        self.year = year
        super().__init__(name,age)    
    def asd(self):
        print('Name: ',self.name,'age: ',self.age,'year: ',self.year)
    def GetPersonProperties(self):
        self.printname()

objectChild = Student("Mike", "Olsen", 2019)
print(objectChild.asd())
# objectPerson = Person('Tansen',"Bondhon")
# objectChild.GetPersonProperties()

