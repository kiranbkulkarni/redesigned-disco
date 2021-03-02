# List comprehensions are very useful

# The easy way to write an List Comprehensions are
# [expression for item in items]

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

prices = list(map(lambda item: item[1], items))
#[expression for item in items]
prices_lc = [item[1] for item in items]
print(prices_lc)

prices_filtered = list(filter(lambda item: item[1] >= 10, items))
print(prices_filtered)

filter = [item for item in items if item[1] >= 10]
print(filter)
