import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    takenSpots = set()
    beacons = set()
    ROW = 2000000 if infile == "../input.txt" else 10
    for line in f.readlines():
        sx, sy, bx, by = map(int, re.findall(r"\=(\-?\d+)", line))
        beacons.add((bx,by))
        distance = abs(sx-bx) + abs(sy-by)
        xDist = distance - abs(sy-ROW)
        for i in range(0, xDist+1):
            takenSpots.add((sx+i, ROW))
            takenSpots.add((sx-i, ROW))

print(len(takenSpots-beacons))
