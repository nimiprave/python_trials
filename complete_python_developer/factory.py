
# using the class method to create a factory of the instances of the class
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def showSelf(self):
        print(f'First Name: {self.first} Last Name: {self.last}')

    @classmethod
    def getInstance(cls, first, last):
        return Employee(first, last)

    def run(self):
        print(f'{self}')


# create an instance of Employee
emp1 = Employee.getInstance('John', 'Doe')
emp1.showSelf()
emp2 = Employee.getInstance('Nimi', 'pothuraj')
emp2.showSelf()

emp1.run()
emp2.run()
