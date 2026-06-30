# Methods :
# - methods are functions defined inside a class,
#  representing the behavior or actions of an object.

# Types of Methods.

# 1. Instance Methods.
#  - take self as the first arguments.
#  - can access both instance attributes and class attributes.

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):   # instance method
        print(f"name:{self.name}, marks:{self.marks}")
        
# 2. Class Methods.
# - use @classmethod decorator.
# - take cls (class) as first argument.
# - used to work with class-level data.

class student:
    school_name = "ABC school"
    
    @classmethod
    def change_school(cls,new_mane):
        cls.school_name = new_mane
        

# 3. Static Methods.
# - use @staticmethod decorator.
# - do not take self or cls.
# - behave like normal fucntion but belong to the class for logical grouping

class math:
    @staticmethod
    def add(a,b):
        return a + b