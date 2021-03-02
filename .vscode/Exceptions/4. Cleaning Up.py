# When you are using exxternal resources like files, databases
# After we are done using the resources
# We need to close the connection to the resources
# Otherwise, other programs will not be able to use that resource

# Example
try:
    file = open("Exceptions.py")
    age = int(input("Age: "))
    xfactor = 10/age
    # file.close()
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
