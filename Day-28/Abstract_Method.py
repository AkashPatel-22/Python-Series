# Abstract Method.
# -it is method to declared but not implement(children must override abstarct methods)
# @abstractmethod
# def method_name(self):

# exmaple.

from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound():
        pass
class lion(animal):
    def make_sound(self):
        print("roar!")
class cow(animal):
    def make_sound(self):
        print("moo!")
lion = lion()
lion.make_sound()

cow = cow()
cow.make_sound()