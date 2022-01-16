import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = f.readline().rstrip()
    obj = defaultdict(list)
    while line:
        a ,b = line.split("-")
        if b != "start" and a != "end": obj[a].append(b) 
        if a != "start" and b != "end": obj[b].append(a) 
        line = f.readline().rstrip()

def solution(key, seq=[]):
    numPaths = 0
    for adjacentNode in obj[key]:
        if adjacentNode == "end":
            numPaths += 1
            continue
        if adjacentNode.islower() and adjacentNode in seq:
            continue
        numPaths += solution(adjacentNode, seq+[adjacentNode])
    return numPaths

print(solution("start"))
