num1 = float(input("Enter first no."))
operator = (input("Enter the operator(+ - * % /)"))
num2 = float(input("Enter second no."))


if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "%":
    print(num1 % num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("Entered operator isn't valid.")
