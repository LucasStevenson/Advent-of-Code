import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    GRID = []
    D = defaultdict(list) # { symbol: [(r, c) positions] }
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
            ri, ci = positions[i]
            rj, cj = positions[j]
            r_dist, c_dist = rj-ri, cj-ci # calculate the distance between each pair of points
            rri, cci = ri-r_dist, ci-c_dist
            rrj, ccj = rj+r_dist, cj+c_dist
            if (0 <= rri < len(GRID)) and (0 <= cci < len(GRID[0])):
                seen.add((rri, cci))
            if (0 <= rrj < len(GRID) and (0 <= ccj < len(GRID[0]))):
                seen.add((rrj, ccj))
print(len(seen))
