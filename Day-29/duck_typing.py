
# Duck Typing. - works on idea..
# - "if it looks like a duck and quacks like a duck, it must be a duck"

class dog:
    def speak(self):
        print("bark")
class cat:
    def speak(self):
        print("meowww")
class robot:
    def speak(self):
        print("beep beeep")
        
def make_it_speak(entity):
    entity.speak() # doesn't care about the type
    

d = dog()
c = cat()
r = robot()

for e in [d,c,r]:
    make_it_speak(e)