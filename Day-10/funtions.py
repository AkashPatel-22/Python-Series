# Functions - blocks of reusable code that perform specific task
# def- keyword is use to define functions

# *******************************************************************
# example
def hello():
    print("hello from learner")  #function definition
hello() # function call


# *************function with parameters***********
# - parameter n arguments

def sum(a,b):  # a & b are parameters
    print(a+b)
sum(5,10) #arguments   

# return -keyword

def avg(a,b,c):
    return (a+b+c)/3
print(avg(1,2,3)) # direct fnx call kr skte hai print() ka use krk

# default parameters:
# -value provide nhi karenge to deafult parameter value le lega

# sum fnx with default paramter 1

def sum(a,b = 1): # b = 1 - default parameter
    print(f"sum is:{a+b}")
sum(5) #6
sum(6,7) # 13