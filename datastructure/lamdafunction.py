# lamba functions for creating anonymous functions.
# lamda arguments : expression
# lambda functions can have only one line expression.
# used for creation function objects which can be used as arguments to another function or method.


# Anonymous function
ss = (lambda x: x * x)(10)
print(ss)

###


def display(x): return f" The value is {x}"


print(display("som"))


# Example of using the lambda function for sort, filter and reduce function of the list object
l = ["1", "2", "9", "0", "-1", "-2"]

# sorting function
print(sorted(l, key=lambda x: int(x)))

# filter function
print(list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

# map reduce
print(list(map(lambda x: str(int(x) + 10), l)))
