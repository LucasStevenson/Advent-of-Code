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

def solution(key, seq=[], paths=[]):
    count = 0
    for i in obj[key]:
        sc = seq.copy()
        if i == "end":
            paths.append(sc)
            continue
        if i.islower() and i in sc:
            continue
        sc.append(i)
        solution(i, sc, paths)
    return len(paths)

print(solution("start"))
