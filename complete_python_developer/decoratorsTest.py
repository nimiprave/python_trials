# CLASS METHOS EXAMPLE
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        print(f'Fullname: {self.first}{self.last}')

    def salary(self):
        print(f'Salaray: {self.pay}')

    def increasePay(self, percent):
        self.pay = int(self.pay + (self.pay * percent / 100))
        print(f'New salary: {self.pay}')

    @classmethod
    def simulate_pay(cls, pay, percent):
        return int(pay + (pay * percent / 100))


# simulate pay
print(f'The Simulatedpay increase for thousand dollors is: {
      Employee.simulate_pay(1000, 10)}')
