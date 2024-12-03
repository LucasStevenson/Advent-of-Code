import sys
import numpy as np
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.strip().split() for line in f.readlines()]
    left, right = np.array(lines).T.astype(int)
    print(sum([ abs(a-b) for a, b in zip(sorted(left), sorted(right)) ]))
