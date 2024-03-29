#training on dictionary

students = [
     {"name" : "Nirmal" , "age" : 21 }, { "name" : "Virmal" , "age" : 22 }, { "name" : "Sirmal" , "age" : 28 }
]

#print(students)
for student in students:
   print([f"{name} {age}" for name,age in student.items()])
   print([value for value in student.values()])
   print([keys for keys in student.keys() ])
