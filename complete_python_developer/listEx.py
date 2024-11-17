cart = ['notebooks','sunglasses','toys','grapes']
print(cart)
print(cart[0])  
print(cart[:3])
cart[0] = 'mouse'
print(cart)

#copy of cart
new_cart = cart[:]
print(new_cart)

cart[0] = 'keyboard'

print(cart)
print(new_cart)