# compute factorial of a number n using FUNCTION
# using Range Function
n = int(input("Enter Number:"))
fact = 1
for i in range(1,n+1):
    fact *= i
print("factorial is:", fact)    
