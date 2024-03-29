#Before the zip function

friends = ["Rolf", "ruth", "charlie","Jen"]
last_seen = [1,4,7, 9]

#dictionary of the friends when last seen. 
friends_last_seen = {
    friends[i] : last_seen[i]
    for i in range(len(friends))
}

print(friends_last_seen)

#Same can be achieved using the zip function
last_seen_friends = dict(zip(friends,last_seen))
last_seen_friends_list = list(zip(friends,last_seen))

print(last_seen_friends)
print(last_seen_friends_list)