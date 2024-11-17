# wallrus operator - came with the python  3.8.2 insstallation
# walrus operator is a new feature in python 3.8.2
# The walrus operator is a new feature in Python 3.8.2. It is represented by := and is known as the assignment expression operator. It is used to assign values to variables as part of an expression. The walrus operator is useful when you want to assign a value to a variable and use that value in an expression at the same time.


# example

# hello = 'helloooooooooo'
# if(len(hello)>10):
#     print(f'too long {len(hello)} elements')


# the example above can be use to use the len function multiple times

hello = 'helloooooooooo'
if ((n := len(hello)) > 10):
    print(f'too long {n} elements')


def display():
    print('hello')
