
friends = ["Rolf", "ruth", "charlie","Jen"]
guests = ["Jose","Bob","Rolf", "Charlie","michael"]

friends_lower= { name.lower() for name in friends}
guests_lower = { name.lower() for name in guests}
common_friends = [ name.title() for name in friends_lower.intersection(guests_lower)]
print(common_friends)