numbers = [1, 1, 2, 3, 4]

uniques = set(numbers)

print(uniques)

second_set = {1, 4}

second_set.add(5)
second_set.remove(5)

len(second_set)

# Where exactly set is gonna shine

first_set = {1, 1, 2, 3, 4}
second_sett = {1, 5}

print(first_set | second_sett)
print(first_set & second_sett)
print(first_set - second_sett)
print(first_set ^ second_sett)

if 1 in first_set:
    print("YES")
