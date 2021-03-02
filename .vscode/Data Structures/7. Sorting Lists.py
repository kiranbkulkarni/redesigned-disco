numbers = [3, 51, 2, 8, 6]

numbers.sort()

numbers.sort(reverse=True)

print(numbers)

sorted(numbers)

sorted(numbers, reverse=True)

# What if we tuples

items = [
    ("Product1", 10),
    ("product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
