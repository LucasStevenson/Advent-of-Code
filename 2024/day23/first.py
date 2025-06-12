import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    G = defaultdict(set)
    for a, b in map(lambda x: x.strip().split('-'), f.readlines()):
        G[a].add(b)
        G[b].add(a)

S = set()
for k, v in G.items():
    for child in v:
        startsT = k[0] == 't' or child[0] == 't'
        intersect = v.intersection(G[child])
        for i in intersect:
            if not startsT and not i[0] == 't':
                continue
            S.add(tuple(sorted((k, child, i))))
print(len(S))
