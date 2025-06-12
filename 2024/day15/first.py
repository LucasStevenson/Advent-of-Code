import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    grid, instructs = f.read().strip().split("\n\n")
    G = []
    r, c = -1, -1
    for row, line in enumerate(grid.split("\n")):
        if r == -1 and '@' in line:
            r, c = row, line.index('@')
        G.append(list(line))
    instructs = instructs.replace("\n", "")

DIRS = {
    '>': (0,1),
    '<': (0,-1),
    'v': (1,0),
    '^': (-1,0),
}

def movedBoxes(r, c, dr, dc):
    rr, cc = r+dr, c+dc
    if G[rr][cc] == '#': # then we cannot pass
        return False
    if G[rr][cc] == '.': # no obstacle, we can scoot over
        G[r][c] = '.'
        G[rr][cc] = 'O'
        return True
    if G[rr][cc] == 'O' and movedBoxes(rr, cc, dr, dc): # then we can scoot over
        G[r][c] = '.'
        G[rr][cc] = 'O'
        return True
    return False

for instruct in instructs:
    dr, dc = DIRS[instruct]
    rr, cc = r+dr, c+dc
    if G[rr][cc] == '#':
        continue
    if G[rr][cc] == '.':
        G[r][c] = '.'
        G[rr][cc] = '@'
        r, c = rr, cc
        continue
    if movedBoxes(rr, cc, dr, dc):
        G[r][c] = '.'
        G[rr][cc] = '@'
        r, c = rr, cc

ans = 0
for r in range(len(G)):
    for c in range(len(G[r])):
        if G[r][c] != 'O':
            continue
        ans += 100*r + c
print(ans)
