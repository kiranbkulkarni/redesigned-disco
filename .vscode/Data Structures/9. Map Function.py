items = [
    ("Product1", 10),
    ("product2", 9),
    ("Product3", 12)
]

# What if you want to transform the above list into a number list

price = []
for item in items:
    price.append(item[1])

x = map(lambda item: item[1], items)
print(x)
for item in x:
    print(item)

x = list(map(lambda item: item[1], items))
print(x)
print(price)
