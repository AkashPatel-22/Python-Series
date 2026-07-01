# OOP Pillars.
# -4 pillars are - encapsulation, abstraction,inheritence & polymorphism


# Encapsulation.
# /* - encapsulation is the bunding of data(variables)& methods (functions)
# that operate on that data into a single unit(a class), along with controlling
# accessto that data.
# this is done to protect the data from accidental or unauthorised modification
# 
# to implement encapsulation, we use acess modifiers.
# python has 3 access levels: **/


# 1. Public Members.
# - accessible everywhere, written like normal variables.

class student:
    def __init__(self, name):
        self.name = name # public variables
        
s = student("rahul")
print(s.name) # allowed


# 2. Protected Members.
# - indicate by a single underscore _ (do not access directly unless needed)
# - still accessible from outside( not truly protected)
# - intended for internal use or inheritence.

class person:
    def __init__(self):
        self._age = 20 # protected variables
        
p = person()
print(p._age) #technically allowed but not recommended


# 3. Private Members.
# - indicated by a double underscore__
# - python does name mangling: the variable name becomes _className__variable
# - cannot be access directly from outside.

class bank:
    def __init__(self, balance):
        self.__balance = balance # private member.

b = bank(50000)
# print(b.__balance) # error: attribute not accessible        
#  so to access:
print(b._bank__balance) # allowed (name-mangled form)