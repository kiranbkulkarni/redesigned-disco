import typing


print("Hello World 😸")
print("*" * 10)

print("Hello World!")

x = 1
unit = 4

students_count = 1000
rating = 4.99
is_published = False
course_name = """
Mutliple
Lines
"""

x = 1
y = 2

x, y = 1, 2

x = y = 1

# Dynamic typing

# static typing
# int students_count = 1000

# Dynamic typing

students_count = 1000
students_count = True

print(type(students_count))
print(type(""))
print(type(0.05))


# Type annotation

age: int = 20
age = "Python"

# Mutable and Immutable types

x = 1

# To print the address of the x varaible
print(id(x))

# Increment x and print the address again
x = x+1

print(id(x))

# Immutable types
y = [1, 2, 3]
print(id(x))

y.append(4)
# You don't see any change in the address
print(id(x))

# Closer look at strings
course = "Python Programming"

print(len(course))

print(course[0])

# very interesting thing about python is negative indexing
print(course[-1])

# slicing the strings
# [start_index:end_index:step_count]
print(course[2:3])

print(course[::2])

print(course[0:])

print(course[:])
