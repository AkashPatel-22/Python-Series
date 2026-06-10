
# Loop Control Statement.

# Break Keyword :- "it stops the loop immediately".

# example :- break for multiple of 6

i = 1
while i <= 10:
    if i % 6 == 0: #checking multiple of 6
        break # jse he multiple milega break ho jayega
    print(i)
    i += 1
    
# Continue Keyword :- " skip the current interation ans move to the next one ".

i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue;
    print(i)
     