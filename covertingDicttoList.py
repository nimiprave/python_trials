import json
#creating a dictionary
payload = {
    "name": "John",
    "age": 30,  
    "city": "New York",
    "is_student": False,
}

print(payload)
#converting the dictionary to a list    
payload_list = list(payload.items())
print(payload_list)

items = payload.items()
print(f"Items: {items}")
# Converting the payload to json
json_payload = json.dumps(payload)
print(json_payload)

##
blist = []
for key, value in payload.items():
    blist.append(f"\"{key}\" : \"{value}\"")
    
print(blist)