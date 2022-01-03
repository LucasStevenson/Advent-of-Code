import sys
import heapq
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

lines = []
for line in open(infile):
    lines.append([int(x) for x in line.strip()])

r, c = 0, 0
distances = defaultdict(lambda: float("inf"))
distances[(0,0)] = 0
pq = [(0, (r, c))]

while pq:
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        # check a point's neighbors
        if not (0 <= r+dr < len(lines) and 0 <= c+dc < len(lines[r])):
            continue
        rr = r+dr
        cc = c+dc
        if distances[(r, c)] + lines[rr][cc] < distances[(rr, cc)]:
            distances[(rr, cc)] = distances[(r, c)] + lines[rr][cc]
            heapq.heappush(pq, (distances[(rr, cc)], (rr, cc)))

    smallestVal = heapq.heappop(pq)[1]
    r, c = smallestVal[0], smallestVal[1]

print(distances[(len(lines)-1,len(lines)-1)])
