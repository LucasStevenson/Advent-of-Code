import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    grid = []
    x, y = -1, -1
    for i, line in enumerate(f.readlines()):
        if x == -1 and '^' in line:
            x, y = i, line.index('^') 
        grid.append(list(line.strip()))

DIRS = {
    '^': [-1, 0],
    '>': [0, 1],
    'v': [1,0],
    '<': [0,-1]
}
ROTATE = { '>': 'v', 'v': '<', '<': '^', '^': '>' }
ans = {(x, y)}
while True:
    symbol = grid[x][y]
    xx, yy = x+DIRS[symbol][0], y+DIRS[symbol][1]
    if not (0 <= xx < len(grid) and 0 <= yy < len(grid[0])):
        break
    if grid[xx][yy] == '#': # we need to rotate
        grid[x][y] = ROTATE[symbol]
        continue
    ans.add((xx,yy))
    grid[xx][yy] = symbol
    x, y = xx, yy
print(len(ans))
