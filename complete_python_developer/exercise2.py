my_list = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in my_list:
    total = total + i

print(f'The Sum of the list is: {total}')
print(f'The Average of the list is: {total/len(my_list)}')


#range function usage
range_list = list(range(1,11))
print(range_list)

#range function with jump over usage
range_list = list(range(1,11,2))
print(range_list)

#range function with jump over usage
range_list = list(range(11,0,-2))
print(range_list)


#enumerate function usage
for i, char in enumerate(list(range(0,10))):
    print(f'Index: {i}, value is: {char}')
    if char == 5:
        print(f'Index of 5 is: {i}')