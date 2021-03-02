# Loop over with lists

letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

# What if we want iterate iver with indexes
for letter in enumerate(letters):
    # This returns items in the form of tuples
    print(letter)

for letter in enumerate(letters):
    # This returns items in the form of tuples arranged
    print(letter[0], letter[1])

print("This section is with tuple unpacking")
# Tuple unpacking
for index, letter in enumerate(letters):
    print(index, letter)
