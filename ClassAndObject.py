class Practice :
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def PrintNameAndAge(self):
        print("Name: ",self.name,"age: ",self.age)
object = Practice("Tansen", 31)        
object.PrintNameAndAge()