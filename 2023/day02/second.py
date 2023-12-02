import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.strip() for line in f.readlines() if line.strip() ]

ans = 0
for i, line in enumerate(lines):
    sets = line.split(": ")[1].split(";")
    D = defaultdict(int)
    for s in sets:
        for cubes in s.split(", "):
            numCubes, color = cubes.split()
            D[color] = max(D[color], int(numCubes))
    power = D["blue"] * D["green"] * D["red"]
    ans += power
print(ans)
