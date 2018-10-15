try:
    num = int(input("Enter a no.: "))
    print(num)

except ZeroDivisionError:
    print("Divided by ZERO")
except ValueError:
    print("Invalid Input!")