import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.rstrip() for line in f.readlines() if line.strip() ]
    foldInstrucs = [ re.search(r"fold along (.+)", el)[1].split("=") for el in lines if el.startswith("fold") ]
    points = [ tuple(map(int,el.split(","))) for el in lines if not el.startswith("fold") ]

def flip(arr, axis, line):
    s = set()
    line = int(line)
    for point in arr:
        x, y = point[0], point[1]
        if axis == "y":
            y = line - abs(y-line)
        elif axis == "x":
            x = line - abs(x-line)
        s.add((x, y))
    return s

print(len(flip(points, *foldInstrucs[0])))
