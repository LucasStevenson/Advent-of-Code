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

def getVisitedPositions(grid, x, y):
    """(Pretty much copied from part 1)
    This function serves the purpose of getting all the visited positions from the initial grid setup (no added obstacles).
    If a position is NOT visited, then adding an obstacle there won't change anything. This will save us time when checking for loops"""
    gridCopy = [ line[:] for line in grid ]
    visited = set()
    while True:
        symbol = gridCopy[x][y]
        xx, yy = x+DIRS[symbol][0], y+DIRS[symbol][1]
        if not (0 <= xx < len(gridCopy) and 0 <= yy < len(gridCopy[0])):
            break
        if gridCopy[xx][yy] == '#':
            gridCopy[x][y] = ROTATE[symbol]
            continue
        visited.add((xx,yy))
        gridCopy[xx][yy] = symbol
        x, y = xx, yy
    return visited

def containsLoop(grid, x, y):
    gridCopy = [ line[:] for line in grid ]
    seen = set()
    while True:
        symbol = gridCopy[x][y]
        xx, yy = x+DIRS[symbol][0], y+DIRS[symbol][1]
        if (xx, yy, symbol) in seen:
            return True
        if not (0 <= xx < len(gridCopy) and 0 <= yy < len(gridCopy[0])):
            return False
        if gridCopy[xx][yy] == '#':
            gridCopy[x][y] = ROTATE[symbol]
            continue
        seen.add((xx, yy, symbol))
        gridCopy[xx][yy] = symbol
        x, y = xx, yy

ans = 0
for r, c in getVisitedPositions(grid, x, y):
    if r == x and c == y:
        continue
    grid[r][c] = '#'
    if containsLoop(grid, x, y):
        ans += 1
    grid[r][c] = '.'
print(ans)
