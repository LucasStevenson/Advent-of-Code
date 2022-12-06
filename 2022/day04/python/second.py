import sys
import re
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    count = 0
    while line := f.readline().rstrip():
        first, second, third, fourth = map(int, re.findall(r"\d+", line))
        range1, range2 = range(first,second+1), range(third,fourth+1)
        if first in range2 or second in range2 or third in range1: # dont need to check fourth
            count += 1
    print(count)
