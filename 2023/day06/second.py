import sys
import re
import math
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    time = int(re.search(r"\d+", f.readline().replace(" ", ""))[0])
    distance = int(re.search(r"\d+", f.readline().replace(" ", ""))[0])

numWaysWin = 0
for boatSpeed in range(1, time):
    distTraveled = (time-boatSpeed)*boatSpeed
    if distTraveled > distance:
        numWaysWin += 1

print(numWaysWin)
