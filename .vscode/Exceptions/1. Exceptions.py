# To stop your applications from crashing
# To display a proper message when error occurs
# Errors are inevitable

# List of examples

numbers = [1, 2]
print(numbers[3])

# The following code throws an error
# Traceback(most recent call last):
#   File "/Users/kirankulkarni/Desktop/HelloWorld/.vscode/Exceptions/1. Exceptions.py", line 8, in <module >
#   print(numbers[3])
# IndexError: list index out of range

# Example 2
Age = int(input("Age: "))

# What if the user inputs a character instead of numeric value

# So let's make use of try & catch statements
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues")
