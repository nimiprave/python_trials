# #Iterating through the for loop

# #iterating through the list
# friends_list = ["Nirmal","Vimal","kamal","Suman"]
# for name in friends_list:
#     print(name)


# #iterating through the tuples
# friends_touple = (1,2,3,4,5,6)
# for n in friends_touple:
#     print(n) 

# #mixing list of touples
# mixed_list_tuple = [friends_touple, friends_list]
# for tuple in mixed_list_tuple:
#     for number in tuple:
#         print(number)



#working with dictionaries
friends_dictionary = { "Nirmal" : 22, 
                        "Shyam" : 20,
                       "Vaichu" :  13 
                      }
for name in friends_dictionary:
    print(f"Name : {name} ")
    
for name,age in friends_dictionary.items():
    print(f"Name : {name} and age is {age}")
