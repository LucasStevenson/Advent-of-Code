#!/usr/bin/env python3
import math
with open("input.txt") as f:
    timestamp, buses = f.readlines()
    buses = [ int(num) for num in buses.split(",") if num != "x" ]
    timestamp = float(timestamp)

# UPDATED SOLUTION
closestTimes = [int(x * (math.ceil(timestamp / x))) for x in buses]
print(int(min(closestTimes)-timestamp) * buses[closestTimes.index(min(closestTimes))])

'''
# OLD SOLUTION

difference = [buses[0] * math.ceil(timestamp/buses[0]), buses[0]]
# difference[0] is the closest factor of the busID to the timestamp
# difference[1] is the busID
for n in range(1, len(buses)):
    busNum = buses[n]
    diff = difference[0]
    busNum *= math.ceil(timestamp/busNum)
    if busNum >= timestamp and busNum - timestamp < diff:
        difference = [busNum - timestamp, buses[n]]
print(int(difference[0] * difference[1]))
'''
