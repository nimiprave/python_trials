friends = ["Nirmal","Dimal","kamal","Cimal","Vimal"]


#Converting the friends to lower text
friends_converted = [ names.lower() for names in friends]
print(friends_converted)

#Printed the greetings for all the friends
print([f"Hello {name}, How is your day" for name in friends])

#longer version of the transpose
converted_friends = []
for friend in friends:
   converted_friends.append(friend.lower())

print(converted_friends)  