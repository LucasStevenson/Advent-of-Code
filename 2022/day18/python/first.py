import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    lines = set([ tuple(map(int, line.split(","))) for line in f.readlines() ])

count = 0
# check to see if another cube exists on any of the six sides
# (x±1,y,z), (x,y±1,z), (x,y,z±1)
# if it does not exist, it's an open side, increment count 
for x, y, z in lines:
    if (x+1, y, z) not in lines:
        count += 1
    if (x-1, y, z) not in lines:
        count += 1
    if (x, y+1, z) not in lines:
        count += 1
    if (x, y-1, z) not in lines:
        count += 1
    if (x, y, z+1) not in lines:
        count += 1
    if (x, y, z-1) not in lines:
        count += 1

print(count)
