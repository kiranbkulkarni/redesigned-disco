
# To define a function

def funcname():
    pass


def increment(number, by):
    return number + by


def increment_number_number(number, by):
    # This is called a tuple
    return (number, number + by)


print(increment(2, 3))

print(increment_number_number(5, 6))

# Functions with Key word arguments
print(increment(2, by=3))

# passing functions the default value


def increment_default(number, by=4):
    return number + by


# Observe here, there is no need to pass the value for 'by' parameter
print(increment_default(3))

# observe here, if the value for 'by' parameter is passed then the default value will be overrided
print(increment_default(3, 9))

# Type annotation and with default parameters


def increment_anno(number: int, by: int = 1) -> int:
    return number + by


print(increment_anno(4, 6))
