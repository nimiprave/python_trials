# using reducing function using the Operator module
import operator
from functools import reduce
from itertools import accumulate

a = [1, 2, 3, 4, 5, 6, 7, 8]

print(reduce(operator.add, a))
print(reduce(operator.sub, a))
print(reduce(operator.mul, a))
print(reduce(operator.add, ["how", "are", "you"]))


# using accumulate using itertools
y = [1, 2, 3, 4, 5, 6, 7, 8]
res = accumulate(y, operator.add)
print(list(res))
