ages = [1,2,3,4,5]
print(ages)
evenage = [ age for age in ages if age % 2 == 0]
print(evenage)


#String manipulations. 
marks = [34,54,65,78,98]
#print(marks[0])
#print(marks[1])

for i in marks:
    print(i)

name = "Nirmal"
for i in name:
    print(i.capitalize())
    print(i.lower())


#functions
def display(name):
    print(name)


display("Nirmal")
display("vaichu")

#everything is a object. 
#object will have data, and some behavior which you can do on that data. These behaviors are implemented using functions. 
#need to call by identifying the object.behavior()

quote = "hard work plus consistency is equal to success"

capitalizedString = quote.capitalize()
print(capitalizedString)
print(quote.upper())



