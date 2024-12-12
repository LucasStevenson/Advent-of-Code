import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    GRID = []
    starting_idxs = []
    for r, line in enumerate(f.readlines()):
        GRID.append(list(map(int, line.strip())))
        for c, num in enumerate(line.strip()):
            if int(num) == 0:
                starting_idxs.append((r, c))

def dfs(r, c):
    if GRID[r][c] == 9:
        return 1
    ans = 0
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        rr, cc = r+dr, c+dc
        if not (0 <= rr < len(GRID) and 0 <= cc < len(GRID[0])):
            continue
        if GRID[rr][cc] == GRID[r][c]+1:
            ans += dfs(rr, cc)
    return ans

print(sum([ dfs(r, c) for r, c in starting_idxs ]))
