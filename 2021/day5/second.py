import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = f.readline().rstrip()
    obj = {}
    while line:
        points = [ list(map(int,point.split(","))) for point in line.split(" -> ")]
        x1, y1, x2, y2 = points[0] + points[1]

        if y1 == y2:
            for x in range(abs(x1-x2)+1):
                if (min(x1, x2)+x,y1) not in obj:
                    obj[(min(x1, x2)+x, y1)] = 1
                else:
                    obj[(min(x1, x2)+x, y1)] += 1
        elif x1 == x2:
            for y in range(abs(y1-y2)+1):
                if (x1, min(y1, y2)+y) not in obj:
                    obj[(x1, min(y1, y2)+y)] = 1
                else:
                    obj[(x1, min(y1, y2)+y)] += 1
        else:
            slope = (y2-y1)/(x2-x1)
            for x in range(min(x1, x2), max(x1, x2)+1):
                y = slope*(x-x1)+y1
                if (x, y) not in obj:
                    obj[(x, y)] = 1
                else:
                    obj[(x, y)] += 1

        line = f.readline().rstrip()

    count = 0
    for k, v in obj.items():
        if v >= 2:
            count += 1
    print(count)
