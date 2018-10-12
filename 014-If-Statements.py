# if are basic statements and the outcome depends whether that statement is true or not

if 4 < 6:
    print("yo")
print("")


if 1 > 4:
    print("cool")
else:
    print("right")
print("")


# Boolean Algebra can also be used in if statements
male = False
if male:
    print("You are male")

else:
    print("You are Female")
print("")


# We can even put multiple statements at once
if(4 < 5) and (4 > 2) and (7 > 2):
    print("All true")
print("")

# For multiple statements
male = False
tall = True

if male and not tall:
    print("You are male but not tall")

elif not male and tall:
    print("You aren't male but tall")

elif not male and not tall:
    print("You are neither male nor tall")

else:
    print("You are male and tall")
print("")


# We can even take inputs from the user
# If we will not use float or int cases, then the answer won't be accurate in case of negative nos. and decimal nos.
val1 = input("Enter first value:")
val2 = input("Enter second value:")
if float(val1) > float(val2):
    print(val1 + " is greater than " + val2)

elif float(val2) > float(val1):
    print(val2 + " is greater than " + val1)

else:
    print("Both the values are equal")

print("")
