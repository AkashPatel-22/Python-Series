# Reading from file
#  we have multiple functions to read content from a file.

# 1. read()
# - Reads retire file as a single string.

f = open("data.txt","r")
content = f.read()
print(content)
f.close()


# 2. readline()
# - reads one line at a time.
f = open("data.txt","r")
line1 = f.readline()
line2 = f.readline()
f.close()

# 3. readlines()
# - reads all the lines into a list.
f = open("data.txt","r")
line = f.readlines()