import random

random_number = random.randint(1, 100)
print(random_number)

# what is the datatype of the list
l1 = []
l2 = []
index = 10
while index > 0:
    l1.append(random.randint(1, 100))
    l2.append(random.randint(1, 100))
    index = index - 1

print(l1)
print(l2)


# loop through the list of for multiplying the values of the elements of the array

result = []
listIndex = 0
while listIndex <= 9:
    result.append(l1[listIndex] + l2[listIndex])
    listIndex = listIndex + 1

print(result)
