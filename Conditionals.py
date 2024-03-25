ages = [1,2,3,4,5]
odds= [ age for age in ages if age % 2 == 1]
print(odds)


friends = ["Rolf", "ruth", "charlie","Jen"]
guests = ["Jose","Bob","Rolf", "Charlie","michael"]

#normal approach with out conditions
friends_lower = set([ name.lower() for name in friends])
guests_lower = set([ name.lower() for name in guests])
common_friends = friends_lower.intersection(guests_lower)
print(common_friends)

#same functionality with conditions
present_friends = [
    name.title() for name in friends_lower if name in guests_lower
]
print(present_friends)