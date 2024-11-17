fileContent = open('payload.json', 'r').read()
print(fileContent)

# converting the string to a dictionary
dict1 = dict(eval(fileContent))
print(dict1)
print(dict1['name'])    
print(dict1['age'])
print(dict1['isStudent'])