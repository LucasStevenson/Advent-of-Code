import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ list(map(int, list(line.rstrip()))) for line in f.readlines() if line.strip() ]

lowestPoints = []
for r in range(len(lines)):
    for c in range(len(lines[r])):
        left = lines[r][c-1] if c-1 >=0 else 10
        right = lines[r][c+1] if c+1 < len(lines[r]) else 10
        up = lines[r-1][c] if r-1 >= 0 else 10
        down = lines[r+1][c] if r+1 < len(lines) else 10
        if lines[r][c] < left and lines[r][c] < right and lines[r][c] < up and lines[r][c] < down:
            lowestPoints.append((r, c))

points = set()

def solution(r, c):
    if (r < 0 or r >= len(lines) or c < 0 or c >= len(lines[r])) or (lines[r][c] == 9) or ((r, c) in points):
        return 0
    points.add((r, c))
    size = 1
    size += solution(r, c-1) + solution(r, c+1) + solution(r+1, c) + solution(r-1, c)
    return size


arr = []
for i in lowestPoints:
    arr.append(solution(i[0], i[1]))
arr = sorted(arr)
print(arr[-1]*arr[-2]*arr[-3])
