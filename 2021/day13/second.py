import sys
from PIL import Image, ImageDraw
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

f = open(infile).read()
foldInstrucs = list(map(lambda a: [a[0], int(a[1])], re.findall(r"([xy])=(\d+)", f)))
points = list(map(lambda p: (int(p[0]), int(p[1])), re.findall(r"(\d+)\,(\d+)", f)))

def flip(arr, axis, line):
    s = set()
    for point in arr:
        x, y = point[0], point[1]
        if axis == "y":
            y = line - abs(y-line)
        elif axis == "x":
            x = line - abs(x-line)
        s.add((x, y))
    return s

for i in foldInstrucs:
    points = flip(points, i[0], i[1])

im = Image.new("RGB", (400, 300))
draw = ImageDraw.Draw(im)
for i in points:
    draw.point((i[0], i[1]), fill=255)
im.show()
