#string examples

lines = '''
Hey. this is the least lines, 
followed by the leading line, 
amazing, 
follow it up.
'''
print(lines)

#string as arrays
print(lines[1])

#loop through the lines 
for letter in lines:
    print(letter)

#search the lines 
if 'this' in lines:
    print("this is found")

# string is an array in python