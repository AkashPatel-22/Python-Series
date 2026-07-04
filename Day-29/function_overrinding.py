# Function Overriding (Method Overriding).

# /** when a child class provides its own version of a method that already
# exits in the parent class (both methods should have same name)
# - type of runtime polymorphism(dynamic binding)
# - child methods takes precedence overparent method**/

class animal:
    def sound(self):
        print("some generic sound")
class lion(animal):
    def sound(self):
        print("roar!")

a = animal()
l = lion()

a.sound() # some generic sound
l.sound() # roar

