import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    GRID = []
    D = defaultdict(list) # { symbol: [(x, y) positions] }
    for r, line in enumerate(f.readlines()):
        line = line.strip()
        GRID.append(list(line))
        for c in range(len(line)):
            if line[c] != '.':
                D[line[c]].append((r, c))

seen = set()
for symbol, positions in D.items():
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            xi, yi = positions[i]
            xj, yj = positions[j]
            x_dist, y_dist = xj-xi, yj-yi # calculate the distance between each pair of points
            xxi, yyi = xi-x_dist, yi-y_dist
            xxj, yyj = xj+x_dist, yj+y_dist
            if (0 <= xxi < len(GRID)) and (0 <= yyi < len(GRID[0])):
                seen.add((xxi, yyi))
            if (0 <= xxj < len(GRID) and (0 <= yyj < len(GRID[0]))):
                seen.add((xxj, yyj))
print(len(seen))
