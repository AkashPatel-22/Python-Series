# Deleting a File.
# - to delete a file we use the remove function.
import os
os.remove("data.txt")


# NOTE : usage with open()
#  we use a context manager that automatically closes the file.

with open("data.txt","r") as f:
    content = f.read()
    print(content)