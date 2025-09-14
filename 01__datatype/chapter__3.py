# x = 5
# y = "Parvez"
# print(x, y)


x = str(3)  # x will be "3"
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

print(type(x))
print(type(y))
print(type(z))


# many values to multiple variables
"""
x, y, z, p = "orange", "mango", "banana", "guava"
print(x)
print(y)
print(z)

"""
# one value to multiple variables
x = y = z = "Orange"
print(x, y, z)


# unpack a collection
names = ["taniya", "afroja", "jerin"]
t, f, j = names
print(t, f, j)
