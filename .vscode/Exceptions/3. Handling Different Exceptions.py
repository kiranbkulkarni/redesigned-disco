try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")0
else:
    print("No exceptions were thrown.")
