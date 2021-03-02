# Very powerful data structure in Python

# key-value pairs

point = {"x": 1, "y": 2}

# dict() function can be used to create a dictionary

point_1 = dict(x=1, y=2)

print(point)
print(point_1)

# How to access an item in a dictionary
print(point["x"])

# How to add an item
point["z"] = 20
print(point)

# What happens when there is no existing key

# Like when you try to access a key that doesn't exist
# The statement below throws an error
# print(point["a"])

# The correct way to access a key is by using get() method
print(point.get("a", 0))

del point["x"]
print(point)

for x, y in point.items():
    print(x, y)
