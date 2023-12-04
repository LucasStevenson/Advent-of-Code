import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    ans = 0
    while line := f.readline().strip():
        winningNums, myNums = map(lambda x: set(x.split()), line.split(": ")[1].split(" | "))
        numMatches = len(winningNums.intersection(myNums))
        ans += int(pow(2, numMatches-1))
    print(ans)
