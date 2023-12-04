import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    D = defaultdict(int) # { cardNum: numCopies }
    for cardNum, line in enumerate(map(lambda x: x.strip(), f.readlines())):
        D[cardNum+1] += 1
        winningNums, myNums = map(lambda x: set(x.split()), line.split(": ")[1].split(" | "))
        numMatches = len(winningNums.intersection(myNums))
        for i in range(1, numMatches+1):
            D[cardNum+1+i] += D[cardNum+1]
    print(sum(D.values()))
