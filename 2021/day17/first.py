import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


with open(infile) as f:
    x1, x2, y1, y2 = map(int, re.search(r"x=(\d+)\.\.(\d+)\, y=(\-?\d+)\.\.(\-?\d+)", f.readline()).groups())
    print((x1, x2, y1, y2))
    xRange = range(x1,x2+1)
    yRange = range(y1, y2+1)

goodStarts = []
ans = 0
for x in range(-200, 200):
    for y in range(-200, 200):
        sx, sy = 0,0
        numSteps = 0
        maxHeight = 0
        while True:
            if sx in xRange and sy in yRange:
                ans = max(ans, maxHeight)
                goodStarts.append((x, y))
                break
            if sy < y1 or sx > x2:
                break
            if x > numSteps:
                sx += x - numSteps
            sy += y - numSteps
            maxHeight = max(maxHeight, sy)
            numSteps += 1
print(len((goodStarts)))

print(ans)
