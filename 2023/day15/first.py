import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    steps = f.read().replace("\n", "").split(",")

ans = 0
for step in steps:
    currentValue = 0
    for c in step:
        currentValue += ord(c)
        currentValue *= 17
    ans += currentValue%256
print(ans)
