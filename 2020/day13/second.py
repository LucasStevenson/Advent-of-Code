#!/usr/bin/env python3
import math
with open("input.txt") as f:
    busIDs = f.readlines()[1].rstrip().split(",")

rems = [-1*i for i in range(len(busIDs)) if busIDs[i] != "x"]
busIDs = [int(x) for x in busIDs if x != "x"]
'''
The chinese remainder theorem is used to solve a system of linear congruences where all the moduli are relatively coprime. What we have right now looks like this:

x = rems[0] (mod busIDs[0])
x = rems[1] (mod busIDs[1])
...
x = rems[i] (mod busIDs[i])

We can use this formula to find the solution: x = (∑(ai*Ni*Mi)) mod N
- N = product of all moduli (busIDs)
- ai = rems[i]
- Ni = N / busIDs[i]
- Mi = modinverse(Ni, busIDs[i])
'''
def CRT(remainders, moduli):
    N = math.prod(moduli)
    return sum([a*(N//n)*pow(N//n,-1,n) for a, n in zip(remainders, moduli)]) % N
print(CRT(rems, busIDs))
