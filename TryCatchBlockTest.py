#Trying the try/except block 
try:
    # x = "Hello world"
    print(x)
except NameError:
    print("Faced Runtime Error")
except:
    print("Any Other kind of error")
finally:
    print("This block is executed after the try except block is called")    



#Raising an exception 
try:    
    x = -1
    if x < 0:
        raise TypeError("The value of x is below zero")    
except TypeError:
       print("Type Error is raised") 
