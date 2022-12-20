import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    allPoints = set()
    for line in f.readlines():
        points = re.findall(r"(\d+)\,(\d+)", line)
        for i in range(len(points)-1):
            x1, y1 = map(int, points[i])
            x2, y2 = map(int, points[i+1])
            allPoints.add((x1,y1))
            allPoints.add((x2,y2))
            # all lines are either vertical or horizontal
            if x1 == x2:
                for n in range(min(y1,y2)+1, max(y1,y2)):
                    allPoints.add((x1, n))
            else:
                for n in range(min(x1,x2)+1, max(x1,x2)):
                    allPoints.add((n, y1))


largestY = max(allPoints, key=lambda t:t[1])[1]
count = 0
done = False
while not done:
    START = (500, 0)
    while True:
        x, y = START
        if y > largestY:
            done = True
            break
        if (x, y+1) not in allPoints: # not occupied
            START = (x,y+1)
            continue
        if (x-1,y+1) not in allPoints: # not occupied
            START = (x-1,y+1)
            continue
        if (x+1,y+1) not in allPoints: # not occupied
            START = (x+1,y+1)
            continue
        allPoints.add((x,y))
        count += 1
        break

print(count)
