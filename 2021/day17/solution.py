import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    x1, x2, y1, y2 = map(int, re.search(r"x=(\d+)\.\.(\d+)\, y=(\-?\d+)\.\.(\-?\d+)", f.readline()).groups())
    xRange, yRange = range(x1,x2+1), range(y1, y2+1)

goodStarts = {}
for dx in range(-200, 200):
    for dy in range(-200, 200):
        x, y = 0,0
        numSteps = 0
        maxHeight = 0
        while True:
            if x in xRange and y in yRange:
                goodStarts[(dx,dy)] = maxHeight
                break
            if y < y1 or x > x2:
                break
            if dx > numSteps:
                x += dx - numSteps
            y += dy - numSteps
            maxHeight = max(maxHeight, y)
            numSteps += 1

print(f"Part 1: {max([ v for k,v in goodStarts.items() ])}")
print(f"Part 2: {len((goodStarts))}")
