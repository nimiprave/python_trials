class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printMyself(self):
        print(f"{self.fname} {self.lname}")



#Inheriting from the Person
class Student(Person):
    def __init__(self,fname,lname,school):
        Person.__init__(self,fname,lname)  
        self.school = school              

    def printMyself(self):
        super().printMyself()
        print(f"School is {self.school}")    



jimmy = Student("Jimmy","Falcon","JDLM")      
jimmy.printMyself()