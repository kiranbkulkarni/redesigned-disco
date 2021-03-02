# how to add or remove items

letters = ["a", "b", "c"]

# Where do you want to add the items? is it at the end of the list?
letters.append("d")
letters.insert(0, "-")

# Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)
