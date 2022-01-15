import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ list(map(int, list(line.rstrip()))) for line in f.readlines() if line.strip() ]

lowestPoints = []
for r in range(len(lines)):
    for c in range(len(lines[r])):
        left = lines[r][c-1] if c-1 >=0 else 10
        right = lines[r][c+1] if c+1 < len(lines[r]) else 10
        up = lines[r-1][c] if r-1 >= 0 else 10
        down = lines[r+1][c] if r+1 < len(lines) else 10
        if lines[r][c] < left and lines[r][c] < right and lines[r][c] < up and lines[r][c] < down:
            lowestPoints.append(lines[r][c]+1)
print(sum(lowestPoints))
