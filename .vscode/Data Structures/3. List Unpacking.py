# Unpacking lists

# Normally
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# With List unpacking
# Number of variables should be equal to the number of items in the list
first, second, third = numbers
print(first, second, third)

# What if we have more than 3 items. Say, we have 7  items
numbers_7 = [1, 2, 3, 4, 5, 6, 7]

# We can't write so many variables.
first, second, *other = numbers_7
print(first)
print(other)

first, second = numbers_7[0:2]
print(first)
print(second)

print("This section is for *others in middle")
first, *others, last = numbers_7
print(first)
print(*others)
print(last)
