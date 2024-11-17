# datastructure: dictionary
# dictionary is a collection of key-value pairs
# dictionary is mutable and unordered
# dictionary is enclosed in curly braces {} and each pair is separated by comma 
# dictionary is indexed by key
# dictionary keys are unique

dict1 = {'name':'John', 'age':25, 'city':'New York'}
print(dict1)
print(dict1.get('name'))
print(dict1.items())
print(len(dict1))

if 'name' in dict1.keys():
    print('Name is available')
if 'John' in dict1.values():
    print('John is available')
