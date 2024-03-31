import mymodule as mx  #mx is an alias for the imported module
import platform
from mymodule import person1
import datetime as dt

# mx.greetings("Nirmal")
# print(mx.person1)


# print(platform.system())
# print(platform.machine())
# print(dir(platform))
# print(person1)


#date time operations
print(dt.datetime.now())

x = dt.datetime(2022,1,1)
print(dt.datetime(2022,1,1))
print(x.strftime("%A"))