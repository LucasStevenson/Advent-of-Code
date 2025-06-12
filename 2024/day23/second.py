import sys
import networkx as nx
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    G = nx.Graph()
    for a, b in map(lambda x: x.strip().split('-'), f.readlines()):
        G.add_edge(a, b)

cliques = list(nx.find_cliques(G))
ans = ",".join(sorted(max(cliques, key=len)))
print(ans)
