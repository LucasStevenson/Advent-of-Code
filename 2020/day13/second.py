#!/usr/bin/env python3
import math
with open("input.txt") as f:
    busIDs = f.readlines()
    del busIDs[0]
    busIDs = [busID.rstrip() for busID in busIDs[0].split(",") if busID.strip()]

rem = []
for i in range(len(busIDs)):
    if busIDs[i] == "x":
        continue
    rem.append(int(busIDs[i])-i)

busIDs = [int(x) for x in busIDs if x != "x"]

def findMinX(busIDs, rem):
    prod = math.prod(busIDs) # product of all busIDs
    return sum([rem[index]*(prod//busID)*pow(prod//busID,-1,busID) for index, busID in enumerate(busIDs)]) % prod

'''
This function does the same thing as the one above but with an extra loop. I'm keeping it here because I feel it's easier to read and understand.

def findMinX(busIDs, rem):
    prod = math.prod(busIDs) # product of all busIDs
    pp = [] # pp[i] = product / busIDs[i]
    inv = [] # modular inverse of pp[i] and busIDs[i]
    for busID in busIDs:
        pp.append(prod//busID)
        inv.append(pow(prod//busID, -1, busID))
    return sum([rem[i]*pp[i]*inv[i] for i in range(len(busIDs))])%prod
'''

print(findMinX(busIDs, rem))
