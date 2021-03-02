letters = ["a", "b", "c", "d"]

print(letters[-1])
print(letters[0])

letters[0] = "A"
print(letters)


print(letters[0:3])
print(letters[0:])
print(letters[:])
print(letters[::2])

numbers = list(range(20))

# Tp print every number in the numbers list with step count =2
print(numbers[::2])

# To print the whole list in reverse order
print(numbers[::-1])
