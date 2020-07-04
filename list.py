#Almost all data types can be inserted in a list.
#Meaning it is bound to multiple object at the same time

shoppingcart = [99, 'Hello, world', [9, 10, 11], 4.456, (9, 3), print,]

print(shoppingcart[2])
print(shoppingcart[2:])
print(shoppingcart[:2])

list3 = shoppingcart
list3.append(401)
print(shoppingcart)
list3.insert(4, str('45'))
print(shoppingcart)
#pop removes the last element in the list and return the value of the removed object.
#You can pop based on index

shoppingcart.pop()
print(shoppingcart)
shoppingcart.pop(3)
print(shoppingcart)
list3.insert(4, 3)
list3.insert(6, 3)
list3.insert(8, 3)
print(shoppingcart)

# The remove method deletes the first occurrence of the specified object

list3.remove(3)
print(shoppingcart)
