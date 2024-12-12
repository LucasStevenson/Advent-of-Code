import sys
from collections import Counter
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    line = list(map(int, f.readline().split()))
    D = Counter(line) # { num: number of occurances }

def solve(numIterations):
    for _ in range(numIterations):
        for num, occurances in list(D.items()):
            D[num] -= occurances
            if num == 0:
                D[1] += occurances
                continue
            num_str = str(num)
            if len(num_str) % 2 == 0:
                D[int(num_str[0:len(num_str)//2])] += occurances
                D[int(num_str[len(num_str)//2:])] += occurances
            else:
                D[num*2024] += occurances
    return sum(D.values())

print(solve(75))
