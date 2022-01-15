import sys
from collections import defaultdict, Counter
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


with open(infile) as f:
    line = list(map(int,f.read().rstrip().split(",")))

def getFish(arr, days):
    count = Counter(arr) # keeps track of how many of each number there are
    nextCount = defaultdict(int) # holds the count of the next iteration
    for i in range(days):
        for n in count:
            c = count[n]
            if n <= 0:
                nextCount[6] += c
                nextCount[8] += c
            else:
                nextCount[n-1] += c
        count = Counter(nextCount)
        nextCount = defaultdict(int)

    return sum(v for k,v in count.items())

print(getFish(line, 256))
