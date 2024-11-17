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


# Tsting the class
tom = Cat('Tom', 3)
jerry = Cat('Jerry', 2)
sam = Cat('Sam', 4)
list_of_cats = [tom, jerry, sam]
previous_cat = None
for cat in list_of_cats:
    print(f'{cat.name} is {cat.age} years old')
    if previous_cat is not None:
        if cat.compare_age(previous_cat) >= 1:
            print(f'{cat.name} is oldest cat')
    previous_cat = cat
