abc = [1, 2, 3, 4, 5]
xyz = ["Ram", "Raman", "Nik", "Naman", "Shivam"]
tuv = ["false", "name", "reload", "game", "fame"]

# To extend or basically add arrays one after another
abc.extend(xyz)
print(abc)

abc.extend(tuv)
print(abc)

abc.extend(abc)
print(abc)

print(abc[11])
print("")


# We can even add elements in the array directly adding one at a time and even change them
tuv.append("shyam")
tuv.append("Shivam")
print(tuv)

tuv[1] = "Ram"
print(tuv)
print("")


# We can even add elements in between the array while rest elements shift by 1
tuv.insert(1, "COD")
tuv.insert(4, "Black")
print(tuv)
print("")


# We can remove elements
tuv.remove("game")
tuv.remove("false")
print(tuv)
print("")


# We can even empty the array
abc.clear()
print("")


# we can POP elements is removing elements from the end
xyz.pop()
print("")


# To find index no. of an array
tuv = ["false", "name", "reload", "game", "fame"]
print(tuv.index("false"))
print("")


# To count similar no. of elements in a list or sort elements
arr = ["false", "name", "reload", "game", "fame", "game"]
print(arr.count("game"))
arr.sort()
print(arr)
print("")


# To copy arrays or reverse arrays
aaa = arr.copy()
print(aaa)
aaa.reverse()
print(aaa)