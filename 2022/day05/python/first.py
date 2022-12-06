import sys
from collections import defaultdict, deque
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

obj = defaultdict(deque) # {crateNumber: corresponding stack}
with open(infile) as f:
    while line := f.readline().rstrip(): # first read in all the crates and save to dict
        idx = 0
        for i in range(0, len(line), 4):
            if (el:=line[i:i+4].strip()) != "" and not el.isdigit():
                obj[idx+1].appendleft(el[1]) # el[1] to only get the letter (discard brackets)
            idx+=1

    while line := f.readline().rstrip(): # now parse the instructions
        amount, fromCrate, toCrate = map(int, re.findall(r"\d+", line))
        for _ in range(amount):
            obj[toCrate].append(obj[fromCrate].pop())

ans = "".join([ v[-1] for k,v in sorted(obj.items()) ])
print(ans)
