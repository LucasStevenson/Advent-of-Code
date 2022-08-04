import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.rstrip() for line in f.readlines() if line.strip() ]

def getMostCommonBit(arr):
    count = sum(map(int, arr))
    ans = count/len(arr)
    # if there's same amount of 0's and 1's, return 1
    if ans == 0.5: return 1
    return round(ans)

def solution(rating):
    arr = lines.copy()
    idx = 0
    while len(arr) > 1:
        transposedBits = list(zip(*arr))
        mostCommonBit = getMostCommonBit(transposedBits[idx])
        bit = mostCommonBit if rating == "oxygen" else not mostCommonBit
        for i, num in enumerate(arr):
            if int(num[idx]) != bit:
                arr[i] = None
        arr = list(filter(lambda el: el != None, arr))
        idx += 1
    return int(arr[0], 2)

print(solution("oxygen") * solution("co2"))
