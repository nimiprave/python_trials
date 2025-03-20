# creating the dictionary out of the lists

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

# zip function
myDict = {k: v for (k, v) in zip(keys, values)}
print(myDict)


# dictionary comprehension for making dictionary
square_dic = {x: x*x for x in range(5)}
print(square_dic)


# nested dictionary comprehension
l = "ABC"
for i in l:
    print(i)
nested_dic = {i: {index: value for index, value in enumerate(l)} for i in l}

print(nested_dic)


# nested dictionary comprehension with a duplicate example.
k = "GFG"
nested = {x: {y: x+y for y in k} for x in k}
print(nested)
