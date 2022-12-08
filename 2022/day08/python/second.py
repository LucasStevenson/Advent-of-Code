import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    lines = [[ int(x) for x in list(line.rstrip()) ] for line in f.readlines() if line.strip() ]

def getScore(r, c):
    left, right, up, down = 0, 0, 0, 0
    # check right
    for x in lines[r][c+1:]:
        right += 1
        if x >= lines[r][c]:
            break
    # check left
    for x in reversed(lines[r][0:c]):
        left += 1
        if x >= lines[r][c]:
            break
    # check up
    for i in range(r-1, -1, -1):
        up += 1
        if lines[i][c] >= lines[r][c]:
            break
    # check down
    for i in range(r+1, len(lines)):
        down += 1
        if lines[i][c] >= lines[r][c]:
            break
    return left*up*right*down

ans = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        ans = max(ans, getScore(r,c))
print(ans)
