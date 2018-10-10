# To print continuous text in next ine
print("The\nAbstract\nPeople")


# To leave a gap between lines
print("")


# To print characters like (") (') (\)
print("A\" B\' C\\ ")
print("")


# To store values in variables
abc = "Hello World"
print(abc)
print(abc + ", Welcome onboard")
print(abc.lower() + " is now in lower case")
print(abc.upper() + " is now in upper case")
print("")


# We can also check whether it's completely in upper or lower case
abc = "HELLO WORLD"
print(abc.islower())
print(abc.isupper())
print(abc.lower().isupper())
print("")


# To check the length of the function or grab the required value in a string
print(len(abc))
print(abc[1])

# [5] will come blank since there was a gap and gaps are also counter in arrays
print(abc[5])

print(abc[7])
print(abc[10])
print("")


# To find the paths of the values in arrays
print(abc.index("H"))

# It only gives the starting point
print(abc.index("WOR"))

# If a value occurs 2 times it provides with the one coming before
print(abc.index("O"))
print("")


# To replace the values in an array
print(abc.replace("HELLO", "HI"))
# Whereas this doesn't affects the value in the variable itself
print(abc)


# Values not in array will show error
print(abc.index("Y"))






