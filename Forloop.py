# friends = ["Rolf", "Bob", "Anne"]
# for friend in friends:
#     print(friend)

# #using ranges   
# for index in range(10):
#     print(index) 

# #using ranges options
# for index in range(2,30,5):
#     print(index) 
        

#destrucing --example
# students = [ ("Nimi",30),("Kimi",31),("Dimi",32)]        
# for name, age in students:
#     print(f"Name is {name} and age is {age}")


#Iterating over dictionaries
# friend_ages = { "Rolf" : 25, "Charlie" : 27, "Bob" : 41}    
# for friend in friend_ages:
#     print(friend)   #prints the keys of the dictionaries

# #Reading the values of the dictionaries
# for age in friend_ages.values():
#     print(age)

# #Reading both the keys and values
# for name,age in friend_ages.items():
#     print(f"Name is {name} and age is {age}")    



#break and continue
cars = ["ok","ok","ok","ok","ok","ok","ok"]
for status in cars:
    if status == "faulty":
        break
    print(f"This car is {status}")
    print("Shipping new car to customer! ")
else:
    print("All cars built successfully . No faulty cars!")



