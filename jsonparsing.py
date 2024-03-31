#Converting Json to Python & vice versa
import json

#some json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y)
print(y["name"])
print(y["age"])
print(y["city"])
print(json.dumps(x))



#Converting the Pythong objects to Json Strings, print values
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#Converting the python object to json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print('\n')
print('\n')
print('\n')
print('\n')

#indenting the json results. 
print(json.dumps(x, indent=4 ))


#sorting the keys. 
print(json.dumps(x, indent=4, sort_keys=True ))
