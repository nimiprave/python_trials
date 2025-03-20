from functools import reduce


# filter function
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = filter(lambda x: x % 2 == 0, a)
l = list(b)
print(type(a))
print(list(b))
print(type(l))

c = list(map(lambda x: x * 5, l))
print(type(c))
print(list(c))
red = reduce(lambda x, y: x + y, c)
print(red)
