import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def isGoodLine(line):
    sign = line[1]-line[0] < 0
    for i in range(len(line)-1):
        if not (1 <= abs(line[i+1]-line[i]) <= 3):
            return False
        if (line[i+1]-line[i] < 0) != sign:
            return False
    return True

with open(infile) as f:
    ans = 0
    while line := f.readline().strip():
        splitted = list(map(int, line.split()))
        ans += int(isGoodLine(splitted))
    print(ans)
