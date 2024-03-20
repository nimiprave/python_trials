xGlobalVariable = 100
def sayHello():
    print("Hey there .. How are you doing?")
    print(f"I am the global variable :{ xGlobalVariable }")
#    print(x)    # hositing is not supported in python.
sayHello()


# does python support hoisting -- NO it does not
global x
x = "Global variable"
print(x)
