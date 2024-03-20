# #list
# friends = ["nimi","simi","gami"]
# print(friends)
# print(friends[0])
# friends.append("sim")
# print(friends)


# #tuples cannot be added or deleted
# short_tuple = ("Rolf","bob" )
# second_tuple = ("simran")
# print(short_tuple)
# print(second_tuple)
# # new_tuple = short_tuple. + ("simi")
# # print(new_tuple)


#sets - don't contain duplicate elements and don't hold order

art_friends = {"Rolf", "Anne"}
art_friends.add("Jen")
print(art_friends)
#art_friends.remove("Rolf")
#print(art_friends)
science_friends = {"Jen","Charlie"}
print(science_friends)
diff_art_friends = art_friends.difference(science_friends)
print(diff_art_friends)
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)


