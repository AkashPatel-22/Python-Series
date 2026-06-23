# Linear Search(using loop)
# --checks elements one by one to find target (x).
 
number = [10, 20, 30, 40, 18, 50]
x = 18
idx = 0
for num in number:
    if num == x:
        print(f"{x} found at index = {idx}")
    idx += 1    
    