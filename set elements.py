#User input to run the loop
i = int(input())
#Taking angles to append in the list
angles = [70]
for n in range(1,i):
    c = (1/13)*n + 70
    angles.append(c)
    print(c)
#Checking if the loop has reached 70 degrees
    if c%360  == 70:
        break

#Printing the length of the list(Index starts at 0)    
print(len(angles)-1) 
