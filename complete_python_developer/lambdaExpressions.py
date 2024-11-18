from functools import reduce


def add_func(x, y): return x + y


print(add_func(2, 3))


# lambda function used in the higher order functions like map, reduce , filter

# map
square_values = map(lambda x: x*x, [1, 2, 3, 4, 5])
for item in square_values:
    print(item)


# filter
even_values = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for item in even_values:
    print(item)


# reduce
total_sum = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5])
print(f'The total value: {total_sum}')


# list sorting using lambda
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
print(a)
a.sort()
print(a)
# sorting based on the key as second values in the tuple
a.sort(key=lambda x: x[1])
print(a)
