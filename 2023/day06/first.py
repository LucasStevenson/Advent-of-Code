import sys
import re
import math
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    times = [int(x) for x in re.findall(r"\d+", f.readline())]
    distances = [int(x) for x in re.findall(r"\d+", f.readline())]

exceeds_distance = []
for time, distance in zip(times, distances):
    numWaysWin = 0
    for boatSpeed in range(1, time):
        distTraveled = (time-boatSpeed)*boatSpeed
        if distTraveled > distance:
            numWaysWin += 1
    exceeds_distance.append(max(numWaysWin, 1))

print(math.prod(exceeds_distance))
