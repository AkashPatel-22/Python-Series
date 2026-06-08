# Conditional Statement
# -conditional statement means let ou program decide whatb to do based on conditons

# 3 main conditional statement:-

# 1. if - used to check condition , if its true or not
# 2. else - runs when all above condition are false
# 3. elif (else if) - used to check multiple conditions 


# some example shown below :- 

# example 1:- voting rights

age = int(input("enter your age: "))

if age >= 18:
    print("you can vote")
    print("you can drive")
else:
    print("you can't vote")    
    print("you can't drive")

# example 2:- tarffic lights

color = input("enter color: ")

if color == "red" or color == "RED":
    print("STOP")
elif color == "green" or color == "GREEN":
    print("GOO")
elif color == "yellow" or color == "YELLOW":
    print("LOOK & WAIT")
else:
    print("wrong color")        