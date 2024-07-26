listAges = [10, 20, 50, 40, 30]
print(listAges)


listAges.sort()
print(listAges)


listAges.insert(len(listAges), 5)
print(listAges)

listAges.reverse()
print(listAges)

listAges.sort()
print(listAges)

print(type(listAges))


## Write a program which can take 10 values from the user and store it in the list and print the list.

# create a loop.
# within a loop I have to call Input function,
# The value of the input function should be added to the List.
# exit the loop
# print the list. .


# while loop  want to loop 10 times.

i = 1
while i < 10:
    print(i)
    i = i + 1


import random

print(random.randrange(1, 100))
