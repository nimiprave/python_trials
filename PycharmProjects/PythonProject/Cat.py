class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_cat):
        if self.age > other_cat.age:
            return 1
        elif self.age < other_cat.age:
            return -1
        else:
            return 0





tom = Cat("Tom", 3)
jerry = Cat("Jerry", 2)
sam = Cat("Sam", 4)
list_of_cats = [tom,jerry,sam]

for cat in list_of_cats:
     print(f'The Name of the Cat is {cat.name} and the age is {cat.age}')





