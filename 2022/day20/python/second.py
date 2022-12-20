import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"
with open(infile) as f:
    lines = [ (i, int(x)*811589153) for i, x in enumerate(f.readlines()) ]
    og = lines.copy()
    length = len(lines)

def mix(lines):
    for idx, el in og:
        i = lines.index((idx, el))
        newIdx = (i+el)%(length-1)
        if newIdx != 0:
            lines.insert(newIdx, lines.pop(i))
            continue
        lines.append(lines.pop(i))

# mix 10 times
for _ in range(10):
    mix(lines)
# find where 0 appears in the list
for i, val in enumerate(lines):
    if val[1] == 0:
        zeroIdx = i
        break
print(sum(lines[(zeroIdx+n)%length][1] for n in [1000, 2000, 3000]))
