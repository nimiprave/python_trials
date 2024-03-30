# lambda function and functions as first citizens

students = [
    {"name": "Rolf", "marks": (90, 80, 70, 87, 90)},
    {"name": "Charlie", "marks": (91, 82, 73, 67, 90)},
    {"name": "Anna", "marks": (83, 74, 95, 91, 99)},
    {"name": "Jen", "marks": (99, 60, 92, 97, 93)},
]

operations = {
    "average" : lambda seq: sum(seq) / len(seq),
    "total"  : lambda seq: sum(seq),
    "top" : lambda seq : max(seq)
}

total = lambda seq: sum(seq)
average = lambda seq: sum(seq) / len(seq)
top = lambda seq : max(seq)


#print(students[0]["marks"])
#print(total(students[0]["marks"]))

for student in students:
    your_choice = input("What do like to see? 'average', 'total','top' : " )
    print(operations[your_choice](student["marks"]))
    