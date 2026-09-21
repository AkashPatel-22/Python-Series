# string formatting.
# - process of creating dynamic string by inserting values from
# varibles or expressions into a predefined string template.
# two ways to format a string:-
# 1 - using format().
# 2 - using f-strings.


#  1 - Using .format()
# we {} to fromat the string 

name = " akash"
age = 23
text = "my name is {} and i am {} years old".format(name,age)
print(text)

# 2 - Using f-strings
name = " akash"
age = 23
text = f"my name is {name} and i am {age} years old"
print(text)
a = 5
b = 10
print(f"sum of {a} + {b} = {a+b}")
