# Inheritence.
# - is where one class(child) accquires the properties & behaviors
# (variables + methods) of another class (parent).
# - the class whose properties are inherited - parent / base / superclass.
# - the class that inherits - child / derived / subclass.

class Employee:          #parent class.
    start_time = "9AM"
    end_time = "5pM"
    
class Teacher(Employee):        #child class
    def __init__(self,subject):
        self.subject = subject

t = Teacher("data science")
print(t.subject,t.start_time,t.end_time)

# inheritence enables:
# - code reuse
# - extensibility
# - cleaner,maintainable design
# - polymorphism