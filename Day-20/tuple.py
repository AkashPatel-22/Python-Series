# Tuple - tuple is an ordered, immutable collection of items.
# -ordered.
# -immutable
# -allows duplicate.
# -heterogenious.

tup = (10,20,30,40)
print(tup)
print(type(tup))

empty_tuple = ()  #empty_tuple
single_element_tuple = (42,)

# Indexing & Slicing - same as lists

print(tup[1])  # 20
print(tup[-1])  # 40- last element
print(tup[0:2])  # 10, 20

