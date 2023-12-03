import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    grid = []
    while line := f.readline().strip():
        grid.append(list(line))

def is_adj_to_symbol(r, c):
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1,-1), (1,0), (1,1)]:
        rr, cc = r+dr, c+dc
        if not (0 <= rr < len(grid) and 0 <= cc < len(grid[rr])):
            continue
        if grid[rr][cc].isdigit() or grid[rr][cc] == ".":
            continue
        return True
    return False

ans = 0
for r in range(len(grid)):
    num = ""
    for c in range(len(grid[r])):
        if grid[r][c].isdigit():
            num += grid[r][c]
            if not (c == len(grid[r])-1): # if number is not in last column, we can skip
                continue
        if any([ is_adj_to_symbol(r, c-i) for i in range(1, len(num)+1) ]): # this wont run if `num` is emptyu
            ans += int(num)
        num = ""
print(ans)
