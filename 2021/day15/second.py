import sys
import heapq
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

startingCave = []
for line in open(infile):
    startingCave.append([ int(x) for x in line.strip() ])

def getRemainingRightTiles(row, n):
    remainingRightTiles = []
    for i in range(n):
        for el in row:
            remainingRightTiles.append((el+i)%9+1)
    return remainingRightTiles

def getRemainingDownTiles(table, n):
    remainingDownTiles = []
    for i in range(n):
        for r in range(len(table)):
            t = []
            for c in range(len(table[r])):
                t.append((table[r][c]+i)%9+1)
            remainingDownTiles.append(t)
    return remainingDownTiles

startingCave += getRemainingDownTiles(startingCave, 4)
cave = []
for row in startingCave:
    cave.append(row + getRemainingRightTiles(row, 4))

def dijkstra(lines):
    r, c = 0, 0
    distances = defaultdict(lambda: float("inf"))
    distances[(0,0)] = 0
    pq = [(0, (r, c))]
    while pq:
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            if not (0 <= r+dr < len(lines) and 0 <= c+dc < len(lines[r])):
                continue
            rr = r+dr
            cc = c+dc
            if distances[(r, c)] + lines[rr][cc] < distances[(rr, cc)]:
                distances[(rr, cc)] = distances[(r, c)] + lines[rr][cc]
                heapq.heappush(pq, (distances[(rr, cc)], (rr, cc)))
        smallestVal = heapq.heappop(pq)[1]
        r, c = smallestVal[0], smallestVal[1]
    return distances[(len(lines)-1,len(lines)-1)]

print(dijkstra(cave))
