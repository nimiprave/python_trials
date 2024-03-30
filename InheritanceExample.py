#Example of Inheritence 

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname, self.lname)



nirmal = Person("Nirmal", "pothuraj")    
nirmal.printname()  

#inheriting from a Parent Class, #pass is a keyword to mention that there is no more declaration
class Student(Person):
    def nickName(self):
        print(f"{self.fname[0:len(self.fname)-2]}")

vaich = Student("Vaishvik","Pothuraj")
vaich.printname()
vaich.nickName()


