try:
    # The with statment automatically release the resources
    # There is no need to release the resourcese explicitly
    # Always use the with keyword whenever you are trying to open a connection
    # To a file, a database, or a network connection

    # If the object follows context management protocol then
    # we can make use of with key word
    with open("../Exceptions/file.txt") as file:
        print("File opened.")
        file.__enter__
        file.__exit__
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valued age.")
else:
    print("No exceptions were thrown")
finally:
    file.close()
