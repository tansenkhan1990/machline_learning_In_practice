class Parents:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def PrintNameAndAge(self):
        print("Name: ",self.name," age: ",self.age)
class child(Parents):
    pass
object = child("Tansen Khan",31)
object.PrintNameAndAge()