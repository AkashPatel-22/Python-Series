# print odd numbers from 1 to 10 using while loop (using continue)

i = 1
while i < 10:
    i += 1 # pehle i ko increase kiye
    if i % 2 == 0: # then conndition check
        continue;# if its meets continue
    print(i)# if not then print odd no