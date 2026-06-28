# Class 
# -- a class is a blueprint or template for creating objects.
class car:  # class
    brand = "toyota"
    
# Object : an object is a (instance) realization of a class,it is the actual
# thing created by based on tht class blueprint.

car1 = car()  # object of class
car2 = car()   # object

print(car1.brand) #toyota
print(car2.brand) #toyota

# we use the '.'(dot operator) to access properties & methods of class

# Class v/s Object

#  Class                                       Object
# -class is a blueprint/template             - An object is a concrete onstance of a class.

# -does not exist in memory until            - contains actual data & occupies memory.
# instantiated.

# -one class can create any number            - each object is independent.
# objects