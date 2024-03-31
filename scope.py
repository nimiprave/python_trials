#Global scope and local scope
# x = 300
# def myfunction():
#     x = 200
#     print(x)

# print(x)
# myfunction()


# Global Scope
global x 
def myfunc():
    x = 300
    print(x)
myfunc()
x = 200
myfunc()
print(x)

