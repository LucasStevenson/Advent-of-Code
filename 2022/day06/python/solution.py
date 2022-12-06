import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    line = f.readline().rstrip()

def solution(n):
    for i in range(len(line)-n):
        if len(set(line[i:i+n])) == n:
            return i+n
    return 0

print(f"Part 1: {solution(4)}")
print(f"Part 2: {solution(14)}")
