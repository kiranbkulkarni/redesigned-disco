from sys import getsizeof

values_gen = (x*2 for x in range(1000000))
print("gen:", getsizeof(values_gen))
values = [x*2 for x in range(1000000)]
print("list:", getsizeof(values))

# It's not possible to check the length of the generator objects before hand
print(len(values))

# This will throw a run-time error
print(len(values_gen))
