# string..
# -string is a sequence of character enclosed in quotes- "str1", 'str2'
# -immutable,once created content cannot be changed directly

# example
str1 = "hello world"
str2 = 'prime'
print(f"{str1} of {str2}")

# len() function
# built in function-used to calculate length of string

word = "prime"
print(f"length of string is {len(word)}")

# concatenation-
# we can add two string, using + operator
str1 = "apna"
str2 = "college"

word = str1 + str2 # apnacollege
word1 = str1 + " " +str2 # apna collge

print(str1+" "+str2)
print(word)
print(word1)