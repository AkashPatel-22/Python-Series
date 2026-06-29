# "self" is a special parameter which refers to 
# the instance of the class that is calling the method.
# we don't need to pass it explicitly


# we can also ise contructor to initialize values for objects.
class student:
    def __init__(self,name):
        self.name = name
stu1 = student("rahul")
stu2 = student("harshita")

print(stu1.name,stu2.name)  # rahul , harshita

# Types Of Constructor.

# 1. default constructor - a constructor call with no parameter except self.

# 2. parameterized constr.- takes parameters to initialize values 
#  uniquely for each object.

# NOTE - Python doesn't support constructor overloading directly (like java/C++) i.e
# having multiple constructor in the same class. whichever is written last is executed.