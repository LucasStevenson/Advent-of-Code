import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    ans = 0
    lines = [ line.rstrip() for line in f.readlines() ]
    for i in range(0, len(lines), 3):
        intersection = list(set.intersection(*[set(x) for x in lines[i:i+3]]))[0]
        ans += ord(intersection)-ord('a')+1 if intersection.islower() else ord(intersection)-ord('A')+27
    print(ans)
