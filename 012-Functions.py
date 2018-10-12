# We will make some functions now
def basic():
    print("Hello User")
    abc = input("What's your name: ")
    print("Hey there " + abc + ", I am Shivam")

# To call a function we can either directly call it or have it printed
basic()
print("")
print(basic())
print("")


# We can even make it better
def example(name, age):
    print("Hello User")
    abc = input("What's your name: ")
    aaa = input("What's your age:")
    print("Hey there " + abc + ", good to know that you are " + aaa + " years old " + ", I am " + name + ", " + str(age))


example("Shivam", 19)
print("")
print(example("a python bot!", 19))
print("")


print("Hope it helped you in understanding functions")