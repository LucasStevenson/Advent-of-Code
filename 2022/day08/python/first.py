import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    lines = [[ int(x) for x in list(line.rstrip()) ] for line in f.readlines() if line.strip() ]

def checkPoint(r, c):
    if r == 0 or c == 0 or r == len(lines)-1 or c == len(lines[r])-1:
        # takes care of edges
        return 1
    # r, c is not an edge, check all 4 directions
    # check right
    if all(x < lines[r][c] for x in lines[r][c+1:]):
        return 1
    # check left
    if all(x < lines[r][c] for x in lines[r][0:c]):
        return 1
    # check up
    if all(lines[i][c] < lines[r][c] for i in range(r)):
        return 1
    # check down
    if all(lines[i][c] < lines[r][c] for i in range(r+1, len(lines))):
        return 1
    return 0

ans = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        ans += checkPoint(r,c)
print(ans)
