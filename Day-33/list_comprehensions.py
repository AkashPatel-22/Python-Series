# List Comprehensions.
# - list comprehensions is a short and elegant way to create lists in python.
# - it replaces long for loops with one-line expressions.

#  Basic Syntax.
# [expression for item in iterable]

# Ex 1.- create a list of number 1 to 5

nums = [x for x in range(1,6)]
print(nums)    # [1,2,3,4,5]


#  List Comprehnsion with Conditions
# syntax
# [expression for item in iterable if condition]

# Ex 2.- even numbers from 1 to 10

evens = [x for x in range(1,11) if x % 2 == 0]
print(evens)     # [2,4,6,8,10]


#  List Comprehnsion with if-else
# [expression_if_true if condition else expressio_if_false for item in iterable]
# 

# Ex 3.-label numbers as "Evens" or "Odd"

labels = ["even" if x % 2 == 0 else "odd" for x in range(1,6)]
print(labels)