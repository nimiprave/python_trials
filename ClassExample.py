#Class Definition & Implementation
class Student:
    def __init__(self,new_name,new_marks):
        self.name = new_name
        self.marks = new_marks

    def average(self):
        return sum(self.marks) / len(self.marks)   
    


#Using the Class Object
Student_one = Student("Rolf",[85,96,75,80])
print(Student_one.name)
print(Student_one.average())
print(Student.average(Student_one))




#Creating a class with static properties. 

class Tax:
    rate = 5
    def __init__(self, my_amount):
        self.amount = my_amount

    def taxTobePaid(self):
        return ( self.amount * self.rate ) / 100    
    
    def __str__(self):
        return f"Rate: {self.rate} , Amount: {self.amount}"

print(Tax.rate)    #static access to the Member variable
taxFor10000 = Tax(10000)
print(f"Tax to be paid is {taxFor10000.taxTobePaid()}")
print(taxFor10000)
print(Tax)
