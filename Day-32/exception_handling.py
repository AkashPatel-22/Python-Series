# Exception Handling.
# /**an exception is an error that occurs while a program is running.
# if not handled. the program crashes. it allows you to manage errors 
# gracefully sp your program continues to run.

# it occurs when python encounters something it cannot handle during execution.**/

# example:
# - dividing by zero = ZeroDivisionError
# - using an undefined variable - NameError
# - opening a missing file - FileNotFoundError
# - wrong datatype - TypeError.

#  basic sytax

# try:
#     # code that may cause an error
# except:
#     # code that runs if error occurs

# example 1.

try:
    x = 10/0
except:
    print("error occured!")

# example 2.

try:
    print(10/0)
except ZeroDivisionError:
    print("you can't divide by zero")