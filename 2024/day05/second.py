import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def insertionSort(line, D):
    lineCopy = line.copy() # don't wanna modify original `line`
    for i in range(0, len(lineCopy)):
        for j in range(i, 0, -1):
            if lineCopy[j] in D[lineCopy[j-1]]: # lineCopy[j] < lineCopy[j-1]
                lineCopy[j], lineCopy[j-1] = lineCopy[j-1], lineCopy[j]
            else:
                break
    return lineCopy

with open(infile) as f:
    D = defaultdict(list) # {x: [nums that should appear BEFORE x]}
    while line := f.readline().strip():
        a, b = [ int(x) for x in line.split("|")]
        D[b].append(a)
    ans = 0
    while line := f.readline().strip():
        line = [int(x) for x in line.split(",")]
        sortedLine = insertionSort(line, D)
        if sortedLine != line:
            ans += sortedLine[len(sortedLine)//2]
    print(ans)
