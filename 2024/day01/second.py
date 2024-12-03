import sys
import numpy as np
from collections import Counter
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.strip().split() for line in f.readlines()]
    left, right = np.array(lines).T.astype(int)
    r_freq = Counter(right)
    print(sum([ x*r_freq[x] for x in left ]))
