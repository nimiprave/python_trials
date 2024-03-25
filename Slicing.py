#List Slicing

friends = ["Nirmal","Dimal","kamal","Cimal","Vimal"]

#Copying the friends list
friends_duplicate = friends[:]
print(friends_duplicate)


#slicing the list
print(friends[1:friends.__sizeof__()])
print(friends[:friends.__sizeof__()])
print(friends[1:5])
print(friends[0:4])


print(friends[-3:])
print(friends[-2:5])
print(friends[:2])