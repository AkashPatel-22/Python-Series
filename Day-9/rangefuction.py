# range function-
# - is used to generate sequnece of numbers.
# - typically used for loops.

#  the function has three parameters:

# 1-start(default=0) - the no. to srt from
# 2-stop - the no. to stop before(not included)
# 2-step(default = 1) - how much to increase by  eaach time

# example :- single argument - start
for i in range(5):
    print(i) # 0,1,2,3,4

# double arguments - start,stop
for i in range(1,5):
    print(i) 
    # 1,2,3,4
    
# triple argumensts - start,stop,step

for i in range(1,10,2):
    print(i)
    # odd no.'s