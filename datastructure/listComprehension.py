# list comprehension example

list = [1, 2, 3]
multiplying_factor = 3
print(list)
new_list = [multiplying_factor * item for item in list]
print(new_list)


# condition with list comprehensions.
odd_list = [
    f"Factor: {multiplying_factor * item}" for item in list if item % 2 == 0]
print(odd_list)


# expresion

ordered_list = [(x, y) for x in range(3) for y in range(3)]
print(ordered_list)

# using expression to create a list of dictionary list
names = ['nimi', 'suji', 'vaichu']
grades = [90, 98, 99]

grades_dic = [{"name": name} for name in names]
print(grades_dic)

# index and item to form the dictionary.

# gradesdic = [{"name": name, "scores": score} for index, name in enumerate(names) grades[index]]

gradesdic_list = []
for index, name in enumerate(names):
    gradesdic_list.append({"name:": name, "score": grades[index]})

print(gradesdic_list)
