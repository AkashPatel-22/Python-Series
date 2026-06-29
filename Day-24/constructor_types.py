class student:
    def __init__(self,name):
        self.name = name
stu1 = student("rahul")
stu2 = student("harshita")

print(stu1.name,stu2.name)  # rahul , harshita

# Types Of Constructor.

# 1. default constructor - a const.call with no parameter except self.
# 2. parameterized constr.- takes parameters to initialize values 
#  uniquely for each object.
