import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    ans = 0
    while line := f.readline().rstrip():
        firstHalf, secondHalf = set(line[:len(line)//2]), set(line[len(line)//2:])
        intersection = list(firstHalf.intersection(secondHalf))[0]
        ans += ord(intersection)-ord('a')+1 if intersection.islower() else ord(intersection)-ord('A')+27
    print(ans)
