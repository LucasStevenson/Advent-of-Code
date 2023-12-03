import sys
import math
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    row = 0
    grid = []
    D = {} # { (x,y): starting index of number }
    # example: [[4, 5, 6, ., ., ., ., ., .]]
    #          [[., ., ., ., 1, 2, 3, ., .]]
    # D = {(0,0): 456, (1,4): 123}
    while line := f.readline().strip():
        grid.append(list(line))
        result = re.finditer(r"\d+", line)
        for match_obj in result:
            D[(row, match_obj.span()[0])] = int(match_obj.group())
        row += 1

def check_valid_gear(r, c):
    partNum_coords = set() # holds the coordinates of all adjacent `part numbers`
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1,-1), (1,0), (1,1)]:
        rr, cc = r+dr, c+dc
        if not (0 <= rr < len(grid) and 0 <= cc < len(grid[rr])):
            continue
        if grid[rr][cc].isdigit():
            # we found an adjacent number; need to get the position of the left most digit and add to `partNum_coords`
            while grid[rr][cc].isdigit():
                cc-=1
            partNum_coords.add((rr, cc+1))
    return len(partNum_coords) == 2, math.prod(map(lambda x: D[x], partNum_coords))

ans = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != "*":
            continue
        isValid, product = check_valid_gear(r, c)
        ans += product if isValid else 0
print(ans)
