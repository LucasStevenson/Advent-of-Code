import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    GRID = [line.strip() for line in f.readlines()]
    seen = set()

def findRegion(r, c):
    seen.add((r, c))
    perimeter = 0
    area = 1
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        rr, cc = r+dr, c+dc
        if not (0 <= rr < len(GRID) and 0 <= cc < len(GRID[0])):
            perimeter += 1
            continue
        if GRID[rr][cc] != GRID[r][c]:
            perimeter += 1
            continue
        if (rr, cc) in seen:
            continue
        ret1, ret2 = findRegion(rr, cc)
        area += ret1
        perimeter += ret2
    return area, perimeter

ans = 0
for r in range(len(GRID)):
    for c in range(len(GRID[0])):
        if (r, c) in seen:
            continue
        area, perimeter = findRegion(r, c)
        ans += area * perimeter
print(ans)
