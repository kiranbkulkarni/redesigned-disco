# Lambda functions
# One line anonymous function

items = [
    ("Product1", 10),
    ("product2", 9),
    ("Product3", 12)
]

#items.sort(key=lambda parameters: expression)

items.sort(key=lambda item: item[1])

print(items)
