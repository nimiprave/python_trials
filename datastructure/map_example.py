s = ['1', '2', '3', '4', '5']

# converting the list elements to int from string.
res = map(int, s)
print(list(res))

# appending the list element with !
res_tx = map(lambda x: x + '!', s)
print(list(res_tx))
