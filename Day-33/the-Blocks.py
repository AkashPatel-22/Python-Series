# The else Block.
# - else executes only if no execution happens.

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")
else:
    print("you entered:",x)
    
    
#  The finally Block.
# - finally always executes, whether an exception occurs or not.it is used
# for cleanup tasks (closing, releasing resources)

try:
    f = open("data.txt")
    print(f.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("execution completed")
