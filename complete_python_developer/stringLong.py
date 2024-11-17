# long_string = '''
# This is a long string
# that goes on for many lines
# WOOW
# O  O
#  {}
# ---

# '''

# print(long_string)

#string concatenation
# long_st1 = '''
# This is the long string. I am gg to concatenate this string with another string.
# '''

# long_str2 ='''
# It's quite cold in montreal today. 
# '''

# print( long_st1 + long_str2)


# #str function 
# print(type(str(100)))

# #escape sequence
# weather = '\t It\'s sunny \n hope to have a day!'
# print(weather)



# #formatted string
# first = 'nirmal'
# print(first.capitalize())
# print(first.casefold())

# age = 45
# print(f'hi my name is {first} and I am {age} years old')   

# #place holders
# print('hi {}. You are {} years old'.format('nimi', '45'))

#string indexes
# selfish = 'me me me'
# print(selfish.__len__())
# print(selfish[0])
# print(selfish[0:selfish.__len__()])

# #step over
# print(selfish[0:8:2])

# #step over with default values string[start:stop:stepover]
# something = '0123456789'
# print(something[::-1])


#string immutability
#we cannot reassign the parts of the string. The full string can be reassigned. 
#Therefore, the string variable is a pointer to the memory location of the string.

# first = 'nirmal'
# first = 'shy'  #this is allowed
#first[0] = 'p' #this is not allowed

#Built in functions

#greet = 'hellooo'
#print(greet.__len__())
print(len('hellooo'))   