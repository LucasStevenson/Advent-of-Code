import sys
from collections import deque
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    lines = [ list(line.rstrip()) for line in f.readlines() if line.strip() ]
    foundEnd = False
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                lines[i][j] = 'a'
            elif lines[i][j] == "E":
                r, c = i, j
                foundEnd = True
                lines[i][j] = 'z'
        if foundEnd:
            break

Q = deque()
Q.appendleft((r,c, 0))
visited = [(r,c)]
while Q:
    r, c, numSteps = Q.pop()
    if lines[r][c] == 'a':
        print(numSteps)
        break
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        # check a point's neighbors
        rr = r+dr
        cc = c+dc
        if (rr, cc) in visited:
            continue
        if not (0 <= r+dr < len(lines) and 0 <= c+dc < len(lines[r])):
            continue
        if ord(lines[r][c]) - ord(lines[rr][cc]) > 1:
            continue
        Q.appendleft((rr, cc, numSteps+1))
        visited.append((rr,cc))
