values = []

for x in range(5):
    values.append(x * 2)

list_values = [x * 2 for x in range(5)]
print(list_values)
print(type(list_values))

# Similarly,
set_values = {x * 2 for x in range(5)}
print(set_values)
print(type(set_values))

dict_object = {x: x*2 for x in range(5)}
print(dict_object)
print(type(dict_object))
