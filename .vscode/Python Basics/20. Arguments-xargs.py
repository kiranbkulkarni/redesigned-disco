# lets say you want to pass arbitrary number of arguments to your function

def multiply(a, b):
    return a*b


def multiply_args(*list):
    print(list)


# This outputs a tuple
print(multiply_args(2, 3, 4, 5))


def multiply_total(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply_total(2, 3, 4, 5))
