import sys
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    grid = []
    startPos = None
    rowIdx = 0
    while line := list(f.readline().strip()):
        grid.append(line)
        if "S" in line:
            startPos = (rowIdx, line.index("S"))
        rowIdx += 1

M = {
        (-1,0): ["|", "7", "F"], # when we go up
        (1,0): ["|", "L", "J"], # when we go down
        (0,-1): ["-", "L", "F"], # when we go left
        (0,1): ["-", "J", "7"] # when we go right
}

D = defaultdict(lambda: float("inf")) # { (x,y): numStepsToGetHere }
queue = deque([(startPos, 0)]) # [(position, numSteps), ...]
seen = []
while len(queue) > 0:
    currentPos, numSteps = queue.pop()
    seen.append(currentPos)
    r, c = currentPos
    for dr, dc in [(0,-1), (-1,0), (0,1), (1,0)]:
        rr, cc = r+dr, c+dc
        if not (0 <= rr < len(grid) and 0 <= cc < len(grid[r])):
            continue
        if (rr, cc) in seen:
            continue
        if grid[rr][cc] not in M[(dr, dc)]:
            continue
        D[(rr, cc)] = min(D[(rr, cc)], numSteps+1)
        queue.appendleft(((rr, cc), numSteps+1))

print(max(D.values()))
