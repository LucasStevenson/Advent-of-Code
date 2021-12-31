import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

lines = []
for line in open(infile):
    lines.append([int(x) for x in line.strip()])

r, c = 0, 0
distances = defaultdict(lambda: float("inf"))
distances[(0,0)] = 0
relaxedPoints = set()


def updateDistances(r, c):
    if c + 1 < len(lines[0]):
        down = (lines[r][c+1], (r, c+1))
        if distances[(r, c)] + down[0] < distances[down[1]]:
            distances[down[1]] = distances[(r, c)] + down[0]

    if r + 1 < len(lines):
        right = (lines[r+1][c], (r+1, c))
        if distances[(r, c)] + right[0] < distances[right[1]]:
            distances[right[1]] = distances[(r, c)] + right[0]

    if r - 1 >= 0:
        left = (lines[r-1][c], (r-1, c))
        if distances[(r, c)] + left[0] < distances[left[1]]:
            distances[left[1]] = distances[(r, c)] + left[0]

    if c - 1 >= 0:
        top = (lines[r][c-1], (r, c-1))
        if distances[(r, c)] + top[0] < distances[top[1]]:
            distances[top[1]] = distances[(r, c)] + top[0]

while True:
    updateDistances(r, c)
    smallestVal = float("inf")
    smallestKey = None

    for k, v in distances.items():
        if k in relaxedPoints:
            continue
        if v < smallestVal:
            smallestVal = v
            smallestKey = k
        
    if smallestKey == None:
        break
    r, c = smallestKey[0], smallestKey[1]
    relaxedPoints.add(smallestKey)

print(distances[(len(lines)-1, len(lines[0])-1)])
