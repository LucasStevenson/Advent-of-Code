import sys
from collections import Counter, defaultdict
import math
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

f = open(infile).read()
rules = dict(re.findall(r"(\w{2})\s\->\s(\w)", f))
template = re.search(r"\w+", f)[0]

def solution(steps, template):
    count = Counter([ template[i:i+2] for i in range(0, len(template)-1)])
    for _ in range(steps):
        obj = defaultdict(int)
        for k, v in count.items():
            obj[k[0]+rules[k]] += v
            obj[rules[k]+k[1]] += v
        count = Counter(obj)
    return count

c = solution(40, template)
letterCount = defaultdict(int)
for k, v in c.items():
    letterCount[k[0]] += v
    letterCount[k[1]] += v

numOccurances = [math.ceil(v/2) for k, v in letterCount.items()]
print(max(numOccurances) - min(numOccurances))
