# #Read from the command
# print(input("Give me your name: "))

# #string formatting . 
# name = "Nirmal Praveen Pothuraj"
# input = f"My name is {name}"
# print(input)

# # String template
# input = "Hello World! Mr.{name}"
# print(input.format(name=name))


# #List
# input= ["first","Second","Third"]
# print(input[1])
# input.append("Fourth")
# print("Before Reverse")
# print(input)
# print("After Reverse")
# input.reverse( )
# print(input)



#booleans and comparision in Python
# print(bool())
# print(bool(78))

#Playing with the bools & or operator
# verify_input = input("Enter Something:") 
# static_input = "Nirmal"
# final_input = verify_input or static_input
# print(final_input)

#playing with the and operator
# verify_input = input("Enter Something:") 
# static_input = "Nirmal"
# final_input = verify_input and static_input
# print(final_input)


#Tuples 
# first_tuple = ('first','second','third')
# print(first_tuple)
# new_tuple = first_tuple.__add__(('fourth',))
# print(new_tuple)
# print(first_tuple)

#Sets & advanced Sets Operations
first_set = {'red','blue','green'}
second_set = { 'red','yellow','orange'}

print(first_set.difference(second_set))
print(first_set.intersection(second_set))       
