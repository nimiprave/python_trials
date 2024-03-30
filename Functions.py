xGlobalVariable = 100
def sayHello():
    print("Hey there .. How are you doing?")
    print(f"I am the global variable :{ xGlobalVariable }")
#    print(x)    # hositing is not supported in python.
sayHello()


#does python support hoisting -- NO it does not
global x
x = "Global variable"
print(x)

#method definition with the arguments, default arguments, named parameters
def addition( x, y):
    return x+y
print(addition(10,4))

def multipicator(x, y=3):
    return x * y
print(multipicator(5))
print(multipicator(6,6))


