name = "nirmal praveen pothuraj"
print(name)

# methods or behaviors or functions
result = name.find("praveen")
if result > 0:
    print("String found")
else:
    print("String not found")

# Replacing a string. String is not mutable which means cannot be changed.
newName = name.replace("praveen", "shyam")

print("oldName: {}".format(name))
print("NewName: {}".format(newName))
