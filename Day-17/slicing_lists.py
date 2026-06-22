# Slicing
#  -- slicing in lists is same as slicing in strings.

# the general syntax for slicing list is:
# list[start:end:step]

# start = inclusive
# end = exclusive
# step = optional (deafult = 1)

#  example 

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Simple Slice
print(numbers[2:5])      # Output: [2, 3, 4]

print(numbers[:4])       # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[5:])       # Output: [5, 6, 7, 8, 9] (from index 5 to end)
print(numbers[:])        # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy of the whole list)

# using STEP
print(numbers[::2])      # Output: [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[1::3])     # Output: [1, 4, 7] (start at 1, every 3rd element)

# NEGATIVE slice
print(numbers[-5:-2])    # Output: [5, 6, 7] (negative indexing from end)