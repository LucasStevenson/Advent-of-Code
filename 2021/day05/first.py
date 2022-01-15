import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = f.readline().rstrip()
    obj = defaultdict(int)
    while line:
        points = [ list(map(int,point.split(","))) for point in line.split(" -> ")]
        x1, y1, x2, y2 = points[0] + points[1]

        if y1 == y2:
            for x in range(abs(x1-x2)+1):
                obj[(min(x1, x2)+x, y1)] += 1
        elif x1 == x2:
            for y in range(abs(y1-y2)+1):
                obj[(x1, min(y1, y2)+y)] += 1

        line = f.readline().rstrip()

    count = 0
    for k, v in obj.items():
        if v >= 2:
            count += 1
    print(count)


