payload = open('payloadList.json', 'r').read()
print(payload)

#convert the payload to the list
students = list(payload)
#print(students)

alt_students = [
        {
            "name": 'John',
            "age": 23,
            "marks": 90
        },
        {
            "name": 'Jane',
            "age": 24,
            "marks": 85
        },
        {
            "name": 'Jack',
            "age": 22,
            "marks": 95
        }
]
print(f'The length of alternative student: {len(alt_students)}')

#consuming the element list and printing the values dictionaries
total = 0
for student in alt_students:
    print(f'Student name: {student["name"]} , age is {student["age"]} and marks is {student["marks"]}')
    total = total + student["marks"]

average = total / len(alt_students)
print(f'The average marks of the students is: {average}')