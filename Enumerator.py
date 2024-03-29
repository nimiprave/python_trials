#Using the Enumerator Function 

#How to print the index without the enumerator function
friends = ["Rolf", "ruth", "charlie","Jen"]

counter = 0
for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1


#DO the same using the enumerator function 
print(dict(enumerate(friends)))
print(list(enumerate(friends)))
print(set(enumerate(friends, start=1)))

