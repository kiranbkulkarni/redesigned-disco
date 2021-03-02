# Unpacking operator

numbers = [1, 2, 3]

print(numbers)

# What if we want to print individual numbers
print(1, 2, 3)

# We make use of unpacking operator
print(*numbers)


# Example 2
values = list(range(5))

# The same can be achieved using unpakcing operator
values_un = [*range(5), *"Hello"]
print(values_un)

# we can also unpack in different ways
first = [1, 2]
second = [3]
values_un1 = [*first, *range(5), "a", *second, *"Hello"]
print(values_un1)

# How to unpakc a dictionary
first = {"x": 1}
second = {"x": 10, "y": 2}

combined = {**first, **second, "z": 1}

print(combined)
