#global variables
x = 20
def display():
    x = 40
    print(x)

print(x)
display()

#creating global variable inside a function

x = 100

def show():
    x = 50
    print(x)
    global y 
    y = 200

print(x)
show()
print(y)