# Writing to a file

# 1. write()
# -writes a string to a file.

f = open("data.txt","w")
f.write("Hello There!")
f.close()

# 2. writelines()
# -writes multiple lines at once.

f = open("data.txt","w")
f.writelines(["Hello There!", "students"])
f.close()

# NOTE - Always remember to close a file at the end to free system resources.