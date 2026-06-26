# Sets Methods.

# 1. add(val)- adds new elements to set
# 2. remove(val)- remove elements(raise error if not found)
# 3. clear()- remove all elements.
# 4. pop()- removes and returns a random elements.

# 5. s1.union(s2) - returns new union( union collection of all unique values
# in both sets).

# 6. s1.nintersection(s2) - returns new union ( intersection is a collection of
# all common & unique values in both sets)

s = {10,20,30}

s.add(40) # 40,10,20,30
print(s)

s.remove(10) # 40, 20 ,30
print(s)

print(s.pop()) # can be any value

s.clear() # set() - emptyset
print(s)


# union & intersection 
a ={1,2,3}
b ={3,4,5}
print(a.union(b)) # {1,2,3,4,5}
print(a.intersection(b)) # {3}