Dictionary = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Fab": "fabulous",
    "FML": "Fuck my life",
    "Marv": "marvelous",
    1: "great",
    2: "yupp",
}

print(Dictionary["FML"])
print(Dictionary.get("Mar"))
print("My birthday is in the month of " + Dictionary["Jan"] + ".")
print("What a " + Dictionary.get("Marv") + " piece of art.")
print("")


# what if we put a value not contained in the dictionary?
print(Dictionary.get("abc", "Not in dictionary"))



