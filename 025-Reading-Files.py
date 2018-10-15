# r = read
# w = write
# a = no changes or modifications but adding at the end (append info)
# r+ = read and write

file = open("025-Sample.txt", "r")
print(file.readable())
print(file.read())
print(file.readline())
print(file.readlines())
file.close()
print("")

file = open("025-Sample.txt", "r")
print(file.readlines()[2])
file.close()
print("")

file = open("025-Sample.txt", "r")
for abc in file.readlines():
    print(abc)
file.close()
print("")
