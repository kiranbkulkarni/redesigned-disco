message = "a"


def greet():
    message = "b"
    print(message)


message = "c"
greet()
print(message)

# Now let's try with the global keyword


def greet_global():
    global message
    message = "Global"


greet_global()
print(message)
# Observe that the global keyword works
