import sys
from collections import Counter
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

f = open(infile).read()
rules = dict(re.findall(r"(\w{2})\s\->\s(\w)", f))
template = re.search(r"\w+", f)[0]

# NAIVE APPROACH
def solution(steps, template):
    for _ in range(steps):
        t = template[0]
        for c in range(1, len(template)):
            first, second = template[c-1], template[c]
            t += rules[first+second]+second
        template = t
    return template

q = Counter(solution(10, template))
s = min(q, key=q.get)
b = max(q, key=q.get)
print(q[b]-q[s])
