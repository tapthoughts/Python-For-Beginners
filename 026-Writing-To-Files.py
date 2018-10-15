# r = read
# w = write
# a = no changes or modifications but adding at the end (append info)
# r+ = read and write

# Take care while appending files
# each time you run the program, a value gets stored there
file = open("026-Sample.txt", "a")
file.write("\n346")
file.close()


# Write function overwrites data and 
# so use a different file or it will overwrite on your previous data
file = open("026-Sample2.txt", "w")
file.write("\n346")
file.close()
