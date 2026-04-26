X = input("Give me a number : ")
try:
    num = float(X) 

    if num.is_integer():
        print("This number is an Integer.")
    else:
        print("This number is a Decimal.")

except ValueError:
    print("This is not a number.")