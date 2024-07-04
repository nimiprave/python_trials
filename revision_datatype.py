#types of datatyes

x = 10
print(type(x))

# String
y = "something"
print(type(y))

#touple
touple = ("first", "second", "third")
print(type(touple))
print(touple)

#touple.__add__(("fourth"))
#print(touple)

#list
list = ["first","second","third"]
print(type(list))
print(list)
print(list[0])
print(list[1])
print(list[2])

#range
range_v = range(10)
print(range_v)
for n in range_v:
    print(n)


#dic
dic_x = { "name" : "nirmal", "Age": "3"}
print(dic_x)
print(dic_x.get("name"))