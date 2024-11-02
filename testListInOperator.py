import random

# another way of creating the list
"""
l1 = list()
print(l1)
l1.append(232)
l1.append(22)
l1.append(2323)
l1.append(232232)
l1.append(23232322)
print(l1)


if 22 in l1:
    print("found")

for i in l1:
    print(i)
   
"""
"""
l1 = ["a", "b", "c", "e", "f"]


# change a list item.
print(l1[0:2])
print(l1[1:2])
print(l1[2:2])
print(l1[1:5])

"""
# create an list of random number of size 10, remove the odd index

# create a list
list = []
index = 1
while index <= 10:
    list.append(random.randint(1, 100))
    index = index + 1

print(list)

arrIndex = 0
while arrIndex <= 9:
    if arrIndex % 2 == 0:
        del list[arrIndex]
        print(list)
    arrIndex = arrIndex + 1


print(list)
