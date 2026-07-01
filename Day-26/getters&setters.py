# Getters & Setters.
# -when we make a variable private, we use methods to read it(getters)
# - or update it (setters).

class Employee:
    def __init__(self, salary):
        self.__salary = salary
        
    def get_salary(self):        # getters
        return self.__salary

    def set_salary(self, new_salary):        # getters
        self.__salary = new_salary
    
e = Employee(50000)
print(e.get_salary())
e.set_salary(60000)
print(e.get_salary())