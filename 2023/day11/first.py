import sys
import numpy as np
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    grid = []
    while line := list(f.readline().strip()):
        grid.append(line)
        if all(x == "." for x in line):
            grid.append(line)
    transposedGrid = []
    for row in np.array(grid).T:
        transposedGrid.append(row)
        if all(x == "." for x in row):
            transposedGrid.append(row)
    grid = np.array(transposedGrid).T

D = {} # { galaxyID: (x, y) }
galaxyID = 1
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "#":
            D[galaxyID] = (r, c)
            galaxyID += 1

def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

ans = 0
for i in range(1, len(D)):
    for j in range(i+1, len(D)+1):
        ans += manhattan_distance(D[i], D[j])
print(ans)
