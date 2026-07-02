# Types of Inheritence.

# 1. single inheritence.
# - a child inherits from one parent.

#parent -> chid.

class parent:
    def display(self):
        print("parent class")
class child(parent):
    pass
c = child()
c.display() # parent class -  output


# 2. Multi-level inheritence.
# - a child inherits from,parent & another class inherits from the child.

# granparent(employee) + parent(adminstaff) + child(accountant)

class Employee:          #parent class.
    start_time = "9AM"
    end_time = "5pM"
    
class adminstaff(Employee):        #child class
    def __init__(self,role):
        self.role = role
        
class accountant(adminstaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary
        
acc = accountant(50_000,"CA")
print(acc.salary,acc.role,acc.start_time,acc.end_time)


# 3. Multiple inheritence.
# - a child inherits from more than one parent class.

class teacher:
    def __init__(self, salary):
        self.salary = salary
class student():          
    def __init__(self, gpa):
        self.gpa = gpa
        
class TA(teacher,student):        #child class
    def __init__(self,name, salary, gpa):
        super().__init__(salary)
        student.__init__(self,gpa)
        self.name = name
        
ta = TA("rahul", 50_000, 7.5)
print(ta.name,ta.salary,ta.gpa)

# super() keyword - used tp call parent class's method from child class.