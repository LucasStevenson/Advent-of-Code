import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def isCorrectOrder(line, D):
    for i in range(len(line)):
        for j in range(i-1, -1, -1):
            if line[j] not in D[line[i]]:
                return False
    return True

with open(infile) as f:
    D = defaultdict(list) # {x: [nums that should appear BEFORE x]}
    while line := f.readline().strip():
        a, b = [ int(x) for x in line.split("|")]
        D[b].append(a)
    ans = 0
    while line := f.readline().strip():
        line = [int(x) for x in line.split(",")]
        if isCorrectOrder(line, D):
            ans += line[len(line)//2]
    print(ans)
