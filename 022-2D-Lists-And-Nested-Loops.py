# Accessing elements in lists
lists = [
    [1, 2, 3, 6],
    [4, 5, 6, 8],
    [7, 8, 9, 9],
    [0, 7, 3, 2]
]

print(lists[0][2])
print(lists[2][1])
print("")


# Nested Loops ie loops within loops
for abc in lists:
    print(abc)
print("")


for abc in lists:
    for xyz in abc:
        print(xyz)
print("")