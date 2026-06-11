# FOR LOOP:
# syntax - for variable in sequence 

# example 1-
# for i in range(5): #i= 0  se start ho rha 
#    print(i) # 0,1,2,3,4
   
# example 2-
# word = "prime"
# # looping over a string
# for ch in word:
#     print(ch)
    
# example 3- counting no.of i's in a word

# word = "artificial intelligence"
# count = 0
# for ch in word:
#     if ch == 'i':
#         count += 1
# print(f"i occurs {count} times.")        

# example 4 - check if i exit in a word

word = "prime"

if 'i' in word: # is tarike se bhi if ka use krk looping kar skte hai
    print("letter exits")