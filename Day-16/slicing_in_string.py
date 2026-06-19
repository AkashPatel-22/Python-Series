# Slicing in String.
# --slicing is powerful features of python that lets us access multiple elements at once.
# we can do slicing in strings & even on the other sequence like list & tuples.

# the general syntax for slicing a string is :

# -->  "string[start:stop:step]"
# where
# start = index where the slice starts(inclusive). Default to 0 if omitted.
# stop = index where the slice ends(exclusive). Defaults to the end of the string if omitted.
# step = how many indices move forward each time. Default to 1.

#  example.

s = "Python"

print(s[0:2]) # 'Py'
print(s[2:]) # 'thon'
print(s[:3]) # 'Py t'
print(s[::2]) # 'Pto' --> (every second character)
print(s[::-1]) # 'nohtyp' --> (reversed string)