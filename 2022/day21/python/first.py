import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    G = {}
    while line := f.readline().rstrip():
        k, v = line.split(": ")
        if v.isdigit():
            G[k] = int(v)
            continue
        G[k] = v.split()

def solution(key):
    if type(G[key]) == int:
        return G[key]
    m1, op, m2 = G[key]
    return int(eval(f"{solution(m1)} {op} {solution(m2)}"))

print(solution("root"))
