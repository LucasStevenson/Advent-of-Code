import sys 
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.strip() for line in f.readlines() ]

# Checks if going a certain direction (dr,dc) from point (r,c) matches with "XMAS"
def checkMatch(r, c, dr, dc):
    for step in range(1, len("XMAS")):
        if not (0 <= r+step*dr < len(lines) and 0 <= c+step*dc < len(lines[r])):
            return False
        if lines[r+step*dr][c+step*dc] != "XMAS"[step]:
            return False
    return True

ans = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] != 'X':
            continue
        for dr, dc in [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]:
            ans += bool(checkMatch(r, c, dr, dc))
print(ans)
