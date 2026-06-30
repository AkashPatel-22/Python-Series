# Attributes in OOP
# - Attributes are variable that belong to a class or an object.
# they store data/state of the object.

# Types of Attributes.

# 1. Class Attributes.
# -Belong to the class itself, shared by all objects.
# -Defined outside any method in the class.

class student:
    college = "ABC college"     # class attributes.

stu1 = student ()    
print(stu1.college)
print(student.college) # class attribute can also be accesed with class name.


# 2. Instance Attributes.
# -Belong individually to each object.
# -Defined inside the __init__ method using self.
# -Each object gets its own copy.

class Student:
    def __init__(self,name,cgpa):    # instance attributes.
        self.name = name
        self.cgpa = cgpa
        
stu2 = Student("Rahul",8.7)
print(stu2.name,stu2.cgpa)
        