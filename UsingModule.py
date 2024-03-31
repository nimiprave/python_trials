import mymodule as mx  #mx is an alias for the imported module
import platform
from mymodule import person1

mx.greetings("Nirmal")
print(mx.person1)


print(platform.system())
print(platform.machine())
print(dir(platform))
print(person1)