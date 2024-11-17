def display():
    print("Hello World")
    
def displayMessage(name, emojji):
    print(name,emojji)
    
display()
displayMessage("John", ":)")


#default parameters
def displaySomething(name="Nirmal"):
    print(name)
    
displaySomething()
displaySomething("Suresh")


#function with return values:
# def sum(a,b):
#     return a+b

# def displayTotal(a):
#     print(f'Total is : {a}')

# displayTotal(sum(10,20))    



#docstring-- use to add comments to the function
def docStringex(name):
    '''
    Info: This functoin prints the name
    '''
    print(name)
    
    
print( docStringex.__doc__)
#another method to get the docstring
help(docStringex)


#args and kwargs
def super_fun(*args):
    print(args)
    return sum(args)
  
print(super_fun(1,2,3,4,5,6,7,8,9,10))  


def keyWordArgs(**kwargs):
    for item in kwargs.items():
        print(item)
        print(f'key is {item[0]} , Value is {item[1]}')
    #print(kwargs)
    
keyWordArgs(name="Nirmal", age=25, city="Chennai")
