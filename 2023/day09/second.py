import sys
from collections import deque
import functools
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    ans = 0
    while line := f.readline().strip():
        d = deque()
        history = [int(x) for x in line.split()]
        d.appendleft(history[0])
        while not all([ x == 0 for x in history ]):
            history = [ history[i+1]-history[i] for i in range(len(history)-1) ]
            d.appendleft(history[0])
        ans += functools.reduce(lambda a, b: b-a, d)
print(ans)
