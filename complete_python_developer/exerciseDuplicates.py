some_list = ['a', 'b', 'c', 'b', 'n', 'm', 'n', 'd']

# Find duplicates in the list
for element in some_list:
    if some_list.count(element) > 1:
        print(f'{element} is a duplicate')

#sorting techinque
some_list.sort()
print(some_list)
previous = ''
for item in some_list:
   if previous == item:
       print(f'{item} is a duplicate')
   previous = item    