# Abstraction.
# -is hiding unnecessary implementation details and showing only the
# essential featueres to the user.

# we implement abstraction with abstract classes & abstract methods.

# Abstract Class.
# an abstract class in python is one which;
# - cannot be instantiated
# - can contain normal + abstract methods
# - usually acts as a buleprint for child classes

from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

