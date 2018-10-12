def abc(num1, num2, num3):
    if float(num1) > float(num2) and float(num1) > float(num3):
        print(num1 + " is the greatest no.")

    elif float(num2) > float(num1) and float(num2) > float(num3):
        print(num2 + " is the greatest no.")

    elif float(num3) > float(num1) and float(num3) > float(num2):
        print(num3 + " is the greatest no.")
    else:
        print("All the values are equal!")


num1 = input("Enter first value:")
num2 = input("Enter second value:")
num3 = input("Enter third value:")
print(abc(num1, num2, num3))
print("")
print(abc("3", "5", "7"))
print("")
print(abc("3.343", "-5.43", "7.41"))
print("")