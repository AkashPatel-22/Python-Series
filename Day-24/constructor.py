# constructor:
# -is a special method used to initialize newly created objects.

# -we use " __init__(self,..) " method to define our constructor.

# -whenever we create an object of a class. python automatically
# calls the _init_() method.

# - self is a instance of the class that is calling the method.

class student: # class
    def __init__(self):
        print("constructor was called")

stu1 = student() # constructor was called


# Attributes & Methods.
# - "Attributes" are variables "Methods" are function defined inside class.