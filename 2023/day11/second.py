import sys
import numpy as np
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    grid = []
    EMPTY_ROWS, EMPTY_COLS = [], []
    rowIdx = 0
    while line := list(f.readline().strip()):
        grid.append(line)
        if all(x == "." for x in line):
            EMPTY_ROWS.append(rowIdx)
        rowIdx += 1
    for rowIdx, row in enumerate(np.array(grid).T):
        if all(x == "." for x in row):
            EMPTY_COLS.append(rowIdx)

D = {} # { galaxyID: (x, y) }
galaxyID = 1
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "#":
            # count the number of elements in EMPTY_ROWS/COLS that are < r and < c, respectively
            a = len(list(filter(lambda x: x < r, EMPTY_ROWS)))
            b = len(list(filter(lambda x: x < c, EMPTY_COLS)))
            D[galaxyID] = (r+(a*999999), c+(b*999999))
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
